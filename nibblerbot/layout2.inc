[XHC_HB04_BUTTONS]
# use button names according to layout file LIB:xhc-hb04-layout{n}.cfg
# note: "start-pause" is connected for standard behavior
#        controlling halui.pause/halui.resume/halui.run
# these are examples, edit as required:

goto-zero   = halui.mdi-command-00
# synthesized per-axis buttons for goto-zero button:
goto-zero-x = ""
goto-zero-y = ""
goto-zero-z = ""
goto-zero-a = ""

start-pause = std_start_pause
rewind      = halui.program.step
# probe-input for simulating a probe:
probe-z     = halui.mdi-command-02
macro-3     = halui.mdi-command-06

#half        = halui.spindle.0.stop
half        = ""
# synthesized per-axis buttons for half button:
half-x      = halui.mdi-command-04
half-y      = halui.mdi-command-05
half-z      = ""
half-a      = ""

zero        = ""
# synthesized per-axis buttons for zero button:
zero-x      = halui.mdi-command-12
zero-y      = halui.mdi-command-13
zero-z      = halui.mdi-command-14
zero-a      = halui.mdi-command-15

safe-z      = halui.mdi-command-10
# in this sim, home-all only works first time, hold down till finished:
home        = halui.mdi-command-08
macro-1     = halui.mdi-command-07
macro-2     = halui.mdi-command-03
#spindle     = halui.spindle.0.start
#Go To Operator
#spindle     = halui.mdi-command-01
step        = xhc-hb04.stepsize-up
#mode        = toggle_mod
macro-6     = halui.mdi-command-09
macro-7     = halui.mdi-command-11
stop        = halui.program.stop
reset       = halui.estop.activate

[HALUI]
# these are examples, edit as required:
# a halui hal pin is created for each MDI_COMMAND below
# halui.mdi-command-00, halui.mdi-command-01,... etc
#0
MDI_COMMAND=O<go_to_zero> CALL
#1
MDI_COMMAND=O<go_to_g30> CALL
#2
MDI_COMMAND=O<probe_z_minus_wco> CALL
#3
MDI_COMMAND=O<probe_back_left_top_corner> CALL
#4
MDI_COMMAND=G10 L20 P0 X[#<_x>/2.0] 
#5
MDI_COMMAND=G10 L20 P0 Y[#<_y>/2.0]
#6
MDI_COMMAND=O<probe_back_right_top_corner> CALL
#7
MDI_COMMAND=O<probe_round_pocket_center_start> CALL 
#8
MDI_COMMAND=O<go_to_home> CALL
#9
MDI_COMMAND=O<probe_front_left_top_corner> CALL
#10
MDI_COMMAND=G0 G53 Z0
#11
MDI_COMMAND=O<probe_front_right_top_corner> CALL
#12
MDI_COMMAND= G10 L20 P0 X0
#13
MDI_COMMAND= G10 L20 P0 Y0
#14
MDI_COMMAND= G10 L20 P0 Z0
#15
MDI_COMMAND= G10 L20 P0 C0
