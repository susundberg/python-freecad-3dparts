
import supalib

WALL_THICK = 4
SIZE_INNER = [ 85, 40, 30 ]
TOP_OVERLAP = 10
SCREW_SIZE = 1.5
SCREW_THREAD_SIZE = 1.0
TOLE_MM = 0.2

def create_hollow_box( size_in, thick, top_overlap, screw_size = None, screw_thread_size = None, scew_wall_thick = None ):
    thick_scalar = [2,2,1]

    def create_box_base( size_in, thick ):
        box   = supalib.create_box( [ size_in[loop] + thick*thick_scalar[loop]  for loop in range(3) ])
        box_m = supalib.create_box( [si for si in size_in], place=(thick,thick,thick) )
        box_base = supalib.create_cut( box, box_m )
        return box_base, box, box_m

    box_base, box, _box_m = create_box_base(size_in, thick)    
       
    
    screw_cuts_top = []
    if screw_size is not None:
        screw_cyls = []
        screw_cuts = []   

        for xloop in range(0,2):
            for yloop in range(0,2):
                center_x = xloop*(size_in[0] - 2*screw_size ) + screw_size + thick
                center_y = yloop*(size_in[1] - 2*screw_size ) + screw_size + thick
                center_z = thick
                cyl = supalib.create_cyl( screw_size + scew_wall_thick, size_in[2], place=(center_x,center_y,center_z))
                cyl = supalib.create_intersection( [cyl,box])
                cyl_hole = supalib.create_cyl( screw_size , size_in[2], place=(center_x,center_y,center_z)) 
                cyl_hole_large = supalib.create_cyl( screw_size + screw_thread_size , size_in[2], place=(center_x,center_y,center_z)) 
                screw_cyls.append(cyl)
                screw_cuts.append( cyl_hole )
                screw_cuts_top.append(cyl_hole_large)
        print("OK - create union")                
        box_base = supalib.create_union( [box_base] + screw_cyls )
        print("OK create cut")
        screw_cuts = supalib.create_union( screw_cuts )
        box_base = supalib.create_cut( box_base, screw_cuts )
        screw_cuts_top = supalib.create_union( screw_cuts_top )

    top_size_in = [ s + thick*2 + TOLE_MM for s in size_in ]
    top_size_in[2] = top_overlap
    top_base, _top_out, _top_in = create_box_base(top_size_in, thick) 
    top_base = supalib.relocate( top_base, (-thick,-thick,0))
    
    screw_cuts_top = supalib.relocate( screw_cuts_top, (0,0,-4*thick))
    top_base = supalib.create_cut( top_base, screw_cuts_top )
    top_base = supalib.relocate( top_base, place=(0,size_in[1] + 2*thick,size_in[2] + 2*thick), rotate=(1,0,0,180)) 
    
    hole_wire = supalib.create_cyl( screw_size, 20, place=(15,26,20))
    top_base = supalib.create_cut( top_base, hole_wire)

    hole_pipes = supalib.create_union( [supalib.create_cyl( 2.0, 20, place=(0, (48/3)*(loop+1), 0 )) for loop in range(2)] )
    hole_pipes = supalib.relocate( hole_pipes, place=(-10,0,15), rotate=(0,1,0,90)) 
    box_base = supalib.create_cut( box_base, hole_pipes)
    
    box_base.Label = "box_base"
    top_base.Label = "box_top"
    return box_base, top_base



    


box_bot, box_top = create_hollow_box( SIZE_INNER, WALL_THICK, TOP_OVERLAP, SCREW_SIZE, SCREW_THREAD_SIZE, WALL_THICK )

mesh_bot = supalib.creta_mesh_from( box_bot, save_to="/home/pauli/", version=1 )
mesh_top = supalib.creta_mesh_from( box_top, save_to="/home/pauli/", version=1 )

