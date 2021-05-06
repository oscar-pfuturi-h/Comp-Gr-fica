class Sphere {
    constructor(radius, alpha, theta, x, y, z, textures) {
        this.r = radius;
        this.a = alpha;
        this.t = theta;
        this.x = x;
        this.y = y;
        this.z = z;
        this.geometry = new THREE.SphereGeometry(this.r, this.a, this.t);
        this.setTexture(textures);
        this.mesh = new THREE.Mesh(this.geometry, this.material);
        this.mesh.position.set(this.x, this.y, this.z);
    }

    set position(newposition) {
        this.mesh.position.x = newposition[0];
        this.mesh.position.y = newposition[1];
        this.mesh.position.z = newposition[2];
    }
    setTexture(textures) { // creamos el material con una(s) textura(s)
        if (textures == null) {
            this.material = new THREE.MeshBasicMaterial({color:0x00ff00, wireframe: true});
        }
        else {
            var texture = new THREE.TextureLoader().load(textures[0]);
            if (textures[1] == null && textures[2] == null)
                this.material = new THREE.MeshPhongMaterial({map: texture})
            else if (textures[2] == null) {
                var bump = new THREE.TextureLoader().load(textures[1]);
                this.material = new THREE.MeshPhongMaterial({map: texture, bumpMap: bump, bumpScale: 0.05})
            }
            else if (textures[1] == null) {
                var specular = new THREE.TextureLoader().load(textures[2]);
                this.material = new THREE.MeshPhongMaterial({map: texture, specularMap: specular, specular: new THREE.Color('grey')})
            }
            else {
                var bump = new THREE.TextureLoader().load(textures[1]);
                var specular = new THREE.TextureLoader().load(textures[2]);
                this.material = new THREE.MeshPhongMaterial({map: texture, bumpMap: bump, bumpScale: 0.05, specularMap: specular, specular: new THREE.Color('grey')});
            }
        }
    }
}

class Planet extends Sphere {
    constructor(radius, alpha, theta, x, y, z, textures, name, orbitRate, rotationRate, nMoons, distance) {
        super(radius, alpha, theta, x, y, z, textures);
        this.name = name;
        this.orbitRate = orbitRate;
        this.rotationRate = rotationRate;
        this.nMoons = nMoons;
        this.distance = distance;
    }
    move() {
        var time = Date.now();
        this.x = -Math.cos(time * (1.0 / (this.orbitRate * orbitData.value)) + 10.0) * this.distance;
        this.z = Math.sin(time * (1.0 / (this.orbitRate * orbitData.value)) + 10.0) * this.distance;
        this.mesh.position.set(this.x, 0, this.z);
        this.mesh.rotation.y += this.rotationRate;
    }
    moveMoon(planetPosition) {
        this.move();
        this.mesh.position.x = this.mesh.position.x + planetPosition.x;
        this.mesh.position.z = this.mesh.position.z + planetPosition.z;
    }
}

var globalRate = 1.0, planetOrbit;
var orbitData = {value: 200, runOrbit: true, runRotation: true};

// sol
const sunRadius = 348.0; // reducido 1/2000
var sunGeometry = new THREE.SphereGeometry(sunRadius, 64, 64);
const texture_1 = new THREE.TextureLoader().load('textures/sun.jpg');
//const texture_2 = new THREE.TextureLoader().load('textures/sunspecular.jpg');
var sunMaterial = new THREE.MeshBasicMaterial({map: texture_1});
var sun = new THREE.Mesh(sunGeometry, sunMaterial);
sun.position.set(0, 0, 0);
var sunGeometry2 = new THREE.SphereGeometry(sunRadius + 3.48, 64, 64);
var sunMaterial2 = new THREE.MeshBasicMaterial({color: 0xff3200, opacity: 0.15,transparent: true});
var sunShine = new THREE.Mesh(sunGeometry2, sunMaterial2);
sun.add(sunShine);
var spriteMaterial = new THREE.SpriteMaterial(
    {
        map: new THREE.TextureLoader().load("textures/sunlight.png")
        , color: 0xffffee
        , transparent: false
        , blending: THREE.AdditiveBlending
    });
var sprite = new THREE.Sprite(spriteMaterial);
sprite.scale.set(1270, 1270, 1270.0);
sun.add(sprite);

// reduccion de la distancia 1/2000000
// reduccion del radio 1/2000
var mercury = new Planet(1.2, 12, 12, sunRadius + 29.0, 0, 0, ['textures/mercury.jpg', 'textures/mercurybump.jpg', null], 
                        'Mercurio', 58.64, 0.005, 0, sunRadius + 29.0);
var venus = new Planet(3.0, 32, 32, sunRadius + 54.1, 0, 0, ['textures/venus.jpg', 'textures/venusbump.jpg', null], 
                        'Venus', 73.55, 0.003, 0, sunRadius + 54.1);
var earth = new Planet(3.18, 32, 32, sunRadius + 74.8, 0, 0, ['textures/earth.jpg', 'textures/earthbump.jpg','textures/earthspecular.jpg'],                       'Tierra', 104.115, 0.03, 1, sunRadius + 74.8);
earth.mesh.receiveShadow = true;
var moon = new Planet(0.8, 10, 10, 8.0, 0, 0, ['textures/moon.jpg', null, null], 'Luna', 3.5, 0.028, 0, 8.0);
moon.mesh.receiveShadow = true; 
moon.mesh.castShadow = true;

var mars = new Planet(1.7, 24, 24, sunRadius + 114.0, 0, 0, ['textures/mars.jpg', 'textures/marsbump.jpg', null], 
                        'Marte', 141.05, 0.015, 1, sunRadius + 114.0);
// reduccion de la distancia al sol 1/4000000
var jupiter = new Planet(40.0, 64, 64, sunRadius + 194.62, 0, 0, ['textures/jupiter.jpg', null, null], 
                        'Júpiter', 260.6, 0.04, 5, sunRadius + 194.62);
var europa = new Planet(1.2, 10, 10, 48.0, 0, 0, ['textures/moon.jpg', null, null], 'Luna', 4.5, 0.028, 0, 48.0);

var saturno = new Planet(29.1, 48, 48, sunRadius + 358.5, 0, 0, ['textures/saturn.jpg', null, null],
                        'Saturno', 321.73, 0.012, 2, sunRadius + 358.5);
// 1/6000000
var urano = new Planet(12.6, 16, 16, sunRadius + 478.5, 0, 0, ['textures/uranus.jpg', null, null],
                        'Urano', 378.32, 0.004, 2, sunRadius + 478.5);
var neptuno = new Planet(12.3, 16, 16, sunRadius + 749.16, 0, 0, ['textures/neptune.jpg', null, null],
                        'Neptuno', 517.21, 0.002, 2, sunRadius + 749.16);

function getRing(size, innerDiameter, segments, myColor, name, x) {
    var ringGeometry = new THREE.RingGeometry(size, innerDiameter, segments);
    var ringMaterial = new THREE.MeshBasicMaterial({color: myColor, side: THREE.DoubleSide});
    var myRing = new THREE.Mesh(ringGeometry, ringMaterial);
    myRing.name = name;
    myRing.position.set(x, 0, 0);
    myRing.rotation.x = Math.PI / 2;
    scene.add(myRing);
    return myRing;
}
function createVisibleOrbits(distance, segments, name) {
    var orbitWidth = 0.05;
    planetOrbit = getRing(
        distance + orbitWidth, 
        distance - orbitWidth, 
        segments, 
        0xffffff, 
        name, 
        0);
}

function getTorus(size, innerDiameter, segments, myColor, distance) {
    var ringGeometry = new THREE.TorusGeometry(size, innerDiameter, segments, segments);
    var ringMaterial = new THREE.MeshPhongMaterial({color: myColor, side: THREE.DoubleSide});
    var myRing = new THREE.Mesh(ringGeometry, ringMaterial);
    myRing.position.set(distance, 0, 0);
    myRing.rotation.x = Math.PI / 2;
    scene.add(myRing);
    return myRing;
}


var camera = new THREE.PerspectiveCamera(
    75, // angulo
    window.innerWidth/window.innerHeight, // aspect, es lo que ve la camara
    0.1, // near
    1500 // far
);
camera.position.set(500, 500, 500);

const axis = new THREE.Vector3(0, 1, 0);


var scene = new THREE.Scene();

scene.add(sun);
scene.add(mercury.mesh);
scene.add(venus.mesh);
scene.add(earth.mesh);
scene.add(moon.mesh);
scene.add(mars.mesh);
scene.add(jupiter.mesh);
scene.add(europa.mesh);
scene.add(saturno.mesh);
scene.add(urano.mesh);
scene.add(neptuno.mesh);


createVisibleOrbits(earth.distance, 640, earth.name);
createVisibleOrbits(mercury.distance, 640, mercury.name);
createVisibleOrbits(venus.distance, 640, venus.name);
createVisibleOrbits(mars.distance, 640, mars.name);
createVisibleOrbits(jupiter.distance, 640, jupiter.name);
createVisibleOrbits(saturno.distance, 640, saturno.name);
createVisibleOrbits(urano.distance, 640, urano.name);
createVisibleOrbits(neptuno.distance, 640, neptuno.name);

var rings = [
    getTorus(44, 0.8, 48, 0xd9a55e, saturno.distance),
    getTorus(41, 0.8, 48, 0xd9a55e, saturno.distance),
    getTorus(38, 0.8, 48, 0xd9a55e, saturno.distance),
    getTorus(35, 0.8, 48, 0xd9a55e, saturno.distance)
];
var rings2 = [
    getTorus(32, 0.4, 48, 0x7a8a93, urano.distance),
    getTorus(30, 0.4, 48, 0x7a8a93, urano.distance),
    getTorus(28, 0.4, 48, 0x7a8a93, urano.distance),
    getTorus(26, 0.4, 48, 0x7a8a93, urano.distance)
];

const color = 0xFFFFFF;
const intensity = 1.0;
const light = new THREE.PointLight(color, intensity);
light.position.set(0, 0, 0);
scene.add(light);

const lightA = new THREE.AmbientLight(0x101010);
scene.add(lightA);

const helper = new THREE.PointLightHelper(light);
scene.add(helper);

function updateLight() {
    helper.update();
}
updateLight();

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

renderer.render( scene, camera );


{
    const loader = new THREE.TextureLoader();
    const texture = loader.load(
      'textures/universo_4k.jpg',
      () => {
        const rt = new THREE.WebGLCubeRenderTarget(texture.image.height);
        rt.fromEquirectangularTexture(renderer, texture);
        scene.background = rt.texture;
      });
  }

  function resizeRendererToDisplaySize(renderer) {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
      renderer.setSize(width, height, false);
    }
    return needResize;
  }
// para los controles del mouse
var controls = new THREE.OrbitControls( camera, renderer.domElement );
controls.minDistance = 3; // minima distancia a q puede hacer zoom
controls.maxDistance = 2000; // maxima distancia a q puede hacer zoom


var animate = function(){
    requestAnimationFrame(animate);            
    if (resizeRendererToDisplaySize(renderer)) {
        const canvas = renderer.domElement;
        camera.aspect = canvas.clientWidth / canvas.clientHeight;
        camera.updateProjectionMatrix();
      }

    sun.rotation.y += 0.0001;
    mercury.move();
    venus.move();
    earth.move();
    moon.moveMoon(earth.mesh.position);
    mars.move();
    jupiter.move();
    europa.moveMoon(jupiter.mesh.position);
    saturno.move();
    for (let ring of rings) {
        ring.position.set(saturno.mesh.position.x, 0, saturno.mesh.position.z)
    }
    
    urano.move();
    for (let ring of rings2) {
        ring.position.set(urano.mesh.position.x, 0, urano.mesh.position.z)
    }
    neptuno.move();

    renderer.render( scene, camera );
}

animate()
