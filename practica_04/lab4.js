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
        //this.material = new THREE.MeshPhongMaterial({color:0x00ff00, wireframe: true});
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
            this.material = new THREE.MeshPhongMaterial({color:0x00ff00, wireframe: true});
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
        this.x = Math.cos(time * (1.0 / (this.orbitRate * orbitData.value)) + 10.0) * this.distance;
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

var globalRate = 1.0;

function setPlanetData(myOrbitRate, myRotationRate, myXDistance, myName, myTexture, myRadius, mySegments) {
    return {
        orbitRate: myOrbitRate,
        rotationRate: myRotationRate,
        distance: myXDistance,
        name: myName,
        texture: myTexture,
        size: myRadius,
        segments: mySegments
    };
}

var earthData = setPlanetData(365.2564, 0.015, 85, "earth", "textures/earth.jpg", 1, 32);
var moonData = setPlanetData(29.5, 0.01, 2.8, "moon", "textures/moon.jpg", 0.5, 32);
var orbitData = {value: 200, runOrbit: true, runRotation: true};


function movePlanet(myPlanet, myData, myTime, stopRotation) {
    if (orbitData.runRotation && !stopRotation) {
        myPlanet.rotation.y += myData.rotationRate;
    }
    if (orbitData.runOrbit) {
        myPlanet.position.x = Math.cos(myTime 
                * (1.0 / (myData.orbitRate * orbitData.value)) + 10.0) 
                * myData.distanceFromAxis;
        myPlanet.position.z = Math.sin(myTime 
                * (1.0 / (myData.orbitRate * orbitData.value)) + 10.0) 
                * myData.distanceFromAxis;
    }
}
function moveMoon(moon, planetPosition) {
    moon.move();
    if (orbitData.runOrbit) {
        moon.mesh.position.x = moon.mesh.position.x + planetPosition.x;
        moon.mesh.position.z = moon.mesh.position.z + planetPosition.z;
    }
}

// sol
const sunRadius = 348.0; // reducido 1/2000
var sunGeometry = new THREE.SphereGeometry(sunRadius, 64, 64);
const texture_1 = new THREE.TextureLoader().load('textures/sun.jpg');
//const texture_2 = new THREE.TextureLoader().load('textures/sunspecular.jpg');
var sunMaterial = new THREE.MeshBasicMaterial({map: texture_1});
var sun = new THREE.Mesh(sunGeometry, sunMaterial);
sun.position.set(0, 0, 0);

// reduccion de la distancia 1/1000000
// reduccion del radio 1/1000
var mercury = new Planet(2.4, 12, 12, sunRadius + 57.90, 0, 0, ['textures/mercury.jpg', 'textures/mercurybump.jpg', null], 
                        'Mercurio', 365.2564, 0.015, 0, sunRadius + 57.90);
var venus = new Planet(6.0, 32, 32, sunRadius + 108.2, 0, 0, ['textures/venus.jpg', 'textures/venusbump.jpg', null], 
                        'Venus', 365.2564, 0.015, 0, sunRadius + 108.2);
var earth = new Planet(6.3, 32, 32, sunRadius+149.6, 0, 0, ['textures/earth.jpg', 'textures/earthbump.jpg','textures/earthspecular.jpg'],                       'Tierra', 365.2564, 0.015, 1, sunRadius + 149.6);
var moon = new Planet(1.7, 10, 10, 10.0, 0, 0, ['textures/moon.jpg', null, null], 'Luna', 29.5, 0.01, 0, 10.0);

var mars = new Planet(3.3, 24, 24, sunRadius + 227.9, 0, 0, ['textures/mars.jpg', 'textures/marsbump.jpg', null], 
                        'Marte', 365.2564, 0.015, 1, sunRadius + 227.9);
// reduccion de la distancia al sol 1/2000000
var jupiter = new Planet(69.9, 64, 64, sunRadius + 389.2, 0, 0, ['textures/jupiter.jpg', null, null], 
                        'Júpiter', 365.2564, 0.015, 5, sunRadius + 389.2);



var camera = new THREE.PerspectiveCamera(
    75, // angulo
    window.innerWidth/window.innerHeight, // aspect, es lo que ve la camara
    0.1, // near
    1000 // far
);
camera.useQuaternion = true;
camera.position.set(500, 500, 500);

var quaternion = new THREE.Quaternion();
const axis = new THREE.Vector3(0, 1, 0);


const lightA = new THREE.AmbientLight(0x101010);

var scene = new THREE.Scene();
const axesHelper = new THREE.AxesHelper( 15 );
scene.add( axesHelper );
scene.add(lightA);
scene.add(sun);
scene.add(mercury.mesh);
scene.add(venus.mesh);
scene.add(earth.mesh);
scene.add(moon.mesh);
scene.add(mars.mesh);
scene.add(jupiter.mesh)

const color = 0xFFFFFF;
const intensity = 1.0;
const light = new THREE.PointLight(color, intensity);
light.position.set(0, 0, 0);
scene.add(light);


const helper = new THREE.PointLightHelper(light);
scene.add(helper);

function updateLight() {
    helper.update();
}
updateLight();

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

//renderer.render( scene, camera );
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
controls.maxDistance = 1000; // maxima distancia a q puede hacer zoom


var animate = function(){
    requestAnimationFrame(animate);            
    if (resizeRendererToDisplaySize(renderer)) {
        const canvas = renderer.domElement;
        camera.aspect = canvas.clientWidth / canvas.clientHeight;
        camera.updateProjectionMatrix();
      }
    // para recorrer cada objeto de la scena (tambien incluye la camara)
    sun.rotation.y += 0.001;
    mercury.move();
    venus.move();
    earth.move();
    moon.moveMoon(earth.mesh.position);
    mars.move();
    jupiter.move();

    //circle.rotation 
    renderer.render( scene, camera );
}

animate()
