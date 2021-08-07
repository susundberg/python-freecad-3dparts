import supalib


TOLE=0.2
OUTSIZE=60.0
SIZE_CONST=25.0
SIZE_DROP=20.0
ANGLE_DROP=45.0
BASE_THICK=5.0
BASE_WIDE=20.0

PIPE_RAD=OUTSIZE/2.0 + TOLE

hole = supalib.create_cyl( radius=PIPE_RAD , size_z = OUTSIZE, place=(0, PIPE_RAD + 1.0, -OUTSIZE/2.0) )
outer_hole = supalib.create_cyl( radius=PIPE_RAD + 5.0 , size_z = OUTSIZE, place=(0, PIPE_RAD + 5.0, -OUTSIZE/2.0) ) 

tr1 = supalib.create_triangle( SIZE_DROP, BASE_THICK, BASE_WIDE/2.0 )
tr2 = supalib.create_triangle( SIZE_DROP, BASE_THICK, BASE_WIDE/2.0,rotate=(1,0,0,180),place=(0,+BASE_THICK,0) )
drop = supalib.create_union( (tr1, tr2) )
drop = supalib.relocate( drop, rotate=(0,1,0,90) )
drop = supalib.create_cut( drop, hole )


drop = supalib.relocate( drop, rotate=(1,0,0,30) )
drop = supalib.relocate( drop, place=(0,0,SIZE_CONST + SIZE_DROP ) )
drop = supalib.relocate( drop, place=(0,-9,-1) )


base = supalib.create_box( (BASE_WIDE,BASE_THICK,SIZE_CONST + 4.0), place = ( -BASE_WIDE/2.0,0.0,0.0)   )
base = supalib.create_intersection( ( base, outer_hole ) )


base = supalib.create_union( ( base, drop ) )
base = supalib.create_cut( base, hole )
base.Label="house_drain"

holder_rad = PIPE_RAD + 0.5 + TOLE
HOLDER_SIZE=5.0
outer_hole2 = supalib.create_cyl( radius=holder_rad , size_z = HOLDER_SIZE, place=(0, 0, 0) ) 
outer_hole3 = supalib.create_cyl( radius=holder_rad + 1.0 , size_z = HOLDER_SIZE, place=(0, 0, 0) ) 
outer_holder = supalib.create_cut( outer_hole3, outer_hole2 )
outer_holder = supalib.relocate( outer_holder, place=(0,+holder_rad,0) )
outer_holder.Label="house_holder"

thight = supalib.create_box( (BASE_WIDE,BASE_THICK,10), place = ( -BASE_WIDE/2.0,0.0,0.0)   )
thight = supalib.create_cut( thight, hole )
thight = supalib.create_intersection( ( thight, outer_hole ) )
thight = supalib.relocate( thight, rotate=(0,0,1,180), place=(0,2*holder_rad,0) )
thight.Label = "house_wedge"

parts = [ thight, outer_holder, base ]
for p in parts:
    supalib.creta_mesh_from( p, save_to="/home/pauli/", version=3 )
    


    #hole_app = supalib.create_box( (0.5,0.25 + TOLE,5.0) ,  place=(offset - 0.25, 5.0 - rad_size/2.0 - 2*TOLE, 2.5 ) )
    #offset += rad_size + RADS[loop+1] + 2.0
    #holes.append(hole)
    #hole_adds.append( hole_app )
#holes = supalib.create_union( holes )
#hole_adds = supalib.create_union( hole_adds )

#box_bound = supalib.create_box( (offset, 10.0, 10 ) )
#box_bound = supalib.create_fillet( box_bound )
#box_bound = supalib.create_cut( box_bound, holes )
#box_bound = supalib.create_union( (box_bound,hole_adds) )

#box_bound.Label="Tool_holder"
#mesh = supalib.creta_mesh_from( box_bound, save_to="/home/pauli/", version=1 )

supalib.finish()

