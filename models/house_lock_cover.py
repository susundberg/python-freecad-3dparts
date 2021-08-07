import supalib

EPS = 0.001

TOLE = 0.2
LOCK_RAD = 54.0/2.0
COVER_SIZE = 15.0
OUTER_RAD = 10
BASE_THICK = 3.0
SCREW_OFFSET = 0.5*(LOCK_RAD + OUTER_RAD + LOCK_RAD + BASE_THICK)
c1 = supalib.create_cyl( radius=LOCK_RAD + OUTER_RAD , size_z = BASE_THICK )
c2 = supalib.create_cyl( radius=LOCK_RAD + BASE_THICK, size_z = COVER_SIZE )
h1 = supalib.create_cyl( radius=LOCK_RAD, size_z = COVER_SIZE*2.0, place=( 0, 0, -EPS ) )
h2 = supalib.create_cyl( radius=1.0, size_z = BASE_THICK*2, place=( -SCREW_OFFSET, 0,0) )
bounding = supalib.create_box( (100,100,100), place=(-14,-50,-2*EPS) )

#hole2           = supalib.create_cyl( radius=PIPE_RAD , size_z = OUTSIZE, place=(0, 0, SADDLE_SIZE ) )
#hole3           = supalib.create_cyl( radius=PIPE_RAD - SADDLE_HEI , size_z = SADDLE_SIZE + 2*EPS, place=(0, 0, -EPS) )
holes = supalib.create_union( ( h1, h2 ) )
shell  = supalib.create_union( (c1, c2 ) )
shell = supalib.create_cut( shell, bounding )

cover = supalib.create_cut( shell, holes )


cover.Label="house_lock_cover"

mesh = supalib.creta_mesh_from( cover, save_to="/home/pauli/", version=1 )
