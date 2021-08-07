import supalib

EPS = 0.001
TOLE = 0.2
DIM=48
THICK=10
BASE=5
db = DIM+BASE
pipe_rad=11

bm = supalib.create_box( (DIM,DIM,THICK), place=(-DIM*0.5, -DIM*0.5, 0.0) )
bo = supalib.create_box( (db, db,THICK), place=( -db*0.5, -db*0.5, 0.0 ) )
bb = supalib.create_box( (db, BASE*0.5, pipe_rad + THICK ), place=( -db*0.5, db*0.5 - BASE*0.5 + EPS,0 ) )

fix = supalib.create_cut( bo, bm ) 
fix = supalib.create_union( (fix, bb) )

pipe_sz = 20
pipe_x = 10.6
pipe_z = THICK

def creta_pipe_re():
    return supalib.create_cyl( radius=0.5*7.2, size_z = pipe_sz + TOLE, place=(0,0,-EPS) )

om  = supalib.create_cyl( radius=0.5*7.2, size_z = pipe_sz )
os  = supalib.create_cyl( radius=0.5*pipe_rad, size_z = pipe_sz  )


def pipe_relocate( obj ):
    obj = supalib.relocate( obj, rotate=(1,0,0,90))
    obj = supalib.relocate( obj, place=(pipe_x,DIM*0.5 + pipe_sz,pipe_z))
    return obj

pipe = supalib.create_cut( os, om)
pipe = pipe_relocate( pipe )
om = creta_pipe_re()
om = pipe_relocate( om )
fix = supalib.create_cut( fix, om )
fix = supalib.create_union( (fix, pipe )) 

fix = supalib.create_chamfer( fix, (fix.Shape.Edges[23],),  radius=2.0 )

fix.Label="hydro_pump_fix"
mesh = supalib.creta_mesh_from( fix, save_to="/home/pauli/", version=1 )

supalib.finish()

