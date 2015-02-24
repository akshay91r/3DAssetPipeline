import bpy  
for item in bpy.data.objects:  
      
    print(item.name)  
    if item.type == 'MESH':  
        for vertex in item.data.vertices:  
            print(vertex.co)
