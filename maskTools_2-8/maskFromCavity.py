import bpy
import bmesh



class MaskFromCavity(bpy.types.Operator) :
    ''' Mask From Cavity'''
    bl_idname = "mesh.mask_from_cavity"
    bl_label = "Mask From Cavity"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod

    def poll(cls, context):

        return context.active_object is not None and context.active_object.mode == 'SCULPT'


    # A Property for cavity angle
    bpy.types.Scene.mask_cavity_angle = bpy.props.IntProperty(name = "Cavity Angle", default = 82, min = 45, max = 90)

    # A Property for cavity mask strength
    bpy.types.Scene.mask_cavity_strength = bpy.props.FloatProperty(name = "Mask Strength", default = 1.0, min = 0.1, max = 1.0)



    def execute(self, context):

        mask_cavity_angle = context.scene.mask_cavity_angle # update property from user input

        mask_cavity_strength = context.scene.mask_cavity_strength # update property from user input

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT' :

           if context.sculpt_object.use_dynamic_topology_sculpting :

              dynatopoEnabled = True

              bpy.ops.sculpt.dynamic_topology_toggle()

           bmeshContainer = bmesh.new() # New bmesh container

           bmeshContainer.from_mesh(context.active_object.data) # Fill container with our object

           mask = bmeshContainer.verts.layers.paint_mask.verify() # get active mask layer

           bmeshContainer.faces.ensure_lookup_table() # Update vertex lookup table

           mask_cavity_angle *= (3.14 * 0.0055556) # Convert angle to radians (approx)

           maskWeight = 1.0 * mask_cavity_strength

           for face in bmeshContainer.faces :

                 for vert in face.verts : # for each x face

                    vert [mask] = 0.0 # Clear any mask beforehand

                    for loop in vert.link_loops :

                        loopTan =  loop.calc_tangent()

                        angleFace = (face.normal.angle (loopTan, 0.0))

                        angleDiff = (vert.normal.angle( loopTan, 0.0 )) # get the angle between the vert normal to loop edge Tangent

#                        print ("Angle Diff: %f" % (angleDiff))
#                        print ("Cav Angle : %f" % (mask_cavity_angle))
#                        print ("Angle Face : %f" % (angleFace))
#                        print ("AD - AF : %f" % (angleDiff + angleFace))
#                        print ("Loop Tangent : [%s] " % loopTan)

                        if ( angleFace + angleDiff ) <=  (1.57 + mask_cavity_angle) : # if the difference is greater then input

                               vert [mask] = maskWeight # mask it with input weight



           bmeshContainer.to_mesh(context.active_object.data) # Fill obj data with bmesh data

           bmeshContainer.free() # Release bmesh

           if dynatopoEnabled :

               bpy.ops.sculpt.dynamic_topology_toggle()



        return {'FINISHED'}






class MaskFromEdges(bpy.types.Operator):
    ''' Mask From Edges'''
    bl_idname = "mesh.mask_from_edges"
    bl_label = "Mask From Edges"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod

    def poll(cls, context):

        return context.active_object is not None and context.active_object.mode == 'SCULPT'


    # A Property for cavity angle
    bpy.types.Scene.mask_edge_angle = bpy.props.IntProperty(name = "Sharp Angle", default = 82, min = 45, max = 90)

    # A Property for cavity mask strength
    bpy.types.Scene.mask_edge_strength = bpy.props.FloatProperty(name = "Mask Strength", default = 1.0, min = 0.1, max = 1.0)



    def execute(self, context):

        mask_edge_angle = context.scene.mask_edge_angle # update property from user input

        mask_edge_strength = context.scene.mask_edge_strength # update property from user input

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT' :

           if context.sculpt_object.use_dynamic_topology_sculpting :

              dynatopoEnabled = True

              bpy.ops.sculpt.dynamic_topology_toggle()

           bmeshContainer = bmesh.new() # New bmesh container

           bmeshContainer.from_mesh(context.active_object.data) # Fill container with our object

           mask = bmeshContainer.verts.layers.paint_mask.verify() # get active mask layer

           bmeshContainer.faces.ensure_lookup_table() # Update vertex lookup table

           mask_edge_angle *= (3.14 * 0.0055556) # Convert angle to radians (approx)

           maskWeight = 1.0 * mask_edge_strength

           for face in bmeshContainer.faces :

                 for vert in face.verts : # for each x face

                    vert [mask] = 0.0 # Clear any mask beforehand

                    for loop in vert.link_loops :

                        loopTan =  loop.calc_tangent()

                        angleFace = (face.normal.angle (-loopTan, 0.0))

                        angleDiff = (vert.normal.angle(-loopTan, 0.0 )) # get the angle between the vert normal to loop edge Tangent

#                        print ("Angle Diff: %f" % (angleDiff))
#                        print ("Cav Angle : %f" % (mask_cavity_angle))
#                        print ("Angle Face : %f" % (angleFace))
#                        print ("AD - AF : %f" % (angleDiff + angleFace))
#                        print ("Loop Tangent : [%s] " % loopTan)

                        if ( angleFace + angleDiff ) <=  (1.57 + mask_edge_angle) : # if the difference is greater then input

                               vert [mask] = maskWeight # mask it with input weight


           bmeshContainer.to_mesh(context.active_object.data) # Fill obj data with bmesh data

           bmeshContainer.free() # Release bmesh

           if dynatopoEnabled :

               bpy.ops.sculpt.dynamic_topology_toggle()

        return {'FINISHED'}


class MaskSmoothAll(bpy.types.Operator):
    ''' Mask Smooth All'''
    bl_idname = "mesh.mask_smooth_all"
    bl_label = "Mask Smooth All"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod

    def poll(cls, context):

        return context.active_object is not None and context.active_object.mode == 'SCULPT'


    bpy.types.Scene.mask_smooth_strength = bpy.props.FloatProperty(name = "Mask Smooth Strength", default = 0.25, min = 0.1, max = 1.0)


    def execute(self, context):

        mask_smooth_strength = context.scene.mask_smooth_strength # update property from user input

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT' :

           if context.sculpt_object.use_dynamic_topology_sculpting :

              dynatopoEnabled = True

              bpy.ops.sculpt.dynamic_topology_toggle()

           bmeshContainer = bmesh.new() # New bmesh container

           bmeshContainer.from_mesh(context.active_object.data) # Fill container with our object

           mask = bmeshContainer.verts.layers.paint_mask.active # get active mask layer

           bmeshContainer.verts.ensure_lookup_table() # Update vertex lookup table

           for vert in bmeshContainer.verts :

                for edge in vert.link_edges :

                    if vert [mask] < (edge.other_vert(vert) [mask] * abs(vert [mask]- mask_smooth_strength)):

                       vert [mask]  = (edge.other_vert(vert) [mask] * abs(vert [mask] -mask_smooth_strength))

                    if vert [mask]< 0.0 :

                        vert [mask] = 0.0

                    elif vert [mask]> 1.0 :

                        vert [mask] = 1.0


           bmeshContainer.to_mesh(context.active_object.data) # Fill obj data with bmesh data

           bmeshContainer.free() # Release bmesh

           if dynatopoEnabled :

               bpy.ops.sculpt.dynamic_topology_toggle()

        return {'FINISHED'}


def register():

    bpy.types.Scene.mask_edge_angle = MaskFromEdges.mask_edge_angle

    bpy.types.Scene.mask_edge_strength = MaskFromEdges.mask_edge_strength

    bpy.types.Scene.mask_cavity_angle = MaskFromCavity.mask_cavity_angle

    bpy.types.Scene.mask_cavity_strength = MaskFromCavity.mask_cavity_strength

    bpy.types.Scene.mask_smooth_strength = MaskSmoothAll.mask_smooth_strength

    bpy.utils.register_module(__name__)




def unregister():

    bpy.types.Scene.mask_edge_angle

    bpy.types.Scene.mask_edge_strength

    bpy.types.Scene.mask_cavity_angle

    bpy.types.Scene.mask_cavity_strength

    bpy.types.Scene.mask_smooth_strength

    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
