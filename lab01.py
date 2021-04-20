from helpers import *

#----------------MAPPERS---------------------->
# molino
techo = cone(6,20,80)
body = cone(6, 16, 80)
aspa = cube(1.5,17,.1)
estaca = cube(.5,.5,5.7)


body_duck       = cube(.7,.8,1.2)
ala_duck        = cube(.15,.5, .7)
cuello_duck     = cube(.5,.7, .5)
eye_duck        = cube(.12, .12, .05)
pico_duck       = cube(.4, .1, .4)
cresta_duck     = cube(.2, .2, .2)
pata1_duck      = cube(.15, .5, .15)
pata2_duck      = cube(.3, .1, .3)

body_hourse     = cube(1.5, 1.5, 4)
legs_hourse     = cube(.5, 1.2, .5)
cascos_hourse   = cube(.52, .3, .52)
cuello_hourse   = cube(.85, 2, .85)
head_hourse     = cube(1, .8 , 1.5)
eye_hourse      = cube(.2, .25, .05)
oreja_hourse    = cube(.2 , .5 ,.2)
cola_hourse     = cube(.2, .2 , 1.5)
melena_hourse   = cube(.2, 1.9 , .5)

grass = cube(80,.1,80)


#--------------ACTORS(mapper/[position]/[angle]/[color]/texture_name)------------------------>
act_techo  = actor(techo, [20,14,20], [None,None,90], [219, 172, 121], None)
act_body   = actor(body, [20,8,20], [None,None,90], [209, 204, 190], None)
act_aspa1   = actor(aspa, [20,16,26], [None,None,None], [163, 130, 93],None)
act_aspa2   = actor(aspa, [20,16,26], [None,None,90], [163, 130, 93],None)
act_estaca   = actor(estaca, [20,16,23], [None,None,90], [163, 130, 93],None)

pos_x=-20
act_body_duck       = actor(body_duck, [pos_x+ 0,1,0], [None,None,None], [212, 202, 184], None)
act_ala_der_duck    = actor(ala_duck, [pos_x+ -0.45, 1.1, 0], [None,None,None], [224, 221, 215], None)
act_ala_izq_duck    = actor(ala_duck, [pos_x+ 0.45, 1.1, 0], [None,None,None], [224, 221, 215], None)
act_cuello_duck     = actor(cuello_duck, [pos_x+ 0,1.6,.7], [None,None,None], [224, 221, 215], None)
act_eye1_duck       = actor(eye_duck, [pos_x+ -0.15, 1.75, .95], [None,None,None], [0, 0, 0], None)
act_eye2_duck       = actor(eye_duck, [pos_x+ 0.15, 1.75, .95], [None,None,None], [0, 0, 0], None)
act_pico1_duck      = actor(pico_duck, [pos_x+ 0, 1.62, 1], [None,None,None], [207, 189, 87], None)
act_pico2_duck      = actor(pico_duck, [pos_x+ 0, 1.52, 1], [None,None,None], [181, 166, 78], None)
act_cresta_duck     = actor(cresta_duck, [pos_x+ 0, 1.4, 1], [None,None,None], [191, 57, 57], None)
act_pata1_duck      = actor(pata1_duck, [pos_x+ -0.2, .4, 0], [None,None,None], [207, 189, 87], None)
act_pata2_duck      = actor(pata2_duck, [pos_x+ -0.2, .1, .1], [None,None,None], [207, 189, 87], None)
act_pata3_duck      = actor(pata1_duck, [pos_x+ 0.2, .4, 0], [None,None,None], [207, 189, 87], None)
act_pata4_duck      = actor(pata2_duck, [pos_x+ 0.2, .1, .1], [None,None,None], [207, 189, 87], None)

pos_x3=-18
act_body_duck2      = actor(body_duck, [pos_x3+ 0,1,0], [None,None,None], [212, 202, 184], None)
act_ala_der_duck2    = actor(ala_duck, [pos_x3+ -0.45, 1.1, 0], [None,None,None], [224, 221, 215], None)
act_ala_izq_duck2    = actor(ala_duck, [pos_x3+ 0.45, 1.1, 0], [None,None,None], [224, 221, 215], None)
act_cuello_duck2     = actor(cuello_duck, [pos_x3+ 0,1.6,.7], [None,None,None], [224, 221, 215], None)
act_eye1_duck2       = actor(eye_duck, [pos_x3+ -0.15, 1.75, .95], [None,None,None], [0, 0, 0], None)
act_eye2_duck2       = actor(eye_duck, [pos_x3+ 0.15, 1.75, .95], [None,None,None], [0, 0, 0], None)
act_pico1_duck2      = actor(pico_duck, [pos_x3+ 0, 1.62, 1], [None,None,None], [207, 189, 87], None)
act_pico2_duck2      = actor(pico_duck, [pos_x3+ 0, 1.52, 1], [None,None,None], [181, 166, 78], None)
act_cresta_duck2     = actor(cresta_duck, [pos_x3+ 0, 1.4, 1], [None,None,None], [191, 57, 57], None)
act_pata1_duck2      = actor(pata1_duck, [pos_x3+ -0.2, .4, 0], [None,None,None], [207, 189, 87], None)
act_pata2_duck2      = actor(pata2_duck, [pos_x3+ -0.2, .1, .1], [None,None,None], [207, 189, 87], None)
act_pata3_duck2      = actor(pata1_duck, [pos_x3+ 0.2, .4, 0], [None,None,None], [207, 189, 87], None)
act_pata4_duck2     = actor(pata2_duck, [pos_x3+ 0.2, .1, .1], [None,None,None], [207, 189, 87], None)

pos_x2=-15
act_body_hourse     = actor(body_hourse, [pos_x2+ 2,2,0], [None,None,None], [112, 54, 7],None)
act_legs1_hourse    = actor(legs_hourse, [pos_x2+ 1.5,.65,1.5], [None,None,None], [79, 39, 6], None)
act_legs2_hourse    = actor(legs_hourse, [pos_x2+ 2.5,.65,1.5], [None,None,None], [79, 39, 6], None)
act_legs3_hourse    = actor(legs_hourse, [pos_x2+ 1.5,.65,-1.5], [None,None,None], [79, 39, 6], None)
act_legs4_hourse    = actor(legs_hourse, [pos_x2+ 2.5,.65,-1.5], [None,None,None], [79, 39, 6], None)
act_casco1_hourse   = actor(cascos_hourse, [pos_x2+ 1.5, .2, 1.5], [None,None,None], [0, 0, 0], None)
act_casco2_hourse   = actor(cascos_hourse, [pos_x2+ 2.5, .2, 1.5], [None,None,None], [0, 0, 0], None)
act_casco3_hourse   = actor(cascos_hourse, [pos_x2+ 1.5, .2, -1.5], [None,None,None], [0, 0, 0], None)
act_casco4_hourse   = actor(cascos_hourse, [pos_x2+ 2.5, .2, -1.5], [None,None,None], [0, 0, 0], None)
act_cuello_hourse   = actor(cuello_hourse, [pos_x2+ 2, 3, 2], [20,None,None], [112, 54, 7], None)
act_head_hourse     = actor(head_hourse, [pos_x2+ 2, 3.5, 2.5], [20,None,None], [112, 54, 7], None)
act_eye1_hourse     = actor(eye_hourse, [pos_x2+ 2.5, 3.5, 2.5], [20,90,None], [0, 0, 0], None)
act_eye2_hourse     = actor(eye_hourse, [pos_x2+ 1.5, 3.5, 2.5], [20,90,None], [0, 0, 0], None)
act_oreja1_hourse   = actor(oreja_hourse, [pos_x2+ 2.2, 4.2, 2.3], [20,None,None], [112, 54, 7], None)
act_oreja2_hourse   = actor(oreja_hourse, [pos_x2+ 1.8, 4.2, 2.3], [20,None,None], [112, 54, 7], None)
act_cola_hourse   = actor(cola_hourse, [pos_x2+ 2, 2.3, -2.5], [-20,None,None], [112, 54, 7], None)
act_melena_hourse   = actor(melena_hourse, [pos_x2+ 2, 3.5, 1.6], [20,None,None], [205, 217, 102], None)


act_grass = actor(grass, [0,0,0], [None,None,None], None, "grass.jpg")


#------------------------------Config--------------------------------------->
#axes
transform = vtk.vtkTransform()
transform.Translate(5.0, 0.0, 0.0) 
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transform)

#camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0,0,0)
camera.SetPosition(5,5,50)

#light
light1 = vtk.vtkLight()
light1.SetIntensity(1)
light1.SetPosition(0, 25, 50)

light2 = vtk.vtkLight()
light2.SetIntensity(.5)
light2.SetPosition(0, 25, -50)

light3 = vtk.vtkLight()
light3.SetIntensity(.5)
light3.SetPosition(50, 25, 0)

light4 = vtk.vtkLight()
light4.SetIntensity(.5)
light4.SetPosition(-50, 25, 0)

# renderer ---------------------> AddActor
renderer = vtk.vtkRenderer()
renderer.SetBackground(transformRGBRange([186, 155, 93]))
#molino
renderer.AddActor(act_techo)
renderer.AddActor(act_body)
renderer.AddActor(act_grass)
renderer.AddActor(act_aspa1)
renderer.AddActor(act_aspa2)
renderer.AddActor(act_estaca)

#pato
renderer.AddActor(act_body_duck)
renderer.AddActor(act_ala_der_duck)
renderer.AddActor(act_ala_izq_duck)
renderer.AddActor(act_cuello_duck)
renderer.AddActor(act_eye1_duck)
renderer.AddActor(act_eye2_duck)
renderer.AddActor(act_pico1_duck)
renderer.AddActor(act_pico2_duck)
renderer.AddActor(act_cresta_duck)
renderer.AddActor(act_pata1_duck)
renderer.AddActor(act_pata2_duck)
renderer.AddActor(act_pata3_duck)
renderer.AddActor(act_pata4_duck)

renderer.AddActor(act_body_duck2)
renderer.AddActor(act_ala_der_duck2)
renderer.AddActor(act_ala_izq_duck2)
renderer.AddActor(act_cuello_duck2)
renderer.AddActor(act_eye1_duck2)
renderer.AddActor(act_eye2_duck2)
renderer.AddActor(act_pico1_duck2)
renderer.AddActor(act_pico2_duck2)
renderer.AddActor(act_cresta_duck2)
renderer.AddActor(act_pata1_duck2)
renderer.AddActor(act_pata2_duck2)
renderer.AddActor(act_pata3_duck2)
renderer.AddActor(act_pata4_duck2)

#caballo
renderer.AddActor(act_body_hourse)
renderer.AddActor(act_legs1_hourse)
renderer.AddActor(act_legs2_hourse)
renderer.AddActor(act_legs3_hourse)
renderer.AddActor(act_legs4_hourse)
renderer.AddActor(act_casco1_hourse)
renderer.AddActor(act_casco2_hourse)
renderer.AddActor(act_casco3_hourse)
renderer.AddActor(act_casco4_hourse)
renderer.AddActor(act_cuello_hourse)
renderer.AddActor(act_head_hourse)
renderer.AddActor(act_eye1_hourse)
renderer.AddActor(act_eye2_hourse)
renderer.AddActor(act_oreja1_hourse)
renderer.AddActor(act_oreja2_hourse)
renderer.AddActor(act_cola_hourse)
renderer.AddActor(act_melena_hourse)

renderer.AddActor(act_grass)

renderer.AddActor(axes)
renderer.SetActiveCamera(camera)
renderer.AddLight(light1)
renderer.AddLight(light2)
renderer.AddLight(light3)
renderer.AddLight(light4)



#renderWindow ---------------------------------------------------->
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()