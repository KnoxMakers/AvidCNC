#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import linuxcnc

from hal import component, HAL_BIT, HAL_U32, HAL_IN, HAL_OUT

def ok_for_mdi(s):
    s.poll()
    return not s.estop and s.enabled and (s.homed.count(1) == s.joints) and (s.interp_state == linuxcnc.INTERP_IDLE)

def main():

    print("INIT DryRun COMP")
    
    s = linuxcnc.stat()
    c = linuxcnc.command()
    
    comp = component("dry_run")
    comp.newpin("run_in", HAL_BIT, HAL_IN)
    comp.ready()

    print("DryRun COMP READY")
    drun_run_on = False

    while True:

        run_macro = comp["run_in"]

        if run_macro == True:
            
            if drun_run_on == False:
                
                if ok_for_mdi(s):
                    
                    drun_run_on = True
                                        
                    c.mode(linuxcnc.MODE_MDI)
                    c.wait_complete() # wait until mode switch executed
                        
                    # ( Move to first corner of bounding box )
                    c.mdi("G53 G1 F1000 X#<_hal[qtpyvcp.xmin]> Y#<_hal[qtpyvcp.ymin]>")
                    # ( Drive around the block )
                    c.mdi("G53 G1 F1000 X#<_hal[qtpyvcp.xmin]> Y#<_hal[qtpyvcp.ymax]>")
                    c.mdi("G53 G1 F1000 X#<_hal[qtpyvcp.xmax]> Y#<_hal[qtpyvcp.ymax]>")
                    c.mdi("G53 G1 F1000 X#<_hal[qtpyvcp.xmax]> Y#<_hal[qtpyvcp.ymin]>")
                    c.mdi("G53 G1 F1000 X#<_hal[qtpyvcp.xmin]> Y#<_hal[qtpyvcp.ymin]>")

        else:
            drun_run_on = False
            

if __name__ == "__main__":
    main()
