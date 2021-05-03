class Sphere {
    constructor(radius, alpha, theta, textures) {
        this.r = radius;
        this.a = alpha;
        this.t = theta;
        this.geometry = new THREE.SphereGeometry(this.r, this.a, this.t);
        this.setTexture(textures);
        //this.material = new THREE.MeshPhongMaterial({color:0x00ff00, wireframe: true});
        this.mesh = new THREE.Mesh(this.geometry, this.material);
    }

    set position(position) {
        this.mesh.position.x = position[0];
        this.mesh.position.y = position[1];
        this.mesh.position.z = position[2];
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







const axis = new THREE.Vector3(80, 1, 3.18).normalize();
// sol
var sunGeometry = new THREE.SphereGeometry(69.6, 64, 64);
const texture_1 = new THREE.TextureLoader().load('textures/sun.jpg' );
const texture_2 = new THREE.TextureLoader().load('textures/sunspecular.jpg');
var sunMaterial = new THREE.MeshBasicMaterial({map: texture_1});
var sun = new THREE.Mesh(sunGeometry, sunMaterial);
sun.position = [0, 0, 0];



var earth = new Sphere(6.3, 32, 32, ['textures/earth.jpg', 'textures/earthbump.jpg', 'textures/earthspecular.jpg']);
earth.position = [80, 0, 0];
var sphereGeometry = new THREE.SphereGeometry(6.31, 32, 32);
const texture_4 = new THREE.TextureLoader().load('textures/earthcloudswb.jpg');
var material = new THREE.MeshPhongMaterial({map: texture_4, side: THREE.DoubleSide, transparent: true, opacity: 0.4, depthWrite: false});
var earthAtmosphere = new THREE.Mesh(sphereGeometry, material);
earthAtmosphere.position.set(0, 0, 0);
earth.mesh.add(earthAtmosphere);




var moon = new Sphere(0.1, 10, 10, ['textures/moon.jpg', null, null]);
moon.position = [81, 0, 0];
var mars = new Sphere(3.3, 24, 24, ['textures/mars.jpg', null, null]);
mars.position = [100, 0, 0];




var quaternion = new THREE.Quaternion();

var scene = new THREE.Scene();
const axesHelper = new THREE.AxesHelper( 15 );
scene.add( axesHelper );
scene.add(sun);
scene.add(earth.mesh);
scene.add(moon.mesh);
scene.add(mars.mesh);

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

const canvas = document.querySelector('#c');
const renderer = new THREE.WebGLRenderer({canvas});



var camera = new THREE.PerspectiveCamera(
    75, // angulo
    window.innerWidth/window.innerHeight, // aspect, es lo que ve la camara
    0.1, // near
    1000 // far
);
camera.useQuaternion = true;
camera.position.set(100, 100, 100);

const controls = new THREE.OrbitControls(camera, canvas);
controls.target.set(0, 0, 0);
controls.update();




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


function render(time) {
    time *= 0.001;

    if (resizeRendererToDisplaySize(renderer)) {
      const canvas = renderer.domElement;
      camera.aspect = canvas.clientWidth / canvas.clientHeight;
      camera.updateProjectionMatrix();
    }

    scene.traverse(function(object){
        if (object.isMesh == true){ // para evitar rotar la camara
            object.rotation.y += 0.001;
        }
    });

    quaternion.setFromAxisAngle(axis, 0.01);
    moon.mesh.position.applyQuaternion(quaternion);

    renderer.render(scene, camera);

    requestAnimationFrame(render);
  }


requestAnimationFrame(render);
