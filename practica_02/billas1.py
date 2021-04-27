import vtk
import numpy as np
import math

class MySphere:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
        self.velocity = [0, 10, 0]
        self.last_velocity = [0, -10, 0]
        self.actor = None

        self.source1 = vtk.vtkSphereSource()
        
        self.sphere_mapper = vtk.vtkPolyDataMapper()
        self.sphere_actor = vtk.vtkActor()
        

    def createSphere(self):
        self.source1.SetThetaResolution(50)
        self.source1.SetRadius(self.radius)
        self.source1.Update()

    def createMapper(self):
        self.sphere_mapper.SetInputData(self.source1.GetOutput())

    def createActor(self):
        reader = vtk.vtkJPEGReader()
        reader.SetFileName("padoru.jpg")


        texture = vtk.vtkTexture()
        # Create texture object
        texture.SetInputConnection(reader.GetOutputPort())


        map_to_sphere = vtk.vtkTextureMapToSphere()
        map_to_sphere.SetInputConnection(self.source1.GetOutputPort())

        sphere_mapper = vtk.vtkPolyDataMapper()
        sphere_mapper.SetInputConnection(map_to_sphere.GetOutputPort())


        self.sphere_actor.SetMapper(sphere_mapper)
        self.sphere_actor.SetTexture(texture)
        #self.sphere_actor.GetProperty().SetColor(1, 0, 0.0)
        self.sphere_actor.SetPosition(self.pos[0], self.pos[1], self.pos[2])
    def getActor(self):
        return self.sphere_actor


class MyFloor:
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        self.velocity = np.array([0, 0, 0])
        self.actor = None

        self.source2 = vtk.vtkCubeSource()
        self.floor_mapper = vtk.vtkPolyDataMapper()
        self.floor_actor = vtk.vtkActor()

    def createFloor(self):

        self.source2.SetXLength(40)
        self.source2.SetYLength(self.height)
        self.source2.SetZLength(40)
        self.source2.Update()

    def createMapper(self):
        
        self.floor_mapper.SetInputData(self.source2.GetOutput())

    def createActor(self):
        
        reader = vtk.vtkJPEGReader()
        reader.SetFileName("ice.jpg")

        # Create texture object
        texture = vtk.vtkTexture()
        texture.SetInputConnection(reader.GetOutputPort())

        #Map texture coordinates
        map_to_plane = vtk.vtkTextureMapToPlane()
        map_to_plane.SetInputConnection(self.source2.GetOutputPort())
        self.floor_actor.SetMapper(self.floor_mapper)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(map_to_plane.GetOutputPort())
        #self.floor_actor.GetProperty().SetColor(0, 1, 0.0)
        self.floor_actor.SetMapper(mapper)
        self.floor_actor.SetTexture(texture)
        self.floor_actor.GetProperty().SetOpacity(0.8)
        self.floor_actor.SetPosition(self.pos[0], self.pos[1], self.pos[2])

    def getActor(self):
        return self.floor_actor

class MyPared:
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        self.velocity = np.array([0, 0, 0])
        self.actor = None


class Paredes:
    def __init__(self, MyPared1,MyPared2,MyPared3,MyPared4):
        self.MyPared1 = MyPared1
        self.MyPared2 = MyPared2
        self.MyPared3 = MyPared3
        self.MyPared4 = MyPared4

        self.source3 = vtk.vtkCubeSource()
        self.source4 = vtk.vtkCubeSource()
        self.source5 = vtk.vtkCubeSource()
        self.source6 = vtk.vtkCubeSource()

        self.pared_mapper = vtk.vtkPolyDataMapper()
        self.pared2_mapper = vtk.vtkPolyDataMapper()
        self.pared3_mapper = vtk.vtkPolyDataMapper()
        self.pared4_mapper = vtk.vtkPolyDataMapper()

        self.pared_actor = vtk.vtkActor()
        self.pared2_actor = vtk.vtkActor()
        self.pared3_actor = vtk.vtkActor()
        self.pared4_actor = vtk.vtkActor()


    def createCubes(self):

        self.source3.SetXLength(40)
        self.source3.SetYLength(self.MyPared1.height)
        self.source3.SetZLength(1)
        self.source3.Update()

        self.source4.SetXLength(40)
        self.source4.SetYLength(self.MyPared2.height)
        self.source4.SetZLength(1)
        self.source4.Update()

        self.source5.SetXLength(1)
        self.source5.SetYLength(self.MyPared3.height)
        self.source5.SetZLength(41)
        self.source5.Update()

        self.source6.SetXLength(1)
        self.source6.SetYLength(self.MyPared4.height)
        self.source6.SetZLength(41)
        self.source6.Update()


    def createMapper(self):
        self.pared_mapper.SetInputData(self.source3.GetOutput())
        self.pared2_mapper.SetInputData(self.source4.GetOutput())
        self.pared3_mapper.SetInputData(self.source5.GetOutput())
        self.pared4_mapper.SetInputData(self.source6.GetOutput())

    def createActor(self):

        self.pared_actor.SetMapper(self.pared_mapper)
        self.pared_actor.GetProperty().SetColor(0, 0, 1.0)
        self.pared2_actor.SetMapper(self.pared2_mapper)
        self.pared2_actor.GetProperty().SetColor(0, 0, 1.0)
        self.pared3_actor.SetMapper(self.pared3_mapper)
        self.pared3_actor.GetProperty().SetColor(0, 0, 1.0)
        self.pared4_actor.SetMapper(self.pared4_mapper)
        self.pared4_actor.GetProperty().SetColor(0, 0, 1.0)

        self.pared_actor.SetPosition(self.MyPared1.pos[0], self.MyPared1.pos[1], self.MyPared1.pos[2])
        self.pared2_actor.SetPosition(self.MyPared2.pos[0], self.MyPared2.pos[1], self.MyPared2.pos[2])
        self.pared3_actor.SetPosition(self.MyPared3.pos[0], self.MyPared3.pos[1], self.MyPared3.pos[2])
        self.pared4_actor.SetPosition(self.MyPared4.pos[0], self.MyPared4.pos[1], self.MyPared4.pos[2])

    def getActor(self):
        paredesActores = []
        paredesActores.append(self.pared_actor)
        paredesActores.append(self.pared2_actor)
        paredesActores.append(self.pared3_actor)
        paredesActores.append(self.pared4_actor)
        return paredesActores


def addActores(renderer,Actores):
    for i in Actores:
        renderer.AddActor(i)

vx=0.5
vz=1
sphere = MySphere([0,2, 0], 2)
floor = MyFloor([0, 0, 0], 1)
pared = MyPared([0,1,20], 3)
pared2 = MyPared([0,1,-20], 3)
pared3 = MyPared([20,1,0], 3)
pared4 = MyPared([-20,1,0], 3)

paredes = Paredes(pared,pared2,pared3,pared4)



largo = 40
ancho = 40
time = 0
g = 9
height = abs(floor.pos[1] - sphere.pos[1])

rotacion = 20
direccion = 0

def callback_func(caller, timer_event):
    global vx,vz,ax,az,rotacion,direccion
    sphere.pos[0] += vx
    sphere.pos[2] += vz
    vx -= vx*0.004
    vz -= vz*0.004
    rotacion -= rotacion *0.004

    sphere.sphere_actor.SetPosition(sphere.pos)
    if (direccion==0):
        sphere.sphere_actor.RotateX(rotacion)
    if (direccion==1):
        sphere.sphere_actor.RotateZ(rotacion)
    render_window.Render()
    x,y,z=sphere.sphere_actor.GetPosition()
    if(x<-largo/2 + 3 or x>largo/2 - 3):
        vx*=-1
        rotacion *= -1
        direccion = 0
    if(z<-ancho/2 +  3 or z>ancho/2 - 3):
        rotacion *= -1
        direccion = 1
        vz*=-1

# source

sphere.createSphere()
floor.createFloor()
paredes.createCubes()


# mapper

#sphere.createMapper()
#floor.createMapper()
paredes.createMapper()




# actor
paredes.createActor()
floor.createActor()
sphere.createActor()




# camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0,0,0)
camera.SetPosition(50,50,50)

# renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)




renderer.AddActor(sphere.getActor())
renderer.AddActor(floor.getActor())
addActores(renderer,paredes.getActor())
renderer.SetActiveCamera(camera)

# renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

# interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
#set_initial_position()
interactor.CreateRepeatingTimer(1)
interactor.AddObserver("TimerEvent", callback_func)
interactor.Start()