import vtk

def transformRGBRange(rgb):
    return rgb[0]/255 , rgb[1]/255 , rgb[2]/255

def cube(size_x, size_y, size_z):
    cube_shape = vtk.vtkCubeSource()
    cube_shape.SetXLength(size_x)
    cube_shape.SetYLength(size_y)
    cube_shape.SetZLength(size_z)
    cube_shape.Update()
    mapp_object = vtk.vtkPolyDataMapper()
    mapp_object.SetInputData(cube_shape.GetOutput())
    return mapp_object

def cone(radius,height,resolution):
    cone_shape = vtk.vtkConeSource()
    cone_shape.SetRadius(radius)
    cone_shape.SetHeight(height)
    cone_shape.SetResolution(resolution)
    cone_shape.Update()
    mapp_object = vtk.vtkPolyDataMapper()
    mapp_object.SetInputData(cone_shape.GetOutput())
    return mapp_object

def sphere(radius):
    sphere_shape = vtk.vtkSphereSource()
    sphere_shape.SetRadius(radius)
    sphere_shape.Update()
    mapp_object = vtk.vtkPolyDataMapper()
    mapp_object.SetInputData(sphere_shape.GetOutput())
    return mapp_object

def cylinder(radius,height,resolution):
    cylinder_shape = vtk.vtkCylinderSource()
    cylinder_shape.SetRadius(radius)
    cylinder_shape.SetHeight(height)
    cylinder_shape.SetResolution(resolution)
    cylinder_shape.Update()
    mapp_object = vtk.vtkPolyDataMapper()
    mapp_object.SetInputData(cylinder_shape.GetOutput())
    return mapp_object

def actor(mapper,xyz,angle,rgb,texture_name):
    actor = vtk.vtkActor()
    if texture_name is not None:
        reader = vtk.vtkJPEGReader()
        reader.SetFileName(texture_name)

        texture = vtk.vtkTexture()
        if vtk.VTK_MAJOR_VERSION <= 5:
            texture.SetInput(reader.GetOutput())
        else:
            texture.SetInputConnection(reader.GetOutputPort())
        actor.SetTexture(texture)
    if rgb is not None:
        actor.GetProperty().SetColor(transformRGBRange(rgb))
    if angle[0] is not None:
        actor.RotateX(angle[0])
    if angle[1] is not None:
        actor.RotateY(angle[1])
    if angle[2] is not None:
        actor.RotateZ(angle[2])
    actor.SetMapper(mapper)
    actor.SetPosition(xyz)
    return actor