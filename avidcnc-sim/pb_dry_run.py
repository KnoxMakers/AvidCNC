
from qtpyvcp.hal import getComponent
from qtpyvcp.plugins import getPlugin

...

  def __init__(... ):
    ...
    
            self.g5x_index = None
        
        self._status = getPlugin('status')
        
        self._status.g5x_offset.notify(self.get_extents)
        self._status.g5x_index.notify(self.on_g5x_changed)
        
        self.extents_comp = getComponent()
        self.extents_comp.addPin("xmin", "float", "io")
        self.extents_comp.addPin("ymin", "float", "io")
        self.extents_comp.addPin("xmax", "float", "io")
        self.extents_comp.addPin("ymax", "float", "io")
        
    
    def on_g5x_changed(self, index):
        
        print("###################3")
        print(f"PART INDEX {index}")
        
        self.g5x_index = index
        self.get_extents()
    
    def get_extents(self, *arg, **args):
        
        print("###################3")
        
        if self.g5x_index is not None:
            index = self.g5x_index -1
            if index in self.vtk.program_bounds_actors.keys():
                bounds = self.vtk.program_bounds_actors[index]
                print("BOUNDS")
                
                print(bounds.path_actor.GetBounds())
                
                x_min, x_max, y_min, y_max, z_min, z_max = bounds.path_actor.GetBounds()
                
                
                self.extents_comp.getPin('xmin').value = x_min
                self.extents_comp.getPin('ymin').value = y_min
                self.extents_comp.getPin('xmax').value = x_max
                self.extents_comp.getPin('ymax').value = y_max
