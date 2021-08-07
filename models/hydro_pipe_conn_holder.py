import supalib

EPS = 0.2
TOLE = 0.2

SMALL_PIPE = False
RAD_LARGE = 104/2
THICK     = 3.0


SUP_LEN = 40 
TOR_RAD=4

#c1 = supalib.create_cyl( radius=RAD_LARGE + THICK + EPS, size_z = SUP_LEN, place=(0, 0, 0 ) )
#c2 = supalib.create_cyl( radius=RAD_LARGE , size_z = SUP_LEN, place=(0, 0, 0 ) )
#base = supalib.create_cut( c1, c2 )

#c1c = supalib.create_cyl( radius=RAD_LARGE + THICK  - EPS, size_z = SUP_LEN - EPS, place=(0, 0, 0 ) )

#to1 = supalib.create_torus( RAD_LARGE + THICK - EPS, TOR_RAD, place=(0,0,TOR_RAD ) )
#to2 = supalib.create_torus( RAD_LARGE + THICK - EPS, TOR_RAD, place=(0,0,SUP_LEN - TOR_RAD ) )
#tors = supalib.create_union( ( to1, to2 ) )

#tors = supalib.create_intersection( c1c, tors )

#holder = supalib.create_union ( ( base, tors ) )
##supalib.crete_crossection( holder, (0,1,0))


#supalib.finish()


wt = 4
ms = 40
tl = 1
ts = 2
PIPE_RAD=105*0.5
holder_wire = [ [0.0, 0.0], [tl,ts], [0.0,ts*2], [ 0.0, ms - ts*2], [ tl, ms - ts], [ 0, ms ],
                   [ -wt, ms ], 
                   [-wt,0.0]  
                 ]
holder_face = supalib.face_create( holder_wire, closed=True, face=True )

holder = supalib.face_revolve( holder_face, revolve_axis=(0,1,0), revolve_offset=(PIPE_RAD  , 0, 0 ), angle = 225 )
holder2 = supalib.face_revolve( holder_face, revolve_axis=(0,1,0), revolve_offset=(PIPE_RAD  , 0, 0 ), angle = 90 )
holder = supalib.relocate( holder, place=(0,0,0), rotate=(1,0,0,-90) )
holder2 = supalib.relocate( holder2, place=(0,0,-50), rotate=(1,0,0,-90) )

holder.Label  = "hydro_pipe_holder_lg"
holder2.Label = "hydro_pipe_holder_sm"
mesh = supalib.creta_mesh_from( holder, save_to="/home/pauli/", version=1 )
mesh = supalib.creta_mesh_from( holder2, save_to="/home/pauli/", version=1 )

#supalib.crete_crossection( holder, (1,0,0))

supalib.finish()



