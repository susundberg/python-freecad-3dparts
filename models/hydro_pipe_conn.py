import supalib

EPS = 0.001
TOLE = 0.2

SMALL_PIPE = False


if SMALL_PIPE:
    part_name="spipe"
    part_version=2
    PIPE_RAD=31.0 / 2.0
    WALL_THICK = 2.0
    MOUNT_SIZE = 50
    MOUNT_TOLERANCE = 1.2
else:
    part_name="pipe"
    part_version=6
    PIPE_RAD        = 102.0 / 2.0
    WALL_THICK      = 1.6
    MOUNT_SIZE      = 120
    MOUNT_TOLERANCE = 0.6
    
#hole1           = supalib.create_cyl( radius=PIPE_RAD , size_z = OUTSIZE, place=(0, 0, -OUTSIZE ) )
#hole2           = supalib.create_cyl( radius=PIPE_RAD , size_z = OUTSIZE, place=(0, 0, SADDLE_SIZE ) )
#hole3           = supalib.create_cyl( radius=PIPE_RAD - SADDLE_HEI , size_z = SADDLE_SIZE + 2*EPS, place=(0, 0, -EPS) )

#holes = supalib.create_union( (hole1, hole2, hole3) )

#shell = supalib.create_cyl( radius=PIPE_RAD + WALL_THICK , size_z = OUTSIZE*2 + SADDLE_SIZE, place=(0,0,-OUTSIZE) ) 

#shell = supalib.create_cyl( radius=PIPE_RAD + WALL_THICK + TOLE + EPS, size_z = SADDLE_SIZE, place=(0,0,-OUTSIZE) ) 
#hole1           = supalib.create_cyl( radius=PIPE_RAD + TOLE + EPS , size_z = OUTSIZE, place=(0, 0, -OUTSIZE ) )
#p1 = supalib.create_cut( shell, hole1 )

wt = WALL_THICK
ms = MOUNT_SIZE
tl = MOUNT_TOLERANCE
sealing_holder = [ [tl, 0.0], [0.0,ms/2], [tl,ms],
                   [tl + wt, ms], [wt,ms/2], [tl + wt, 00.0],
                 ]
sealing_holder = supalib.face_create( sealing_holder, closed=True, face=True )
sealing_holder = supalib.face_revolve( sealing_holder, revolve_axis=(0,1,0), revolve_offset=(-PIPE_RAD  , 0, 0 ) )
sealing_holder = supalib.relocate( sealing_holder, rotate=(0,1,0,90) )

#p1 = supalib.create_union( ( p1, sealing_holder ) ) 

sealing_holder.Label="hydro_" + part_name + "_pipe_holder"


mesh = supalib.creta_mesh_from( sealing_holder, save_to="/home/pauli/", version=part_version )

supalib.finish()


