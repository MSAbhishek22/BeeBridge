/* BeeBridge — 3D beehive (hero).
 * Classic script, Three.js r160 UMD from jsDelivr (window.THREE).
 * Auto-inits on first load. Drag to rotate. One still frame under
 * prefers-reduced-motion; pauses off-screen. Guarded no-op if the
 * CDN or WebGL is unavailable. */
(function () {
  'use strict';
  var canvas = document.getElementById('hero3d');
  if (!canvas || typeof THREE === 'undefined') return;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
  } catch (e) { return; }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
  camera.position.set(0, 3.4, 7.6);
  camera.lookAt(0, 0.4, 0);
  scene.add(new THREE.AmbientLight(0xfff2d0, 0.7));
  var key = new THREE.DirectionalLight(0xffd479, 1.4);
  key.position.set(4, 7, 5);
  scene.add(key);
  var fill = new THREE.PointLight(0xffb020, 10, 18);
  fill.position.set(-4, 2, 3);
  scene.add(fill);

  var world = new THREE.Group();
  scene.add(world);

  /* Hex-cell lattice: a domed honeycomb of golden cells. */
  var gold = new THREE.MeshStandardMaterial({ color: 0xd99a26, roughness: 0.45, metalness: 0.25 });
  var goldBright = new THREE.MeshStandardMaterial({ color: 0xffc84d, roughness: 0.35, metalness: 0.3, emissive: 0x664400, emissiveIntensity: 0.35 });
  var cellGeo = new THREE.CylinderGeometry(0.42, 0.42, 0.3, 6);
  var nodes = [];
  var rows = [-2, -1, 0, 1, 2];
  rows.forEach(function (row) {
    var count = 5 - Math.abs(row);
    for (var i = 0; i < count; i++) {
      var x = (i - (count - 1) / 2) * 0.78;
      var z = row * 0.68 + (Math.abs(row) % 2 ? 0.34 : 0);
      var dome = Math.max(0, 1 - (x * x + z * z) / 9) * 0.55;
      var isNode = (row + i) % 4 === 0;
      var cell = new THREE.Mesh(cellGeo, isNode ? goldBright : gold);
      cell.position.set(x, dome, z);
      cell.rotation.y = Math.PI / 6;
      cell.userData.isNode = isNode;
      cell.userData.phase = (row + 3) * 1.1 + i * 0.7;
      world.add(cell);
      if (isNode) nodes.push(cell);
    }
  });
  /* Hive base disc. */
  var base = new THREE.Mesh(
    new THREE.CylinderGeometry(2.5, 2.7, 0.22, 48),
    new THREE.MeshStandardMaterial({ color: 0x2a1c08, roughness: 0.8 })
  );
  base.position.y = -0.22;
  world.add(base);

  /* Orbiting bee: gold body, dark stripes, two wings. */
  var bee = new THREE.Group();
  var body = new THREE.Mesh(
    new THREE.SphereGeometry(0.22, 20, 16),
    new THREE.MeshStandardMaterial({ color: 0xffc84d, roughness: 0.4 })
  );
  body.scale.set(1.25, 1, 1);
  bee.add(body);
  [-0.08, 0.08].forEach(function (dx) {
    var stripe = new THREE.Mesh(
      new THREE.TorusGeometry(0.2, 0.035, 8, 20),
      new THREE.MeshStandardMaterial({ color: 0x201404, roughness: 0.6 })
    );
    stripe.position.x = dx;
    stripe.rotation.y = Math.PI / 2;
    bee.add(stripe);
  });
  var wingMat = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.55, side: THREE.DoubleSide });
  [-1, 1].forEach(function (s) {
    var wing = new THREE.Mesh(new THREE.CircleGeometry(0.2, 16), wingMat);
    wing.position.set(0, 0.16, s * 0.16);
    wing.rotation.x = -Math.PI / 2 + s * 0.5;
    wing.scale.set(1, 1.6, 1);
    bee.add(wing);
  });
  world.add(bee);

  /* Floating pollen motes. */
  var pCount = 90, pPos = new Float32Array(pCount * 3);
  for (var i = 0; i < pCount; i++) {
    var a = Math.random() * Math.PI * 2, r = 1.5 + Math.random() * 3;
    pPos[i * 3] = Math.cos(a) * r;
    pPos[i * 3 + 1] = 0.2 + Math.random() * 2.6;
    pPos[i * 3 + 2] = Math.sin(a) * r;
  }
  var pGeo = new THREE.BufferGeometry();
  pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
  world.add(new THREE.Points(pGeo, new THREE.PointsMaterial({ color: 0xffd479, size: 0.05, transparent: true, opacity: 0.85 })));

  var rotY = 0, targetRotY = 0, dragging = false, lastX = 0;
  canvas.addEventListener('pointerdown', function (e) { dragging = true; lastX = e.clientX; canvas.setPointerCapture(e.pointerId); });
  canvas.addEventListener('pointermove', function (e) {
    if (!dragging) return;
    targetRotY += (e.clientX - lastX) * 0.008;
    lastX = e.clientX;
  });
  function endDrag() { dragging = false; }
  canvas.addEventListener('pointerup', endDrag);
  canvas.addEventListener('pointercancel', endDrag);

  function resize() {
    var w = canvas.clientWidth || 800, h = canvas.clientHeight || 340;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
  window.addEventListener('resize', resize);
  resize();

  var visible = true;
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) { visible = entries[0].isIntersecting; }, { threshold: 0.02 }).observe(canvas);
  }

  var clock = new THREE.Clock();
  var raf = null;
  function frame() {
    raf = null;
    var t = clock.getElapsedTime();
    if (!dragging) targetRotY += 0.0016;
    rotY += (targetRotY - rotY) * 0.08;
    world.rotation.y = rotY;
    /* Bee orbits the hive on a tilted path, wings fluttering. */
    var a = t * 0.7;
    bee.position.set(Math.cos(a) * 3.1, 1.5 + Math.sin(t * 1.3) * 0.35, Math.sin(a) * 3.1);
    bee.rotation.y = -a;
    bee.rotation.z = 0.25;
    nodes.forEach(function (cell) {
      var s = 1 + 0.18 * Math.sin(t * 2 + cell.userData.phase);
      cell.scale.set(s, 1, s);
      cell.material.emissiveIntensity = 0.35 + 0.3 * Math.sin(t * 2 + cell.userData.phase);
    });
    renderer.render(scene, camera);
    if (!reduced && visible && !document.hidden) raf = requestAnimationFrame(frame);
  }
  function kick() { if (raf === null) { clock.getDelta(); raf = requestAnimationFrame(frame); } }
  document.addEventListener('visibilitychange', function () { if (!document.hidden) kick(); });
  if (reduced) { frame(); } else { kick(); }
  window.__beebridge3DReady = true;
})();
