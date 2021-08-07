import supalib

EPS = 0.001
TOLE = 0.2
PIPE_RAD = 95.0/2.0
SUPPORT_LEN = 40
THICK = 1.6

HOLE_SIZE = 2.0
WITH_HOLES = False

shell   = supalib.create_cyl( radius=PIPE_RAD , size_z = THICK + SUPPORT_LEN, place=(0,0,0) ) 
shell_m = supalib.create_cyl( radius=PIPE_RAD - THICK, size_z = 2*SUPPORT_LEN, place=(0,0,THICK) ) 
shell = supalib.create_cut( shell, shell_m )
shell_m = supalib.create_box( (1000,1000,1000), place=(0,-500,0))
shell = supalib.create_cut( shell, shell_m )

shell_m = supalib.create_box( (1000,1000,1000), place=(-PIPE_RAD/2,-500,THICK+EPS))
shell = supalib.create_cut( shell, shell_m )

if WITH_HOLES:
    holes = []
    for loop_x in range(11):
        for loop_y in range(11):
            loop_xx = (-1.0 + loop_x / 5.0)*PIPE_RAD + THICK*4
            loop_yy = (-1.0 + loop_y / 5.0)*PIPE_RAD
            holes.append( supalib.create_cyl( radius=HOLE_SIZE , size_z = 2*THICK+EPS, place=(loop_xx,loop_yy,-THICK) )  )
    holes = supalib.create_union( holes )         
    shell = supalib.create_cut( shell, holes )
    shell.Label="hydro_stopper_with_holes"
else:
    shell.Label="hydro_stopper_solid"
    

supalib.finish()


mesh = supalib.creta_mesh_from( shell, save_to="/home/pauli/", version=1 )

supalib.finish()



