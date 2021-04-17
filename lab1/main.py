import vtk

def main() :
    transform = vtk.vtkTransform()
    transform.Translate(0.0, 0.0, 0.0)
    axes = vtk.vtkAxesActor()
    axes.SetUserTransform(transform)

    axes.SetShaftTypeToLine()
    axes.SetTotalLength(13.0, 13.0, 13.0)
    axes.SetNormalizedShaftLength(1.0, 1.0, 1.0)
    axes.SetNormalizedTipLength(0.05, 0.05, 0.05)

    xAxisLabel = axes.GetXAxisCaptionActor2D()
    xAxisLabel.GetCaptionTextProperty().SetFontSize(6)

    colors = vtk.vtkNamedColors()

    plane = vtk.vtkPlaneSource()
    plane.SetCenter(10.0, -5.0, 10.0)
    plane.SetNormal(0, 1.0, 0)
    plane.SetPoint1(10.0, -5.0, -10.0)
    plane.SetPoint2(-15.0, -5.0, 10.0)
    plane.SetXResolution(10)
    plane.SetYResolution(10)
    plane.Update()

    cube = vtk.vtkCubeSource()
    cube.SetXLength(10)
    cube.SetYLength(10)
    cube.SetZLength(10)
    cube.Update()

    door = vtk.vtkCubeSource()
    door.SetXLength(1.0)
    door.SetYLength(6.0)
    door.SetZLength(3.0)
    door.Update()

    window = vtk.vtkCubeSource()
    window.SetXLength(4.0)
    window.SetYLength(3.0)
    window.SetZLength(0.8)
    window.Update()

    cone = vtk.vtkConeSource()
    cone.SetResolution(30)
    cone.SetCenter(0, 0, 0)
    cone.SetRadius(5.0)
    cone.SetHeight(10.0)
    cone.Update()

    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(0, 0, 0)
    sphere.SetRadius(0.5)
    sphere.SetPhiResolution(100)
    sphere.SetThetaResolution(100)
    sphere.Update()

    cylinder = vtk.vtkCylinderSource()
    cylinder.SetRadius(0.2)
    cylinder.SetHeight(0.6)
    cylinder.SetResolution(10)
    cylinder.Update()

    plane_mapper = vtk.vtkPolyDataMapper()
    cube_mapper = vtk.vtkPolyDataMapper()
    cylinder_mapper = vtk.vtkPolyDataMapper()
    door_mapper = vtk.vtkPolyDataMapper()
    cone_mapper = vtk.vtkPolyDataMapper()
    sphere_mapper = vtk.vtkPolyDataMapper()
    window_mapper = vtk.vtkPolyDataMapper()

    if vtk.VTK_MAJOR_VERSION <= 5 :
        cube_mapper.SetInput(cube.GetOutput())
        cylinder_mapper.SetInput(cylinder.GetOutput())
        door_mapper.SetInput(door.GetOutput())
        cone_mapper.SetInput(cone.GetOutput())
        sphere_mapper.SetInput(sphere.GetOutput())
    else :
        cube_mapper.SetInputData(cube.GetOutput())
        cylinder_mapper.SetInputData(cylinder.GetOutput())
        door_mapper.SetInputData(door.GetOutput())
        cone_mapper.SetInputData(cone.GetOutput())
        sphere_mapper.SetInputData(sphere.GetOutput())
        plane_mapper.SetInputData(plane.GetOutput())
        window_mapper.SetInputData(window.GetOutput())

    plane_actor = vtk.vtkActor()
    plane_actor.SetMapper(plane_mapper)
    plane_actor.GetProperty().SetColor(colors.GetColor3d('green'))

    cube_actor = vtk.vtkActor()
    cube_actor.SetMapper(cube_mapper)
    cube_actor.GetProperty().SetColor(1.0, 1.0, 0.0)

    window_actor = vtk.vtkActor()
    window_actor.SetMapper(window_mapper)
    window_actor.SetPosition(0, 0, 5.0)
    window_actor.GetProperty().SetColor(colors.GetColor3d('silver'))

    cylinder_actor = vtk.vtkActor()
    cylinder_actor.SetMapper(cylinder_mapper)
    cylinder_actor.GetProperty().SetColor(0.0, 1.0, 0.0)
    cylinder_actor.SetPosition(1.0, 0.0, 0.0)
    cylinder_actor.RotateX(120.0)

    door_actor = vtk.vtkActor()
    door_actor.SetMapper(door_mapper)
    door_actor.SetPosition(5.0, -2.0, 0.0)
    door_actor.GetProperty().SetColor(colors.GetColor3d('Silver'))

    cone_actor = vtk.vtkActor()
    cone_actor.SetMapper(cone_mapper)
    cone_actor.SetPosition(0.0, 10.0, 0.0)
    cone_actor.RotateZ(90.0)
    cone_actor.GetProperty().SetDiffuseColor(colors.GetColor3d('bisque'))

    sphere_actor = vtk.vtkActor()
    sphere_actor.SetMapper(sphere_mapper)
    sphere_actor.SetPosition(5.5, -2.0, 1.0)
    sphere_actor.GetProperty().SetColor(colors.GetColor3d('blue'))

    camera = vtk.vtkCamera()
    camera.SetFocalPoint(0, 0, 0)
    camera.SetPosition(50, 50, 50)

    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.0, 0.0, 0.0)
    renderer.AddActor(axes)
    renderer.AddActor(plane_actor)
    renderer.AddActor(cube_actor)
    renderer.AddActor(door_actor)
    renderer.AddActor(window_actor)
    renderer.AddActor(cone_actor)
    renderer.AddActor(sphere_actor)
    renderer.AddActor(cylinder_actor)
    renderer.SetActiveCamera(camera)

    render_window = vtk.vtkRenderWindow()
    render_window.SetWindowName("Simple VTK scene")
    render_window.SetSize(600, 600)
    render_window.AddRenderer(renderer)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    interactor.Initialize()
    render_window.Render()
    interactor.Start()

if __name__ == '__main__' :
    main()
