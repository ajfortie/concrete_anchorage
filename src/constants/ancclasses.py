
from constants import properties as prop
from functions import ancgeometry as geom

# The class definition below defines anchor geometry and location properties
class anc_class:
    def __init__(self,anc,heff,headtype,washer_size=0,washer_thickness=0,anc_type="CIP",):
        # units are in inches
        self.type = anc_type
        self.da = prop.anchor_dict[anc]["Nominal Dia."]
        self.Anom = prop.anchor_dict[anc]["Nominal Area"]
        self.Aeff = prop.anchor_dict[anc]["Stress Area"]
        self.head = headtype
        self.Abrg = prop.anchor_dict[anc][headtype]
        self.heff = heff
        self.matl = prop.anchor_dict[anc]["Material"]
        self.fyanc = prop.matl_dict[prop.anchor_dict[anc]["Material"]]["Yield"]
        self.fuanc = prop.matl_dict[prop.anchor_dict[anc]["Material"]]["Ult"]
        self.d_wash = washer_size
        self.t_wash = washer_thickness
        self.pts = []
        self.pts_x = []
        self.pts_y = []
        self.CoG = []
    def add_point(self,point):
        # point shall be an nested list [[x0,y0],[x1,y1]...]
        for i in point:
            self.pts.append(i)
            self.pts_x.append(i[0])
            self.pts_y.append(i[1])
            self.CoG = geom.anc_CoG(self.pts_x,self.pts_y)

# The class below defines the geometric and material properties of the
# base material
