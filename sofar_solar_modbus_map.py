# =======================================
#                                       #
# Real time data (0x0400-0x07FF)        #
#                                       #
# =======================================
# Real time data (0x0400-0x07FF)
# System info (0x0400-0x047F)
ADDRESS_MASK_REALTIME_SYSINFO1 = 0x0400
SYS_STATE = 0x0404
FAULT1 = 0x0405
FAULT2 = 0x0406
FAULT3 = 0x0407
FAULT4 = 0x0408
FAULT5 = 0x0409
FAULT6 = 0x040A
FAULT7 = 0x040B
FAULT8 = 0x040C
FAULT9 = 0x040D
FAULT10 = 0x040E
FAULT11 = 0x040F
FAULT12 = 0x0410
FAULT13 = 0x0411
FAULT14 = 0x0412
FAULT15 = 0x0413
FAULT16 = 0x0414
FAULT17 = 0x0415
FAULT18 = 0x0416
COUNTDOWN = 0x0417
TEMPERATURE_ENV1 = 0x0418
TEMPERATURE_ENV2 = 0x0419
TEMPERATURE_HEATSINK1 = 0x041A
TEMPERATURE_HEATSINK2 = 0x041B
TEMPERATURE_HEATSINK3 = 0x041C
TEMPERATURE_HEATSINK4 = 0x041D
TEMPERATURE_HEATSINK5 = 0x041E
TEMPERATURE_HEATSINK6 = 0x041F
TEMPERATURE_INV1 = 0x0420
TEMPERATURE_INV2 = 0x0421
TEMPERATURE_INV3 = 0x0422
TEMP_RSV1 = 0x0423
TEMP_RSV2 = 0x0424
TEMP_RSV3 = 0x0425
GENERATION_TIME_TODAY = 0x0426
GENERATION_TIME_TOTAL = 0x0427
SERVICE_TIME_TOTAL = 0x0429
INSULATION_RESISTANCE = 0x042B
SYS_TIME_YEAR = 0x042C
SYS_TIME_MONTH = 0x042D
SYS_TIME_DATE = 0x042E
SYS_TIME_HOUR = 0x042F
SYS_TIME_MINUTE = 0x0430
SYS_TIME_SECOND = 0x0431
# On grid output (0x0480-0x04FF)
ADDRESS_MASK_REALTIME_GRID_OUTPUT1 = 0x0480
# Note: 0481-0483 are part of AddressMask_Realtime_GridOutput1 and do not have individual entries
FREQUENCY_GRID = 0x0484
ACTIVE_POWER_OUTPUT_TOTAL = 0x0485
REACTIVE_POWER_OUTPUT_TOTAL = 0x0486
APPARENT_POWER_OUTPUT_TOTAL = 0x0487
ACTIVE_POWER_PCC_TOTAL = 0x0488
REACTIVE_POWER_PCC_TOTAL = 0x0489
APPARENT_POWER_PCC_TOTAL = 0x048A
GRID_OUTPUT_RSVD1 = 0x048B
GRID_OUTPUT_RSVD2 = 0x048C
VOLTAGE_PHASE_R = 0x048D
CURRENT_OUTPUT_R = 0x048E
ACTIVE_POWER_OUTPUT_R = 0x048F
REACTIVE_POWER_OUTPUT_R = 0x0490
POWER_FACTOR_OUTPUT_R = 0x0491
CURRENT_PCC_R = 0x0492
ACTIVE_POWER_PCC_R = 0x0493
REACTIVE_POWER_PCC_R = 0x0494
POWER_FACTOR_PCC_R = 0x0495
R_RSVD1 = 0x0496
R_RSVD2 = 0x0497
VOLTAGE_PHASE_S = 0x0498
CURRENT_OUTPUT_S = 0x0499
ACTIVE_POWER_OUTPUT_S = 0x049A
REACTIVE_POWER_OUTPUT_S = 0x049B
POWER_FACTOR_OUTPUT_S = 0x049C
CURRENT_PCC_S = 0x049D
ACTIVE_POWER_PCC_S = 0x049E
REACTIVE_POWER_PCC_S = 0x049F
POWER_FACTOR_PCC_S = 0x04A0
S_RSVD1 = 0x04A1
S_RSVD2 = 0x04A2
VOLTAGE_PHASE_T = 0x04A3
CURRENT_OUTPUT_T = 0x04A4
ACTIVE_POWER_OUTPUT_T = 0x04A5
REACTIVE_POWER_OUTPUT_T = 0x04A6
POWER_FACTOR_OUTPUT_T = 0x04A7
CURRENT_PCC_T = 0x04A8
ACTIVE_POWER_PCC_T = 0x04A9
REACTIVE_POWER_PCC_T = 0x04AA
POWER_FACTOR_PCC_T = 0x04AB
T_RSVD1 = 0x04AC
T_RSVD2 = 0x04AD
ACTIVE_POWER_PV_EXT = 0x04AE
ACTIVE_POWER_LOAD_SYS = 0x04AF
VOLTAGE_PHASE_L1N = 0x04B0
CURRENT_OUTPUT_L1N = 0x04B1
ACTIVE_POWER_OUTPUT_L1N = 0x04B2
CURRENT_PCC_L1N = 0x04B3
ACTIVE_POWER_PCC_L1N = 0x04B4
VOLTAGE_PHASE_L2N = 0x04B5
CURRENT_OUTPUT_L2N = 0x04B6
ACTIVE_POWER_OUTPUT_L2N = 0x04B7
CURRENT_PCC_L2N = 0x04B8
ACTIVE_POWER_PCC_L2N = 0x04B9
VOLTAGE_LINE_L1 = 0x04BA
VOLTAGE_LINE_L2 = 0x04BB
VOLTAGE_LINE_L3 = 0x04BC
# Off grid output (0x0500-0x057F)
ADDRESS_MASK_REALTIME_EMERGENCY_OUTPUT1 = 0x0500
# 0501 to 0503 are part of the address mask and do not require individual entries
ACTIVE_POWER_LOAD_TOTAL = 0x0504
REACTIVE_POWER_LOAD_TOTAL = 0x0505
APPARENT_POWER_LOAD_TOTAL = 0x0506
FREQUENCY_OUTPUT = 0x0507
ESOUTPUT_RSVD1 = 0x0508
ESOUTPUT_RSVD2 = 0x0509
VOLTAGE_OUTPUT_R = 0x050A
CURRENT_LOAD_R = 0x050B
ACTIVE_POWER_LOAD_R = 0x050C
REACTIVE_POWER_LOAD_R = 0x050D
APPARENT_POWER_LOAD_R = 0x050E
LOAD_PEAK_RATIO_R = 0x050F
ESR_RSVD1 = 0x0510
ESR_RSVD2 = 0x0511
VOLTAGE_OUTPUT_S = 0x0512
CURRENT_LOAD_S = 0x0513
ACTIVE_POWER_LOAD_S = 0x0514
REACTIVE_POWER_LOAD_S = 0x0515
APPARENT_POWER_LOAD_S = 0x0516
LOAD_PEAK_RATIO_S = 0x0517
ESS_RSVD1 = 0x0518
ESS_RSVD2 = 0x0519
VOLTAGE_OUTPUT_T = 0x051A
CURRENT_LOAD_T = 0x051B
ACTIVE_POWER_LOAD_T = 0x051C
REACTIVE_POWER_LOAD_T = 0x051D
APPARENT_POWER_LOAD_T = 0x051E
LOAD_PEAK_RATIO_T = 0x051F
EST_RSVD1 = 0x0520
EST_RSVD2 = 0x0521
VOLTAGE_OUTPUT_L1N = 0x0522
CURRENT_LOAD_L1N = 0x0523
ACTIVE_POWER_LOAD_L1N = 0x0524
VOLTAGE_OUTPUT_L2N = 0x0525
CURRENT_LOAD_L2N = 0x0526
ACTIVE_POWER_LOAD_L2N = 0x0527
# PV input (0x0580-0x05FF)
ADDRESS_MASK_REALTIME_INPUT_PV1 = 0x0580
VOLTAGE_PV1 = 0x0584
CURRENT_PV1 = 0x0585
POWER_PV1 = 0x0586
VOLTAGE_PV2 = 0x0587
CURRENT_PV2 = 0x0588
POWER_PV2 = 0x0589
VOLTAGE_PV3 = 0x058A
CURRENT_PV3 = 0x058B
POWER_PV3 = 0x058C
VOLTAGE_PV4 = 0x058D
CURRENT_PV4 = 0x058E
POWER_PV4 = 0x058F
VOLTAGE_PV5 = 0x0590
CURRENT_PV5 = 0x0591
POWER_PV5 = 0x0592
VOLTAGE_PV6 = 0x0593
CURRENT_PV6 = 0x0594
POWER_PV6 = 0x0595
VOLTAGE_PV7 = 0x0596
CURRENT_PV7 = 0x0597
POWER_PV7 = 0x0598
VOLTAGE_PV8 = 0x0599
CURRENT_PV8 = 0x059A
POWER_PV8 = 0x059B
VOLTAGE_PV9 = 0x059C
CURRENT_PV9 = 0x059D
POWER_PV9 = 0x059E
VOLTAGE_PV10 = 0x059F
CURRENT_PV10 = 0x05A0
POWER_PV10 = 0x05A1
VOLTAGE_PV11 = 0x05A2
CURRENT_PV11 = 0x05A3
POWER_PV11 = 0x05A4
VOLTAGE_PV12 = 0x05A5
CURRENT_PV12 = 0x05A6
POWER_PV12 = 0x05A7
VOLTAGE_PV13 = 0x05A8
CURRENT_PV13 = 0x05A9
POWER_PV13 = 0x05AA
VOLTAGE_PV14 = 0x05AB
CURRENT_PV14 = 0x05AC
POWER_PV14 = 0x05AD
VOLTAGE_PV15 = 0x05AE
CURRENT_PV15 = 0x05AF
POWER_PV15 = 0x05B0
VOLTAGE_PV16 = 0x05B1
CURRENT_PV16 = 0x05B2
POWER_PV16 = 0x05B3
# Battery input (0x0600-0x067F)
ADDRESS_MASK_REALTIME_INPUT_BAT1 = 0x0600
VOLTAGE_BAT1 = 0x0604
CURRENT_BAT1 = 0x0605
POWER_BAT1 = 0x0606
TEMPERATURE_ENV_BAT1 = 0x0607
SOC_BAT1 = 0x0608
SOH_BAT1 = 0x0609
CHARGE_CYCLE_BAT1 = 0x060A
VOLTAGE_BAT2 = 0x060B
CURRENT_BAT2 = 0x060C
POWER_BAT2 = 0x060D
TEMPERATURE_ENV_BAT2 = 0x060E
SOC_BAT2 = 0x060F
SOH_BAT2 = 0x0610
CHARGE_CYCLE_BAT2 = 0x0611
VOLTAGE_BAT3 = 0x0612
CURRENT_BAT3 = 0x0613
POWER_BAT3 = 0x0614
TEMPERATURE_ENV_BAT3 = 0x0615
SOC_BAT3 = 0x0616
SOH_BAT3 = 0x0617
CHARGE_CYCLE_BAT3 = 0x0618
VOLTAGE_BAT4 = 0x0619
CURRENT_BAT4 = 0x061A
POWER_BAT4 = 0x061B
TEMPERATURE_ENV_BAT4 = 0x061C
SOC_BAT4 = 0x061D
SOH_BAT4 = 0x061E
CHARGE_CYCLE_BAT4 = 0x061F
VOLTAGE_BAT5 = 0x0620
CURRENT_BAT5 = 0x0621
POWER_BAT5 = 0x0622
TEMPERATURE_ENV_BAT5 = 0x0623
SOC_BAT5 = 0x0624
SOH_BAT5 = 0x0625
CHARGE_CYCLE_BAT5 = 0x0626
VOLTAGE_BAT6 = 0x0627
CURRENT_BAT6 = 0x0628
POWER_BAT6 = 0x0629
TEMPERATURE_ENV_BAT6 = 0x062A
SOC_BAT6 = 0x062B
SOH_BAT6 = 0x062C
CHARGE_CYCLE_BAT6 = 0x062D
VOLTAGE_BAT7 = 0x062E
CURRENT_BAT7 = 0x062F
POWER_BAT7 = 0x0630
TEMPERATURE_ENV_BAT7 = 0x0631
SOC_BAT7 = 0x0632
SOH_BAT7 = 0x0633
CHARGE_CYCLE_BAT7 = 0x0634
VOLTAGE_BAT8 = 0x0635
CURRENT_BAT8 = 0x0636
POWER_BAT8 = 0x0637
TEMPERATURE_ENV_BAT8 = 0x0638
SOC_BAT8 = 0x0639
SOH_BAT8 = 0x063A
CHARGE_CYCLE_BAT8 = 0x063B
ADDRESS_MASK_REALTIME_INPUT_BAT2 = 0x0640
VOLTAGE_BAT9 = 0x0644
CURRENT_BAT9 = 0x0645
POWER_BAT9 = 0x0646
TEMPERATURE_ENV_BAT9 = 0x0647
SOC_BAT9 = 0x0648
SOH_BAT9 = 0x0649
CHARGE_CYCLE_BAT9 = 0x064A
VOLTAGE_BAT10 = 0x064B
CURRENT_BAT10 = 0x064C
POWER_BAT10 = 0x064D
TEMPERATURE_ENV_BAT10 = 0x064E
SOC_BAT10 = 0x064F
SOH_BAT10 = 0x0650
CHARGE_CYCLE_BAT10 = 0x0651
VOLTAGE_BAT11 = 0x0652
CURRENT_BAT11 = 0x0653
POWER_BAT11 = 0x0654
TEMPERATURE_ENV_BAT11 = 0x0655
SOC_BAT11 = 0x0656
SOH_BAT11 = 0x0657
CHARGE_CYCLE_BAT11 = 0x0658
VOLTAGE_BAT12 = 0x0659
CURRENT_BAT12 = 0x065A
POWER_BAT12 = 0x065B
TEMPERATURE_ENV_BAT12 = 0x065C
SOC_BAT12 = 0x065D
SOH_BAT12 = 0x065E
CHARGE_CYCLE_BAT12 = 0x065F
POWER_BAT_TOTAL = 0x0667
SOC_BAT_AVERAGE = 0x0668
SOH_BAT = 0x0669
# Power (0x0680-0x06BF)
ADDRESS_MASK_REALTIME_ELECTRICITY_STATISTICS1 = 0x0680
PV_GENERATION_TODAY = 0x0684
PV_GENERATION_TOTAL = 0x0686
LOAD_CONSUMPTION_TODAY = 0x0688
LOAD_CONSUMPTION_TOTAL = 0x068A
ENERGY_PURCHASE_TODAY = 0x068C
ENERGY_PURCHASE_TOTAL = 0x068E
ENERGY_SELLING_TODAY = 0x0690
ENERGY_SELLING_TOTAL = 0x0692
BAT_CHARGE_TODAY = 0x0694
BAT_CHARGE_TOTAL = 0x0696
BAT_DISCHARGE_TODAY = 0x0698
BAT_DISCHARGE_TOTAL = 0x069A
# Internal info (0x06C0-0x06FF)
# skip
# Combined info (0x0700-0x077F)
ADDRESS_MASK_REALTIME_COMBINERINFO1 = 0x0700
VOLTAGE_GROUP1 = 0x0704
CURRENT_GROUP1_BRANCH1 = 0x0705
CURRENT_GROUP1_BRANCH2 = 0x0706
VOLTAGE_GROUP2 = 0x0707
CURRENT_GROUP2_BRANCH1 = 0x0708
CURRENT_GROUP2_BRANCH2 = 0x0709
VOLTAGE_GROUP3 = 0x070A
CURRENT_GROUP3_BRANCH1 = 0x070B
CURRENT_GROUP3_BRANCH2 = 0x070C
VOLTAGE_GROUP4 = 0x070D
CURRENT_GROUP4_BRANCH1 = 0x070E
CURRENT_GROUP4_BRANCH2 = 0x070F
VOLTAGE_GROUP5 = 0x0710
CURRENT_GROUP5_BRANCH1 = 0x0711
CURRENT_GROUP5_BRANCH2 = 0x0712
VOLTAGE_GROUP6 = 0x0713
CURRENT_GROUP6_BRANCH1 = 0x0714
CURRENT_GROUP6_BRANCH2 = 0x0715
VOLTAGE_GROUP7 = 0x0716
CURRENT_GROUP7_BRANCH1 = 0x0717
CURRENT_GROUP7_BRANCH2 = 0x0718
VOLTAGE_GROUP8 = 0x0719
CURRENT_GROUP8_BRANCH1 = 0x071A
CURRENT_GROUP8_BRANCH2 = 0x071B
VOLTAGE_GROUP9 = 0x071C
CURRENT_GROUP9_BRANCH1 = 0x071D
CURRENT_GROUP9_BRANCH2 = 0x071E
VOLTAGE_GROUP10 = 0x071F
CURRENT_GROUP10_BRANCH1 = 0x0720
CURRENT_GROUP10_BRANCH2 = 0x0721
VOLTAGE_GROUP11 = 0x0722
CURRENT_GROUP11_BRANCH1 = 0x0723
CURRENT_GROUP11_BRANCH2 = 0x0724
VOLTAGE_GROUP12 = 0x0725
CURRENT_GROUP12_BRANCH1 = 0x0726
CURRENT_GROUP12_BRANCH2 = 0x0727
VOLTAGE_GROUP13 = 0x0728
CURRENT_GROUP13_BRANCH1 = 0x0729
CURRENT_GROUP13_BRANCH2 = 0x072A
VOLTAGE_GROUP14 = 0x072B
CURRENT_GROUP14_BRANCH1 = 0x072C
CURRENT_GROUP14_BRANCH2 = 0x072D
VOLTAGE_GROUP15 = 0x072E
CURRENT_GROUP15_BRANCH1 = 0x072F
CURRENT_GROUP15_BRANCH2 = 0x0730
VOLTAGE_GROUP16 = 0x0731
CURRENT_GROUP16_BRANCH1 = 0x0732
CURRENT_GROUP16_BRANCH2 = 0x0733
# Arcing information (0x0780-0x07BF)
# skip
# =======================================
#                                       #
# Safety Parameter Area(0x0800-0x0FFF)  #
#                                       #
# =======================================
#Boot Parameters (0x0800-0x083F)
CONNECT_WAIT_TIME = 0x0800
POWER_UP_SPEED = 0x0801
RECONNECT_WAIT_TIME = 0x0802
RECONNECT_POWER_UP_SPEED = 0x0803
VOLT_HIGH_LIMIT = 0x0804
VOLT_LOW_LIMIT = 0x0805
FREQ_HIGH_LIMIT = 0x0806
FREQ_LOW_LIMIT = 0x0807
RECONNECT_VOLT_HIGH_LIMIT = 0x0808
RECONNECT_VOLT_LOW_LIMIT = 0x0809
RECONNECT_FREQ_HIGH_LIMIT = 0x080A
RECONNECT_FREQ_LOW_LIMIT = 0x080B
# Grid voltage protection Parameters (0x0840-0x087F)
VOLTAGE_CONFIG = 0x0840
RATED_VOLTAGE = 0x0841
FIRST_OVERVOLTAGE_PROTECTION_VALUE = 0x0842
FIRST_OVERVOLTAGE_PROTECTION_TIME = 0x0843
SECOND_OVERVOLTAGE_PROTECTION_VALUE = 0x0844
SECOND_OVERVOLTAGE_PROTECTION_TIME = 0x0845
THIRD_OVERVOLTAGE_PROTECTION_VALUE = 0x0846
THIRD_OVERVOLTAGE_PROTECTION_TIME = 0x0847
FIRST_UNDERVOLTAGE_PROTECTION_VALUE = 0x0848
FIRST_UNDERVOLTAGE_PROTECTION_TIME = 0x0849
SECOND_UNDERVOLTAGE_PROTECTION_VALUE = 0x084A
SECOND_UNDERVOLTAGE_PROTECTION_TIME = 0x084B
THIRD_UNDERVOLTAGE_PROTECTION_VALUE = 0x084C
THIRD_UNDERVOLTAGE_PROTECTION_TIME = 0x084D
TEN_MIN_OVERVOLTAGE_PROTECTION_VALUE = 0x084E
# Frquency Protection Parameter (0x0880-0x08BF)
FREQUENCY_CONFIG = 0x0880
RATED_FREQUENCY = 0x0881
FIRST_OVERFREQUENCY_PROTECTION_VALUE = 0x0882
FIRST_OVERFREQUENCY_PROTECTION_TIME = 0x0883
SECOND_OVERFREQUENCY_PROTECTION_VALUE = 0x0884
SECOND_OVERFREQUENCY_PROTECTION_TIME = 0x0885
THIRD_OVERFREQUENCY_PROTECTION_VALUE = 0x0886
THIRD_OVERFREQUENCY_PROTECTION_TIME = 0x0887
FIRST_UNDERFREQUENCY_PROTECTION_VALUE = 0x0888
FIRST_UNDERFREQUENCY_PROTECTION_TIME = 0x0889
SECOND_UNDERFREQUENCY_PROTECTION_VALUE = 0x088A
SECOND_UNDERFREQUENCY_PROTECTION_TIME = 0x088B
THIRD_UNDERFREQUENCY_PROTECTION_VALUE = 0x088C
THIRD_UNDERFREQUENCY_PROTECTION_TIME = 0x088D
# DCIProtection Parameter (0x08C0-0x08FF)
# skip
# Active power &Over/Under voltage Power Derate  Paramter (0x0900-0x093F)
REMOTE_CONFIG = 0x0900
ACTIVE_OUTPUT_LIMIT = 0x0901
ACTIVE_OUTPUT_DOWN_SPEED = 0x0902
GRID_VOLTAGE_DROP_START = 0x0903
GRID_VOLTAGE_DROP_STOP = 0x0904
GRID_VOLTAGE_DROP_MIN_POWER = 0x0905
OVERVOLTAGE_DOWN_SPEED = 0x0906
CHG_DERATE_VOLT_START = 0x0907
CHG_DERATE_VOLT_END = 0x0908
CHG_DERATE_MIN_POWER = 0x0909
POWER_FOR_LOGIC_1 = 0x090A
POWER_FOR_LOGIC_2 = 0x090B
POWER_FOR_LOGIC_3 = 0x090C
POWER_FOR_LOGIC_4 = 0x090D
POWER_FOR_LOGIC_5 = 0x090E
POWER_FOR_LOGIC_6 = 0x090F
POWER_FOR_LOGIC_7 = 0x0910
POWER_FOR_LOGIC_8 = 0x0911
REFLUX_POWER = 0x0912
REFLUX_OV_LOAD_TIME = 0x0913
LOGIC_DERATE_SPEED = 0x0914
LOGIC_RELOAD_SPEED = 0x0915
VOLTAGE_DERATE_RESPONSE_TIME = 0x0916
# Over/Under Frquency Power Derate (0x0940-0x097F)
FREQUENCY_DERATE_CONFIG = 0x0940
OVERFREQUENCY_START = 0x0941
OVERFREQUENCY_END = 0x0942
OVERFREQUENCY_SLOPE = 0x0943
OVERFREQUENCY_RESPONSE_DELAY = 0x0944
OVERFREQUENCY_RELOAD_DELAY = 0x0945
OVERFREQUENCY_RELOAD_START = 0x0946
OVERFREQUENCY_RELOAD_SPEED = 0x0947
UNDERFREQUENCY_START = 0x0948
UNDERFREQUENCY_END = 0x0949
UNDERFREQUENCY_SLOPE = 0x094A
UNDERFREQUENCY_RESPONSE_DELAY = 0x094B
UNDERFREQUENCY_RELOAD_DELAY = 0x094C
UNDERFREQUENCY_RELOAD_START = 0x094D
UNDERFREQUENCY_RELOAD_SPEED = 0x094E
FREQUENCY_RECOVER_MAX = 0x094F
FREQUENCY_RECOVER_MIN = 0x0950
ESS_OVERFREQUENCY_START = 0x0951
ESS_OVERFREQUENCY_END = 0x0952
ESS_OVERFREQUENCY_SLOPE = 0x0953
ESS_OVERFREQUENCY_RESPONSE_DELAY = 0x0954
ESS_OVERFREQUENCY_RELOAD_DELAY = 0x0955
ESS_OVERFREQUENCY_RELOAD_START = 0x0956
ESS_OVERFREQUENCY_RELOAD_SPEED = 0x0957
ESS_UNDERFREQUENCY_START = 0x0958
ESS_UNDERFREQUENCY_END = 0x0959
ESS_UNDERFREQUENCY_SLOPE = 0x095A
ESS_UNDERFREQUENCY_RESPONSE_DELAY = 0x095B
ESS_UNDERFREQUENCY_RELOAD_DELAY = 0x095C
ESS_UNDERFREQUENCY_RELOAD_START = 0x095D
ESS_UNDERFREQUENCY_RELOAD_SPEED = 0x095E
ESS_FREQUENCY_RECOVER_MAX = 0x095F
ESS_FREQUENCY_RECOVER_MIN = 0x0960
ESS_OVERFREQUENCY_TRANSITION = 0x0961
ESS_UNDERFREQUENCY_TRANSITION = 0x0962
# Reactive power Parameter (0x0980-0x09BF)
REACTIVE_CONFIG = 0x0980
POWER_FACTOR = 0x0981
FIXED_REACTIVE_PERCENTAGE = 0x0982
REACTIVE_COS1 = 0x0983
REACTIVE_DYNAMIC_VALUE1 = 0x0984
REACTIVE_COS2 = 0x0985
REACTIVE_DYNAMIC_VALUE2 = 0x0986
REACTIVE_COS3 = 0x0987
REACTIVE_DYNAMIC_VALUE3 = 0x0988
REACTIVE_COS4 = 0x0989
REACTIVE_DYNAMIC_VALUE4 = 0x098A
LOCKIN_V = 0x098B
LOCKOUT_V = 0x098C
HIGH_VOLT_START_VALUE4 = 0x098D
HIGH_VOLT_END_VALUE4 = 0x098E
LOW_VOLT_START_VALUE4 = 0x098F
LOW_VOLT_END_VALUE4 = 0x0990
LOCKIN_POWER4 = 0x0991
LOCKOUT_POWER4 = 0x0992
MAX_LEADING_REACTIVE_POWER4 = 0x0993
REACTIVE_RESPONSE_WAIT_TIME4 = 0x0994
REACTIVE_POWER_OFFSET4 = 0x0995
REACTIVE_POWER_START4 = 0x0996
HIGH_VOLT_START_VALUE5 = 0x0997
HIGH_VOLT_END_VALUE5 = 0x0998
LOW_VOLT_START_VALUE5 = 0x0999
LOW_VOLT_END_VALUE5 = 0x099A
LOCKIN_POWER5 = 0x099B
LOCKOUT_POWER5 = 0x099C
MAX_REACTIVE_POWER5 = 0x099D
REACTIVE_RESPONSE_WAIT_TIME5 = 0x099E
PHASE_TYPE = 0x099F
REACTIVE_RESPONSE_PERIOD = 0x09A0
MAX_LAGGING_REACTIVE_POWER4 = 0x09A1
# Voltage ride through Parameter (0x09C0-0x09FF)
VRT_CONFIG = 0x09C0
LVRT_IN_VOLT = 0x09C1
LVRT_FIRST_POINT_VOLT = 0x09C2
LVRT_FIRST_POINT_TIME = 0x09C3
LVRT_SECOND_POINT_VOLT = 0x09C4
LVRT_SECOND_POINT_TIME = 0x09C5
LVRT_THIRD_POINT_VOLT = 0x09C6
LVRT_THIRD_POINT_TIME = 0x09C7
LVRT_FOURTH_POINT_VOLT = 0x09C8
LVRT_FOURTH_POINT_TIME = 0x09C9
LVRT_REACTIVE_CURRENT_COEFFICIENT_K = 0x09CA
LVRT_WAITING_TIME_AFTER_VOLTAGE_RECOVERY = 0x09CB
LVRT_POWER_BACK_RATE = 0x09CC
OVRT_IN_VOLT = 0x09CD
OVRT_FIRST_POINT_VOLT = 0x09CE
OVRT_FIRST_POINT_TIME = 0x09CF
OVRT_SECOND_POINT_VOLT = 0x09D0
OVRT_SECOND_POINT_TIME = 0x09D1
OVRT_THIRD_POINT_VOLT = 0x09D2
OVRT_THIRD_POINT_TIME = 0x09D3
OVRT_FOURTH_POINT_VOLT = 0x09D4
OVRT_FOURTH_POINT_TIME = 0x09D5
OVRT_REACTIVE_CURRENT_COEFFICIENT_K = 0x09D6
OVRT_WAITING_TIME_AFTER_VOLTAGE_RECOVERY = 0x09D7
OVRT_POWER_BACK_RATE = 0x09D8
ZERO_CURRENT_MODE_IN_LOW_VOLT = 0x09D9
ZERO_CURRENT_MODE_IN_HIGH_VOLT = 0x09DA
LVRT_OUT_VOLT = 0x09DB
LVRT_IQ_VOLT_START = 0x09DC
OVRT_OUT_VOLT = 0x09DD
OVRT_IQ_VOLT_START = 0x09DE
# islanding、GFCI、ISO Parameter (0x0A00-0x0A3F)
ISLAND_CONFIG = 0x0A00
GFCI_CONFIG = 0x0A01
ISO_CONFIG = 0x0A02
INSULATION_PROTECTION_VALUE = 0x0A03
ISO_LEAKAGE_CURRENT_LIMIT = 0x0A04
GFCI_LIMIT = 0x0A05
# Basic Parameter Configuration (0x1000-0x10FF)
ADDRESS_MASK_CONFIG_BASIC1 = 0x1000
SYS_TIME_CONFIG_YEAR = 0x1004
SYS_TIME_CONFIG_MONTH = 0x1005
SYS_TIME_CONFIG_DATE = 0x1006
SYS_TIME_CONFIG_HOUR = 0x1007
SYS_TIME_CONFIG_MINUTE = 0x1008
SYS_TIME_CONFIG_SECOND = 0x1009
SYS_TIME_CONFIG_CONTROL = 0x100A
# Remote control (0x1100-0x12FF)
ADDRESS_MASK_CONFIG_REMOTE1 = 0x1100
REMOTE_ON_OFF_CONTROL = 0x1104
POWER_CONTROL = 0x1105
ACTIVE_POWER_EXPORT_LIMIT = 0x1106
ACTIVE_POWER_IMPORT_LIMIT = 0x1107
REACTIVE_POWER_SETTING = 0x1108
POWER_FACTOR_SETTING = 0x1109
ACTIVE_POWER_LIMIT_SPEED = 0x110A
REACTIVE_POWER_RESPONSE_TIME = 0x110B
ENERGY_STORAGE_MODE_CONTROL = 0x1110
TIMING_ID = 0x1111
TIMING_ON_OFF_CONTROL = 0x1112
TIMING_CHARGE_START = 0x1113
TIMING_CHARGE_END = 0x1114
TIMING_DISCHARGE_START = 0x1115
TIMING_DISCHARGE_END = 0x1116
TIMING_POWER_CHARGE = 0x1117
TIMING_POWER_DISCHARGE = 0x1119
TIMING_RSVD1 = 0x111B
TIMING_RSVD2 = 0x111C
TIMING_RSVD3 = 0x111D
TIMING_RSVD4 = 0x111E
TIMING_CONTROL = 0x111F
TOU_ID = 0x1120
TOU_ON_OFF_CONTROL = 0x1121
TOU_CHARGE_START = 0x1122
TOU_CHARGE_END = 0x1123
TOU_CHARGE_TARGET_SOC = 0x1124
TOU_CHARGE_POWER = 0x1125
TOU_EXECUTED_DATE_START = 0x1127
TOU_EXECUTED_DATE_END = 0x1128
TOU_EXECUTED_DAY_OF_WEEK = 0x1129
TOU_CONTROL = 0x112F
PEAK_SHAVING_DISCHARGE_THRESHOLD = 0x1130
PEAK_SHAVING_CHARGE_THRESHOLD = 0x1132

#mask addreses:
register_mask_list = [
    # ADDRESS_MASK_CONFIG_BASIC1,
    # ADDRESS_MASK_REALTIME_COMBINERINFO1,
    # ADDRESS_MASK_REALTIME_ELECTRICITY_STATISTICS1,
    # ADDRESS_MASK_REALTIME_INPUT_BAT2,
    # ADDRESS_MASK_REALTIME_INPUT_BAT1,
    # ADDRESS_MASK_REALTIME_INPUT_PV1,
    # ADDRESS_MASK_REALTIME_EMERGENCY_OUTPUT1,
    ADDRESS_MASK_REALTIME_GRID_OUTPUT1,
    ADDRESS_MASK_REALTIME_SYSINFO1,
]
register_map = {
    #----------System info (0x0400-0x047F)--------------#
    ADDRESS_MASK_REALTIME_SYSINFO1: {"description": "Address Mask for Realtime System Info 1", "unit": None, "sign": "U64", "multiplier": None, "bytes": 1},
    FAULT1: {"description": "Fault information table 1", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT2: {"description": "Fault information table 2", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT3: {"description": "Fault information table 3", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT4: {"description": "Fault information table 4", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT5: {"description": "Fault information table 5", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT6: {"description": "Fault information table 6", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT7: {"description": "Fault information table 7", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT8: {"description": "Fault information table 8", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT9: {"description": "Fault information table 9", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT10: {"description": "Fault information table 10", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT11: {"description": "Fault information table 11", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT12: {"description": "Fault information table 12", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT13: {"description": "Fault information table 13", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT14: {"description": "Fault information table 14", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT15: {"description": "Fault information table 15", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT16: {"description": "Fault information table 16", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT17: {"description": "Fault information table 17", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    FAULT18: {"description": "Fault information table 18", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    COUNTDOWN: {"description": "Power-on countdown", "unit": "seconds", "sign": "U16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_ENV1: {"description": "Ambient temperature 1", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_ENV2: {"description": "Ambient temperature 2", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_HEATSINK1: {"description": "Radiator temperature 1", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_HEATSINK2: {"description": "Radiator temperature 2", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_HEATSINK3: {"description": "Radiator temperature 3", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_HEATSINK4: {"description": "Radiator temperature 4", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_HEATSINK5: {"description": "Radiator temperature 5", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_HEATSINK6: {"description": "Radiator temperature 6", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_INV1: {"description": "Module temperature 1", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_INV2: {"description": "Module temperature 2", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMPERATURE_INV3: {"description": "Module temperature 3", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMP_RSV1: {"description": "Reserve temperature 1", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMP_RSV2: {"description": "Reserve temperature 2", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    TEMP_RSV3: {"description": "Reserve temperature 3", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    GENERATION_TIME_TODAY: {"description": "Day of power generation time", "unit": "Minute", "sign": "U32", "multiplier": "1", "bytes": 0},
    GENERATION_TIME_TOTAL: {"description": "Total power generation time", "unit": "Minute", "sign": "U32", "multiplier": "1", "bytes": 0},
    SERVICE_TIME_TOTAL: {"description": "Total running time", "unit": "Minute", "sign": "U16", "multiplier": "1", "bytes": 0},
    INSULATION_RESISTANCE: {"description": "Insulation resistance", "unit": "kΩ", "sign": "U16", "multiplier": "1", "bytes": 0},
    SYS_TIME_YEAR: {"description": "System time-year", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    SYS_TIME_MONTH: {"description": "System time-month", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    SYS_TIME_DATE: {"description": "System Time-Daily Minutes", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    SYS_TIME_HOUR: {"description": "System time-hour", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    SYS_TIME_MINUTE: {"description": "System time-minutes", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    SYS_TIME_SECOND: {"description": "System time-second", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    #------------------------On grid output (0x0480-0x04FF)---------------------------------#
    ADDRESS_MASK_REALTIME_GRID_OUTPUT1: {"description": "Address Mask for Realtime Grid Output 1", "unit": None, "sign": "U64", "multiplier": None, "bytes": 1},
    FREQUENCY_GRID: {"description": "Grid frequency", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_OUTPUT_TOTAL: {"description": "Total active power output", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_OUTPUT_TOTAL: {"description": "Total reactive power output", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    APPARENT_POWER_OUTPUT_TOTAL: {"description": "Total apparent power output", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_PCC_TOTAL: {"description": "Total PCC active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_PCC_TOTAL: {"description": "Total PCC reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    APPARENT_POWER_PCC_TOTAL: {"description": "Total PCC apparent power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    GRID_OUTPUT_RSVD1: {"description": "Grid-connected output reserved 1", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    GRID_OUTPUT_RSVD2: {"description": "Grid-connected output reserved 2", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    VOLTAGE_PHASE_R: {"description": "R phase grid voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_OUTPUT_R: {"description": "R-phase inverter output current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_OUTPUT_R: {"description": "R-phase inverter output active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_OUTPUT_R: {"description": "R-phase inverter output reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_FACTOR_OUTPUT_R: {"description": "R-phase power factor", "unit": "p.u.", "sign": "I16", "multiplier": "0.001", "bytes": 0},
    CURRENT_PCC_R: {"description": "R phase PCC current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_PCC_R: {"description": "R-phase PCC active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_PCC_R: {"description": "R-phase PCC reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_FACTOR_PCC_R: {"description": "R-phase PCC power factor", "unit": "p.u.", "sign": "I16", "multiplier": "0.001", "bytes": 0},
    R_RSVD1: {"description": "R phase reserved 1", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    R_RSVD2: {"description": "R phase reserved 2", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    VOLTAGE_PHASE_S: {"description": "S phase grid voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_OUTPUT_S: {"description": "S-phase inverter output current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_OUTPUT_S: {"description": "S-phase inverter outputs active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_OUTPUT_S: {"description": "S-phase inverter outputs reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_FACTOR_OUTPUT_S: {"description": "S-phase power factor", "unit": "p.u.", "sign": "I16", "multiplier": "0.001", "bytes": 0},
    CURRENT_PCC_S: {"description": "S phase PCC current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_PCC_S: {"description": "S-phase PCC active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_PCC_S: {"description": "S-phase PCC reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_FACTOR_PCC_S: {"description": "S-phase PCC power factor", "unit": "p.u.", "sign": "I16", "multiplier": "0.001", "bytes": 0},
    S_RSVD1: {"description": "S phase reserved 1", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    S_RSVD2: {"description": "S phase reserved 2", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    VOLTAGE_PHASE_T: {"description": "T phase grid voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_OUTPUT_T: {"description": "T-phase inverter output current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_OUTPUT_T: {"description": "T-phase inverter output active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_OUTPUT_T: {"description": "T-phase inverter output reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_FACTOR_OUTPUT_T: {"description": "T-phase power factor", "unit": "p.u.", "sign": "I16", "multiplier": "0.001", "bytes": 0},
    CURRENT_PCC_T: {"description": "T phase PCC current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_PCC_T: {"description": "T-phase PCC active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_PCC_T: {"description": "T-phase PCC reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_FACTOR_PCC_T: {"description": "T-phase PCC power factor", "unit": "p.u.", "sign": "I16", "multiplier": "0.001", "bytes": 0},
    T_RSVD1: {"description": "T phase reserved 1", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    T_RSVD2: {"description": "T phase reserved 2", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    ACTIVE_POWER_PV_EXT: {"description": "External power generation", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_LOAD_SYS: {"description": "System total load power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PHASE_L1N: {"description": "Grid L1 to N voltage effective value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_OUTPUT_L1N: {"description": "L1 output current effective value", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_OUTPUT_L1N: {"description": "Active power output on L1 line", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    CURRENT_PCC_L1N: {"description": "Effective value of CT current on L1 line", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_PCC_L1N: {"description": "PCC active power on L1 line", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PHASE_L2N: {"description": "Grid L2 to N voltage effective value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_OUTPUT_L2N: {"description": "L2 output current effective value", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_OUTPUT_L2N: {"description": "Active power output on L2 line", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    CURRENT_PCC_L2N: {"description": "Effective value of CT current on L2 line", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_PCC_L2N: {"description": "Active power output on L2 line", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_LINE_L1: {"description": "L1 line voltage: voltage between R/S phase", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    VOLTAGE_LINE_L2: {"description": "L2 line voltage: voltage between S/T phase", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    VOLTAGE_LINE_L3: {"description": "L3 line voltage: voltage between T/R phase", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    # --------------------Off grid output (0x0500-0x057F)--------------------------------#
    ADDRESS_MASK_REALTIME_EMERGENCY_OUTPUT1: {"description": "Address Mask for Realtime Emergency Output 1", "unit": None, "sign": "U64", "multiplier": None, "bytes": 1},
    ACTIVE_POWER_LOAD_TOTAL: {"description": "Load active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_LOAD_TOTAL: {"description": "Load reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    APPARENT_POWER_LOAD_TOTAL: {"description": "Load apparent power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    FREQUENCY_OUTPUT: {"description": "Output voltage frequency", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESOUTPUT_RSVD1: {"description": "Off-grid total output reserved 1", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    ESOUTPUT_RSVD2: {"description": "Off-grid total output reserved 2", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    VOLTAGE_OUTPUT_R: {"description": "R-phase inverter output voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_LOAD_R: {"description": "R phase load current", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_LOAD_R: {"description": "R-phase load active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_LOAD_R: {"description": "R-phase load reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    APPARENT_POWER_LOAD_R: {"description": "Apparent power of R-phase load", "unit": "kVA", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    LOAD_PEAK_RATIO_R: {"description": "R phase load peak ratio", "unit": "p.u.", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESR_RSVD1: {"description": "R phase reserved 1", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    ESR_RSVD2: {"description": "R phase reserved 2", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    VOLTAGE_OUTPUT_S: {"description": "S phase inverter output voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_LOAD_S: {"description": "S phase load current", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_LOAD_S: {"description": "S-phase load active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_LOAD_S: {"description": "S-phase load reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    APPARENT_POWER_LOAD_S: {"description": "Apparent power of S-phase load", "unit": "kVA", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    LOAD_PEAK_RATIO_S: {"description": "S phase load peak ratio", "unit": "p.u.", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_RSVD1: {"description": "S phase reserved 1", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    ESS_RSVD2: {"description": "S phase reserved 2", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    VOLTAGE_OUTPUT_T: {"description": "T-phase inverter output voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_LOAD_T: {"description": "T phase load current", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_LOAD_T: {"description": "T-phase load active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_LOAD_T: {"description": "T-phase load reactive power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    APPARENT_POWER_LOAD_T: {"description": "Apparent power of T-phase load", "unit": "kVA", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    LOAD_PEAK_RATIO_T: {"description": "T-phase load peak ratio", "unit": "p.u.", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    EST_RSVD1: {"description": "T phase reserved 1", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    EST_RSVD2: {"description": "T phase reserved 2", "unit": None, "sign": None, "multiplier": None, "bytes": 0},
    VOLTAGE_OUTPUT_L1N: {"description": "Inverter L1 to N voltage effective value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_LOAD_L1N: {"description": "L1 load current effective value", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_LOAD_L1N: {"description": "Load L1 to N active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_OUTPUT_L2N: {"description": "Effective value of inverter L2 to N voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_LOAD_L2N: {"description": "L2 load current effective value", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_LOAD_L2N: {"description": "Load L2 to N active power", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    #--------------------PV input (0x0580-0x05FF)--------------------------------#
    VOLTAGE_PV1: {"description": "The first PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV1: {"description": "The first PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV1: {"description": "PV power of the first road", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV2: {"description": "The second PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV2: {"description": "The second PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV2: {"description": "PV power of the 2nd road", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV3: {"description": "No. 3 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV3: {"description": "No. 3 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV3: {"description": "No. 3 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV4: {"description": "No. 4 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV4: {"description": "No. 4 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV4: {"description": "No. 4 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV5: {"description": "No. 5 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV5: {"description": "No. 5 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV5: {"description": "No. 5 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV6: {"description": "No. 6 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV6: {"description": "No. 6 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV6: {"description": "No. 6 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV7: {"description": "No. 7 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV7: {"description": "No. 7 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV7: {"description": "No. 7 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV8: {"description": "No. 8 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV8: {"description": "No. 8 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV8: {"description": "No. 8 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV9: {"description": "No. 9 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV9: {"description": "No. 9 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV9: {"description": "No. 9 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV10: {"description": "No. 10 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV10: {"description": "No. 10 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV10: {"description": "No. 10 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV11: {"description": "11th PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV11: {"description": "11th PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV11: {"description": "11th PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV12: {"description": "12th PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV12: {"description": "12th PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV12: {"description": "12th PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV13: {"description": "13th PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV13: {"description": "13th PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV13: {"description": "13th PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV14: {"description": "No. 14 PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV14: {"description": "No. 14 PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV14: {"description": "No. 14 PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV15: {"description": "15th PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV15: {"description": "15th PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV15: {"description": "15th PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_PV16: {"description": "16th PV voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_PV16: {"description": "16th PV current", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    POWER_PV16: {"description": "16th PV power", "unit": "kW", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    #--------------------Battery input (0x0600-0x067F)--------------------------------#
    ADDRESS_MASK_REALTIME_INPUT_BAT1: {"description": "Address Mask Realtime Input Bat1", "unit": None, "sign": "U64", "multiplier": None, "bytes": 1},
    VOLTAGE_BAT1: {"description": "Voltage Bat1", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT1: {"description": "Current Bat1", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT1: {"description": "Power Bat1", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT1: {"description": "Temperature Env Bat1", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT1: {"description": "SOC Bat1", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT1: {"description": "SOH Bat1", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT1: {"description": "ChargeCycle Bat1", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT2: {"description": "Voltage Bat2", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT2: {"description": "Current Bat2", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT2: {"description": "Power Bat2", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT2: {"description": "Temperature Env Bat2", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT2: {"description": "SOC Bat2", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT2: {"description": "SOH Bat2", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT2: {"description": "ChargeCycle Bat2", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT3: {"description": "Voltage Bat3", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT3: {"description": "Current Bat3", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT3: {"description": "Power Bat3", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT3: {"description": "Temperature Env Bat3", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT3: {"description": "SOC Bat3", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT3: {"description": "SOH Bat3", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT3: {"description": "ChargeCycle Bat3", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT4: {"description": "Voltage Bat4", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT4: {"description": "Current Bat4", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT4: {"description": "Power Bat4", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT4: {"description": "Temperature Env Bat4", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT4: {"description": "SOC Bat4", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT4: {"description": "SOH Bat4", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT4: {"description": "ChargeCycle Bat4", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT5: {"description": "Voltage Bat5", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT5: {"description": "Current Bat5", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT5: {"description": "Power Bat5", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT5: {"description": "Temperature Env Bat5", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT5: {"description": "SOC Bat5", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT5: {"description": "SOH Bat5", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT5: {"description": "ChargeCycle Bat5", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT6: {"description": "Voltage Bat6", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT6: {"description": "Current Bat6", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT6: {"description": "Power Bat6", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT6: {"description": "Temperature Env Bat6", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT6: {"description": "SOC Bat6", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT6: {"description": "SOH Bat6", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT6: {"description": "ChargeCycle Bat6", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT7: {"description": "Voltage Bat7", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT7: {"description": "Current Bat7", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT7: {"description": "Power Bat7", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT7: {"description": "Temperature Env Bat7", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT7: {"description": "SOC Bat7", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT7: {"description": "SOH Bat7", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT7: {"description": "ChargeCycle Bat7", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT8: {"description": "Voltage Bat8", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT8: {"description": "Current Bat8", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT8: {"description": "Power Bat8", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT8: {"description": "Temperature Env Bat8", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT8: {"description": "SOC Bat8", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT8: {"description": "SOH Bat8", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT8: {"description": "ChargeCycle Bat8", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    ADDRESS_MASK_REALTIME_INPUT_BAT2: {"description": "AddressMask Realtime Input Bat2", "unit": "Uint", "sign": "U64", "multiplier": None, "bytes": 0},
    VOLTAGE_BAT9: {"description": "Voltage Bat9", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT9: {"description": "Current Bat9", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT9: {"description": "Power Bat9", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT9: {"description": "Temperature Env Bat9", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT9: {"description": "SOC Bat9", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT9: {"description": "SOH Bat9", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT9: {"description": "ChargeCycle Bat9", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT10: {"description": "Voltage Bat10", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT10: {"description": "Current Bat10", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT10: {"description": "Power Bat10", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT10: {"description": "Temperature Env Bat10", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT10: {"description": "SOC Bat10", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT10: {"description": "SOH Bat10", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT10: {"description": "ChargeCycle Bat10", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT11: {"description": "Voltage Bat11", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT11: {"description": "Current Bat11", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT11: {"description": "Power Bat11", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT11: {"description": "Temperature Env Bat11", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT11: {"description": "SOC Bat11", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT11: {"description": "SOH Bat11", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT11: {"description": "ChargeCycle Bat11", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_BAT12: {"description": "Voltage Bat12", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_BAT12: {"description": "Current Bat12", "unit": "A", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    POWER_BAT12: {"description": "Power Bat12", "unit": "kW", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    TEMPERATURE_ENV_BAT12: {"description": "Temperature Env Bat12", "unit": "℃", "sign": "I16", "multiplier": "1", "bytes": 0},
    SOC_BAT12: {"description": "SOC Bat12", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT12: {"description": "SOH Bat12", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHARGE_CYCLE_BAT12: {"description": "ChargeCycle Bat12", "unit": "cycle", "sign": "U16", "multiplier": "1", "bytes": 0},
    POWER_BAT_TOTAL: {"description": "Power Bat Total", "unit": "kW", "sign": "I16", "multiplier": "0.1", "bytes": 0},
    SOC_BAT_AVERAGE: {"description": "SOC Bat Average", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    SOH_BAT: {"description": "SOH Bat", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    #--------------------Power (0x0680-0x06BF)--------------------------------#
    ADDRESS_MASK_REALTIME_ELECTRICITY_STATISTICS1: {"description": "AddressMask Realtime Electricity Statistics1", "unit": "Uint", "sign": "U64", "multiplier": None, "bytes": 1},
    PV_GENERATION_TODAY: {"description": "PV Generation Today", "unit": "kWh", "sign": "U32", "multiplier": "0.01", "bytes": 0},
    PV_GENERATION_TOTAL: {"description": "PV Generation Total", "unit": "kWh", "sign": "U32", "multiplier": "0.1", "bytes": 0},
    LOAD_CONSUMPTION_TODAY: {"description": "Load Consumption Today", "unit": "kWh", "sign": "U32", "multiplier": "0.01", "bytes": 0},
    LOAD_CONSUMPTION_TOTAL: {"description": "Load Consumption Total", "unit": "kWh", "sign": "U32", "multiplier": "0.1", "bytes": 0},
    ENERGY_PURCHASE_TODAY: {"description": "Energy Purchase Today", "unit": "kWh", "sign": "U32", "multiplier": "0.01", "bytes": 0},
    ENERGY_PURCHASE_TOTAL: {"description": "Energy Purchase Total", "unit": "kWh", "sign": "U32", "multiplier": "0.1", "bytes": 0},
    ENERGY_SELLING_TODAY: {"description": "Energy Selling Today", "unit": "kWh", "sign": "U32", "multiplier": "0.01", "bytes": 0},
    ENERGY_SELLING_TOTAL: {"description": "Energy Selling Total", "unit": "kWh", "sign": "U32", "multiplier": "0.1", "bytes": 0},
    BAT_CHARGE_TODAY: {"description": "Battery Charge Today", "unit": "kWh", "sign": "U32", "multiplier": "0.01", "bytes": 0},
    BAT_CHARGE_TOTAL: {"description": "Battery Charge Total", "unit": "kWh", "sign": "U32", "multiplier": "0.1", "bytes": 0},
    BAT_DISCHARGE_TODAY: {"description": "Battery Discharge Today", "unit": "kWh", "sign": "U32", "multiplier": "0.01", "bytes": 0},
    BAT_DISCHARGE_TOTAL: {"description": "Battery Discharge Total", "unit": "kWh", "sign": "U32", "multiplier": "0.1", "bytes": 0},
    # --------------------Internal info (0x06C0-0x06FF)--------------------------------#
    # FOR INSTALATOR#
    # --------------------Combined info (0x0700-0x077F)--------------------------------#
    ADDRESS_MASK_REALTIME_COMBINERINFO1: {"description": "AddressMask Realtime CombinerInfo1", "unit": "Uint", "sign": "U64", "multiplier": None, "bytes": 1},
    VOLTAGE_GROUP1: {"description": "Voltage Group 1", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP1_BRANCH1: {"description": "Current Group 1 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP1_BRANCH2: {"description": "Current Group 1 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP2: {"description": "Voltage Group 2", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP2_BRANCH1: {"description": "Current Group 2 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP2_BRANCH2: {"description": "Current Group 2 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP3: {"description": "Voltage Group 3", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP3_BRANCH1: {"description": "Current Group 3 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP3_BRANCH2: {"description": "Current Group 3 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP4: {"description": "Voltage Group 4", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP4_BRANCH1: {"description": "Current Group 4 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP4_BRANCH2: {"description": "Current Group 4 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP5: {"description": "Voltage Group 5", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP5_BRANCH1: {"description": "Current Group 5 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP5_BRANCH2: {"description": "Current Group 5 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP6: {"description": "Voltage Group 6", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP6_BRANCH1: {"description": "Current Group 6 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP6_BRANCH2: {"description": "Current Group 6 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP7: {"description": "Voltage Group 7", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP7_BRANCH1: {"description": "Current Group 7 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP7_BRANCH2: {"description": "Current Group 7 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP8: {"description": "Voltage Group 8", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP8_BRANCH1: {"description": "Current Group 8 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP8_BRANCH2: {"description": "Current Group 8 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP9: {"description": "Voltage Group 9", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP9_BRANCH1: {"description": "Current Group 9 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP9_BRANCH2: {"description": "Current Group 9 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP10: {"description": "Voltage Group 10", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP10_BRANCH1: {"description": "Current Group 10 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP10_BRANCH2: {"description": "Current Group 10 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP11: {"description": "Voltage Group 11", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP11_BRANCH1: {"description": "Current Group 11 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP11_BRANCH2: {"description": "Current Group 11 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP12: {"description": "Voltage Group 12", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP12_BRANCH1: {"description": "Current Group 12 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP12_BRANCH2: {"description": "Current Group 12 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP13: {"description": "Voltage Group 13", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP13_BRANCH1: {"description": "Current Group 13 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP13_BRANCH2: {"description": "Current Group 13 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP14: {"description": "Voltage Group 14", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP14_BRANCH1: {"description": "Current Group 14 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP14_BRANCH2: {"description": "Current Group 14 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP15: {"description": "Voltage Group 15", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP15_BRANCH1: {"description": "Current Group 15 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP15_BRANCH2: {"description": "Current Group 15 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    VOLTAGE_GROUP16: {"description": "Voltage Group 16", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CURRENT_GROUP16_BRANCH1: {"description": "Current Group 16 Branch 1", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    CURRENT_GROUP16_BRANCH2: {"description": "Current Group 16 Branch 2", "unit": "A", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    # --------------------Arcing information (0x0780-0x07BF)--------------------------------#
    # SKIP
    #========= ========= ========= Safety Parameter Area(0x0800-0x0FFF) ========= ========= =========#
    # --------------------Boot Parameters (0x0800-0x083F)--------------------------------#
    CONNECT_WAIT_TIME: {"description": "Connect Wait Time", "unit": "Second", "sign": "U16", "multiplier": "1", "bytes": 0},
    POWER_UP_SPEED: {"description": "Power Up Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    RECONNECT_WAIT_TIME: {"description": "Reconnect Wait Time", "unit": "Second", "sign": "U16", "multiplier": "1", "bytes": 0},
    RECONNECT_POWER_UP_SPEED: {"description": "Reconnect Power Up Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLT_HIGH_LIMIT: {"description": "Voltage High Limit (Grid Side)", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    VOLT_LOW_LIMIT: {"description": "Voltage Low Limit (Grid Side)", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    FREQ_HIGH_LIMIT: {"description": "Frequency High Limit (Grid Side)", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    FREQ_LOW_LIMIT: {"description": "Frequency Low Limit (Grid Side)", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    RECONNECT_VOLT_HIGH_LIMIT: {"description": "Reconnect Voltage High Limit", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    RECONNECT_VOLT_LOW_LIMIT: {"description": "Reconnect Voltage Low Limit", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    RECONNECT_FREQ_HIGH_LIMIT: {"description": "Reconnect Frequency High Limit", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    RECONNECT_FREQ_LOW_LIMIT: {"description": "Reconnect Frequency Low Limit", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    # --------------------Grid voltage protection Parameters (0x0840-0x087F)--------------------------------#
    VOLTAGE_CONFIG: {"description": "Voltage Configuration", "unit": None, "sign": "U16", "multiplier": None, "bytes": 1},
    RATED_VOLTAGE: {"description": "Rated Voltage", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    FIRST_OVERVOLTAGE_PROTECTION_VALUE: {"description": "First Overvoltage Protection Value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    FIRST_OVERVOLTAGE_PROTECTION_TIME: {"description": "First Overvoltage Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    SECOND_OVERVOLTAGE_PROTECTION_VALUE: {"description": "Second Overvoltage Protection Value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    SECOND_OVERVOLTAGE_PROTECTION_TIME: {"description": "Second Overvoltage Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    THIRD_OVERVOLTAGE_PROTECTION_VALUE: {"description": "Third Overvoltage Protection Value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    THIRD_OVERVOLTAGE_PROTECTION_TIME: {"description": "Third Overvoltage Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    FIRST_UNDERVOLTAGE_PROTECTION_VALUE: {"description": "First Undervoltage Protection Value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    FIRST_UNDERVOLTAGE_PROTECTION_TIME: {"description": "First Undervoltage Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    SECOND_UNDERVOLTAGE_PROTECTION_VALUE: {"description": "Second Undervoltage Protection Value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    SECOND_UNDERVOLTAGE_PROTECTION_TIME: {"description": "Second Undervoltage Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    THIRD_UNDERVOLTAGE_PROTECTION_VALUE: {"description": "Third Undervoltage Protection Value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    THIRD_UNDERVOLTAGE_PROTECTION_TIME: {"description": "Third Undervoltage Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    TEN_MIN_OVERVOLTAGE_PROTECTION_VALUE: {"description": "10-Min Overvoltage Protection Value", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    # --------------------Frquency Protection Parameter (0x0880-0x08BF)--------------------------------#
    FREQUENCY_CONFIG: {"description": "Frequency Configuration", "unit": None, "sign": "U16", "multiplier": None, "bytes": 1},
    RATED_FREQUENCY: {"description": "Rated Frequency", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    FIRST_OVERFREQUENCY_PROTECTION_VALUE: {"description": "First Overfrequency Protection Value", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    FIRST_OVERFREQUENCY_PROTECTION_TIME: {"description": "First Overfrequency Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    SECOND_OVERFREQUENCY_PROTECTION_VALUE: {"description": "Second Overfrequency Protection Value", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    SECOND_OVERFREQUENCY_PROTECTION_TIME: {"description": "Second Overfrequency Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    THIRD_OVERFREQUENCY_PROTECTION_VALUE: {"description": "Third Overfrequency Protection Value", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    THIRD_OVERFREQUENCY_PROTECTION_TIME: {"description": "Third Overfrequency Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    FIRST_UNDERFREQUENCY_PROTECTION_VALUE: {"description": "First Underfrequency Protection Value", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    FIRST_UNDERFREQUENCY_PROTECTION_TIME: {"description": "First Underfrequency Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    SECOND_UNDERFREQUENCY_PROTECTION_VALUE: {"description": "Second Underfrequency Protection Value", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    SECOND_UNDERFREQUENCY_PROTECTION_TIME: {"description": "Second Underfrequency Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    THIRD_UNDERFREQUENCY_PROTECTION_VALUE: {"description": "Third Underfrequency Protection Value", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    THIRD_UNDERFREQUENCY_PROTECTION_TIME: {"description": "Third Underfrequency Protection Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    # --------------------DCIProtection Parameter (0x08C0-0x08FF)--------------------------------#
    # skip
    # --------------------active power &Over/Under voltage Power Derate  Paramter (0x0900-0x093F)--------------------------------#
    # skip
# --------------------active power &Over/Under voltage Power Derate  Paramter (0x0900-0x093F)--------------------------------#
    REMOTE_CONFIG: {"description": "Remote Configuration", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    ACTIVE_OUTPUT_LIMIT: {"description": "Active Output Limit", "unit": "%", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    ACTIVE_OUTPUT_DOWN_SPEED: {"description": "Active Output Down Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    GRID_VOLTAGE_DROP_START: {"description": "Grid Voltage Drop Start", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    GRID_VOLTAGE_DROP_STOP: {"description": "Grid Voltage Drop Stop", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    GRID_VOLTAGE_DROP_MIN_POWER: {"description": "Grid Voltage Drop Min Power", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    OVERVOLTAGE_DOWN_SPEED: {"description": "Overvoltage Down Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    CHG_DERATE_VOLT_START: {"description": "Charging Derate Voltage Start", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CHG_DERATE_VOLT_END: {"description": "Charging Derate Voltage End", "unit": "V", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    CHG_DERATE_MIN_POWER: {"description": "Charging Derate Min Power", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    POWER_FOR_LOGIC_1: {"description": "Power for Logic 1", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    POWER_FOR_LOGIC_2: {"description": "Power for Logic 2", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    POWER_FOR_LOGIC_3: {"description": "Power for Logic 3", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    POWER_FOR_LOGIC_4: {"description": "Power for Logic 4", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    POWER_FOR_LOGIC_5: {"description": "Power for Logic 5", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    POWER_FOR_LOGIC_6: {"description": "Power for Logic 6", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    POWER_FOR_LOGIC_7: {"description": "Power for Logic 7", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    POWER_FOR_LOGIC_8: {"description": "Power for Logic 8", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    REFLUX_POWER: {"description": "Reflux Power", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    REFLUX_OV_LOAD_TIME: {"description": "Reflux Overload Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    LOGIC_DERATE_SPEED: {"description": "Logic Derate Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOGIC_RELOAD_SPEED: {"description": "Logic Reload Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    VOLTAGE_DERATE_RESPONSE_TIME: {"description": "Voltage Derate Response Time", "unit": "Second", "sign": "U16", "multiplier": "1", "bytes": 0},
    # --------------------Over/Under Frquency Power Derate (0x0940-0x097F)--------------------------------#
    FREQUENCY_DERATE_CONFIG: {"description": "Frequency Derate Configuration", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    OVERFREQUENCY_START: {"description": "Overfrequency Start", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    OVERFREQUENCY_END: {"description": "Overfrequency End", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    OVERFREQUENCY_SLOPE: {"description": "Overfrequency Slope", "unit": "%Pn/Hz", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVERFREQUENCY_RESPONSE_DELAY: {"description": "Overfrequency Response Delay", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    OVERFREQUENCY_RELOAD_DELAY: {"description": "Overfrequency Reload Delay", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    OVERFREQUENCY_RELOAD_START: {"description": "Overfrequency Reload Start", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    OVERFREQUENCY_RELOAD_SPEED: {"description": "Overfrequency Reload Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    UNDERFREQUENCY_START: {"description": "Underfrequency Start", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    UNDERFREQUENCY_END: {"description": "Underfrequency End", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    UNDERFREQUENCY_SLOPE: {"description": "Underfrequency Slope", "unit": "%Pn/Hz", "sign": "U16", "multiplier": "1", "bytes": 0},
    UNDERFREQUENCY_RESPONSE_DELAY: {"description": "Underfrequency Response Delay", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    UNDERFREQUENCY_RELOAD_DELAY: {"description": "Underfrequency Reload Delay", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    UNDERFREQUENCY_RELOAD_START: {"description": "Underfrequency Reload Start", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    UNDERFREQUENCY_RELOAD_SPEED: {"description": "Underfrequency Reload Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    FREQUENCY_RECOVER_MAX: {"description": "Frequency Recover Max", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    FREQUENCY_RECOVER_MIN: {"description": "Frequency Recover Min", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_OVERFREQUENCY_START: {"description": "(Energy storage) Overfrequency Start", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_OVERFREQUENCY_END: {"description": "(Energy storage) Overfrequency End", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_OVERFREQUENCY_SLOPE: {"description": "(Energy storage) Overfrequency Slope", "unit": "%Pn/Hz", "sign": "U16", "multiplier": "1", "bytes": 0},
    ESS_OVERFREQUENCY_RESPONSE_DELAY: {"description": "(Energy storage) Overfrequency Response Delay", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    ESS_OVERFREQUENCY_RELOAD_DELAY: {"description": "(Energy storage) Overfrequency Reload Delay", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    ESS_OVERFREQUENCY_RELOAD_START: {"description": "(Energy storage) Overfrequency Reload Start", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_OVERFREQUENCY_RELOAD_SPEED: {"description": "(Energy storage) Overfrequency Reload Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    ESS_UNDERFREQUENCY_START: {"description": "(Energy storage) Underfrequency Start", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_UNDERFREQUENCY_END: {"description": "(Energy storage) Underfrequency End", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_UNDERFREQUENCY_SLOPE: {"description": "(Energy storage) Underfrequency Slope", "unit": "%Pn/Hz", "sign": "U16", "multiplier": "1", "bytes": 0},
    ESS_UNDERFREQUENCY_RESPONSE_DELAY: {"description": "(Energy storage) Underfrequency Response Delay", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    ESS_UNDERFREQUENCY_RELOAD_DELAY: {"description": "(Energy storage) Underfrequency Reload Delay", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    ESS_UNDERFREQUENCY_RELOAD_START: {"description": "(Energy storage) Underfrequency Reload Start", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_UNDERFREQUENCY_RELOAD_SPEED: {"description": "(Energy storage) Underfrequency Reload Speed", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    ESS_FREQUENCY_RECOVER_MAX: {"description": "(Energy storage) Frequency Recover Max", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_FREQUENCY_RECOVER_MIN: {"description": "(Energy storage) Frequency Recover Min", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_OVERFREQUENCY_TRANSITION: {"description": "(Energy storage) Overfrequency Transition", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    ESS_UNDERFREQUENCY_TRANSITION: {"description": "(Energy storage) Underfrequency Transition", "unit": "Hz", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    # --------------------Reactive power Parameter (0x0980-0x09BF)--------------------------------#
    REACTIVE_CONFIG: {"description": "Reactive Config", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    POWER_FACTOR: {"description": "Power Factor", "unit": None, "sign": "I16", "multiplier": "0.0001", "bytes": 0},
    FIXED_REACTIVE_PERCENTAGE: {"description": "Fixed Reactive Percentage", "unit": "%", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_COS1: {"description": "Reactive Cos1", "unit": None, "sign": "I16", "multiplier": "0.0001", "bytes": 0},
    REACTIVE_DYNAMIC_VALUE1: {"description": "Reactive Dynamic Value1", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    REACTIVE_COS2: {"description": "Reactive Cos2", "unit": None, "sign": "I16", "multiplier": "0.0001", "bytes": 0},
    REACTIVE_DYNAMIC_VALUE2: {"description": "Reactive Dynamic Value2", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    REACTIVE_COS3: {"description": "Reactive Cos3", "unit": None, "sign": "I16", "multiplier": "0.0001", "bytes": 0},
    REACTIVE_DYNAMIC_VALUE3: {"description": "Reactive Dynamic Value3", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    REACTIVE_COS4: {"description": "Reactive Cos4", "unit": None, "sign": "I16", "multiplier": "0.0001", "bytes": 0},
    REACTIVE_DYNAMIC_VALUE4: {"description": "Reactive Dynamic Value4", "unit": "%", "sign": "I16", "multiplier": "1", "bytes": 0},
    LOCKIN_V: {"description": "Lockin V", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOCKOUT_V: {"description": "Lockout V", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    HIGH_VOLT_START_VALUE4: {"description": "High Volt Start Value 4", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    HIGH_VOLT_END_VALUE4: {"description": "High Volt End Value 4", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOW_VOLT_START_VALUE4: {"description": "Low Volt Start Value 4", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOW_VOLT_END_VALUE4: {"description": "Low Volt End Value 4", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOCKIN_POWER4: {"description": "Lockin Power 4", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOCKOUT_POWER4: {"description": "Lockout Power 4", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    MAX_LEADING_REACTIVE_POWER4: {"description": "Max Leading Reactive Power 4", "unit": "%", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_RESPONSE_WAIT_TIME4: {"description": "Reactive Response Wait Time 4", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    REACTIVE_POWER_OFFSET4: {"description": "Reactive Power Offset 4", "unit": "%Qmax", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_POWER_START4: {"description": "Reactive Power Start 4", "unit": "%Pn", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    HIGH_VOLT_START_VALUE5: {"description": "High Volt Start Value 5", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    HIGH_VOLT_END_VALUE5: {"description": "High Volt End Value 5", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOW_VOLT_START_VALUE5: {"description": "Low Volt Start Value 5", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOW_VOLT_END_VALUE5: {"description": "Low Volt End Value 5", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOCKIN_POWER5: {"description": "Lockin Power 5", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LOCKOUT_POWER5: {"description": "Lockout Power 5", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    MAX_REACTIVE_POWER5: {"description": "Max Reactive Power 5", "unit": "%", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    REACTIVE_RESPONSE_WAIT_TIME5: {"description": "Reactive Response Wait Time 5", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    PHASE_TYPE: {"description": "Phase Type", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    REACTIVE_RESPONSE_PERIOD: {"description": "Reactive Response Period", "unit": "Second", "sign": "U16", "multiplier": "1", "bytes": 0},
    MAX_LAGGING_REACTIVE_POWER4: {"description": "Max Lagging Reactive Power 4", "unit": "%Pn", "sign": "U16", "multiplier": "0.01", "bytes": 0},
    # --------------------Voltage ride through Parameter (0x09C0-0x09FF)--------------------------------#
    VRT_CONFIG: {"description": "VRT Config", "unit": None, "sign": "U16", "multiplier": None, "bytes": 0},
    LVRT_IN_VOLT: {"description": "Lvrt In Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_FIRST_POINT_VOLT: {"description": "Lvrt First Point Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_FIRST_POINT_TIME: {"description": "Lvrt First Point Time", "unit": "ms", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_SECOND_POINT_VOLT: {"description": "Lvrt Second Point Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_SECOND_POINT_TIME: {"description": "Lvrt Second Point Time", "unit": "ms", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_THIRD_POINT_VOLT: {"description": "Lvrt Third Point Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_THIRD_POINT_TIME: {"description": "Lvrt Third Point Time", "unit": "ms", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_FOURTH_POINT_VOLT: {"description": "Lvrt Fourth Point Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_FOURTH_POINT_TIME: {"description": "Lvrt Fourth Point Time", "unit": "ms", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_REACTIVE_CURRENT_COEFFICIENT_K: {"description": "Lvrt Reactive Current Coefficient K", "unit": "p.u.", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    LVRT_WAITING_TIME_AFTER_VOLTAGE_RECOVERY: {"description": "Lvrt Waiting Time After Voltage Recovery", "unit": "ms", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_POWER_BACK_RATE: {"description": "Lvrt Power Back Rate", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_IN_VOLT: {"description": "OVRT In Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_FIRST_POINT_VOLT: {"description": "OVRT First Point Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_FIRST_POINT_TIME: {"description": "OVRT First Point Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    OVRT_SECOND_POINT_VOLT: {"description": "OVRT Second Point Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_SECOND_POINT_TIME: {"description": "OVRT Second Point Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    OVRT_THIRD_POINT_VOLT: {"description": "OVRT Third Point Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_THIRD_POINT_TIME: {"description": "OVRT Third Point Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    OVRT_FOURTH_POINT_VOLT: {"description": "OVRT Fourth Point Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_FOURTH_POINT_TIME: {"description": "OVRT Fourth Point Time", "unit": "ms", "sign": "U16", "multiplier": "10", "bytes": 0},
    OVRT_REACTIVE_CURRENT_COEFFICIENT_K: {"description": "OVRT Reactive Current Coefficient K", "unit": "p.u.", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    OVRT_WAITING_TIME_AFTER_VOLTAGE_RECOVERY: {"description": "OVRT Waiting Time After Voltage Recovery", "unit": "ms", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_POWER_BACK_RATE: {"description": "OVRT Power Back Rate", "unit": "%Pn/min", "sign": "U16", "multiplier": "1", "bytes": 0},
    ZERO_CURRENT_MODE_IN_LOW_VOLT: {"description": "Zero Current Mode In Low Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    ZERO_CURRENT_MODE_IN_HIGH_VOLT: {"description": "Zero Current Mode In High Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_OUT_VOLT: {"description": "LVRT Out Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    LVRT_IQ_VOLT_START: {"description": "LVRT Iq Volt Start", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_OUT_VOLT: {"description": "OVRT Out Volt", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    OVRT_IQ_VOLT_START: {"description": "OVRT Iq Volt Start", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 0},
    # --------------------islanding、GFCI、ISO Parameter (0x0A00-0x0A3F)--------------------------------#
    ISLAND_CONFIG: {"description": "Island Config", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    GFCI_CONFIG: {"description": "GFCI Config", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    ISO_CONFIG: {"description": "ISO Config", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    INSULATION_PROTECTION_VALUE: {"description": "Insulation Protection Value", "unit": "kΩ", "sign": "U16", "multiplier": "1", "bytes": 0},
    ISO_LEAKAGE_CURRENT_LIMIT: {"description": "ISO Leakage Current Limit", "unit": "mA", "sign": "U16", "multiplier": "1", "bytes": 0},
    GFCI_LIMIT: {"description": "GFCI Limit", "unit": "mA/kVA", "sign": "U16", "multiplier": "1", "bytes": 0},

    #========= ========= ========= Paranters setting (0x1000-0x17FF) ========= ========= =========#

    # --------------------Basic Parameter Configuration (0x1000-0x10FF)--------------------------------#
    ADDRESS_MASK_CONFIG_BASIC1: {"description": "Address Mask Config Basic 1", "unit": "", "sign": "U64", "multiplier": "", "bytes": 0},
    SYS_TIME_CONFIG_YEAR: {"description": "System Time Config Year", "unit": "Year", "sign": "U16", "multiplier": "", "bytes": 0},
    SYS_TIME_CONFIG_MONTH: {"description": "System Time Config Month", "unit": "Month", "sign": "U16", "multiplier": "", "bytes": 0},
    SYS_TIME_CONFIG_DATE: {"description": "System Time Config Date", "unit": "date", "sign": "U16", "multiplier": "", "bytes": 0},
    SYS_TIME_CONFIG_HOUR: {"description": "System Time Config Hour", "unit": "Hour", "sign": "U16", "multiplier": "", "bytes": 0},
    SYS_TIME_CONFIG_MINUTE: {"description": "System Time Config Minute", "unit": "Minute", "sign": "U16", "multiplier": "", "bytes": 0},
    SYS_TIME_CONFIG_SECOND: {"description": "System Time Config Second", "unit": "Second", "sign": "U16", "multiplier": "", "bytes": 0},
    SYS_TIME_CONFIG_CONTROL: {"description": "System Time Config Control", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    # --------------------Remote control (0x1100-0x12FF)--------------------------------#
    ADDRESS_MASK_CONFIG_REMOTE1: {"description": "Address Mask Config Remote 1", "unit": "", "sign": "U64", "multiplier": "", "bytes": 0},
    REMOTE_ON_OFF_CONTROL: {"description": "Remote On/Off Control", "unit": "", "sign": "U16", "multiplier": "", "bytes": 'low'},
    POWER_CONTROL: {"description": "Power Control", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    ACTIVE_POWER_EXPORT_LIMIT: {"description": "Active Power Export Limit", "unit": "%", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    ACTIVE_POWER_IMPORT_LIMIT: {"description": "Active Power Import Limit", "unit": "%", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    REACTIVE_POWER_SETTING: {"description": "Reactive Power Setting", "unit": "%", "sign": "I16", "multiplier": "0.1", "bytes": 0},
    POWER_FACTOR_SETTING: {"description": "Power Factor Setting", "unit": "p.u.", "sign": "I16", "multiplier": "0.01", "bytes": 0},
    ACTIVE_POWER_LIMIT_SPEED: {"description": "Active Power Limit Speed", "unit": "%", "sign": "U16", "multiplier": "", "bytes": 0},
    REACTIVE_POWER_RESPONSE_TIME: {"description": "Reactive Power Response Time", "unit": "second", "sign": "U16", "multiplier": "0.1", "bytes": 0},
    ENERGY_STORAGE_MODE_CONTROL: {"description": "Energy Storage Mode Control", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    TIMING_ID: {"description": "Timing ID", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    TIMING_ON_OFF_CONTROL: {"description": "Timing On/Off Control", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    TIMING_CHARGE_START: {"description": "Timing Charge Start", "unit": "Hour/Minute", "sign": "U16", "multiplier": "1", "bytes": 1},
    TIMING_CHARGE_END: {"description": "Timing Charge End", "unit": "Hour/Minute", "sign": "U16", "multiplier": "1", "bytes": 1},
    TIMING_DISCHARGE_START: {"description": "Timing Discharge Start", "unit": "Hour/Minute", "sign": "U16", "multiplier": "1", "bytes": 1},
    TIMING_DISCHARGE_END: {"description": "Timing Discharge End", "unit": "Hour/Minute", "sign": "U16", "multiplier": "1", "bytes": 1},
    TIMING_POWER_CHARGE: {"description": "Timing Power Charge", "unit": "", "sign": "U32", "multiplier": "1", "bytes": 1},
    TIMING_POWER_DISCHARGE: {"description": "Timing Power Discharge", "unit": "", "sign": "U32", "multiplier": "1", "bytes": 1},
    TIMING_RSVD1: {"description": "Timing Reserved 1", "unit": "", "sign": "", "multiplier": "", "bytes": 0},
    TIMING_RSVD2: {"description": "Timing Reserved 2", "unit": "", "sign": "", "multiplier": "", "bytes": 0},
    TIMING_RSVD3: {"description": "Timing Reserved 3", "unit": "", "sign": "", "multiplier": "", "bytes": 0},
    TIMING_RSVD4: {"description": "Timing Reserved 4", "unit": "", "sign": "", "multiplier": "", "bytes": 0},
    TIMING_CONTROL: {"description": "Timing Control", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    TOU_ID: {"description": "TOU ID", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    TOU_ON_OFF_CONTROL: {"description": "TOU On/Off Control", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    TOU_CHARGE_START: {"description": "TOU Charge Start", "unit": "Hour/Minute", "sign": "U16", "multiplier": "1", "bytes": 1},
    TOU_CHARGE_END: {"description": "TOU Charge End", "unit": "Hour/Minute", "sign": "U16", "multiplier": "1", "bytes": 1},
    TOU_CHARGE_TARGET_SOC: {"description": "TOU Charge Target SOC", "unit": "%", "sign": "U16", "multiplier": "1", "bytes": 1},
    TOU_CHARGE_POWER: {"description": "TOU Charge Power", "unit": "", "sign": "U32", "multiplier": "1", "bytes": 1},
    TOU_EXECUTED_DATE_START: {"description": "TOU Executed Date Start", "unit": "Month/Date", "sign": "U16", "multiplier": "1", "bytes": 1},
    TOU_EXECUTED_DATE_END: {"description": "TOU Executed Date End", "unit": "Month/Date", "sign": "U16", "multiplier": "1", "bytes": 1},
    TOU_EXECUTED_DAY_OF_WEEK: {"description": "TOU Executed Day of Week", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    TOU_CONTROL: {"description": "TOU Control", "unit": "", "sign": "U16", "multiplier": "", "bytes": 0},
    PEAK_SHAVING_DISCHARGE_THRESHOLD: {"description": "Peak Shaving Discharge Threshold", "unit": "", "sign": "U32", "multiplier": "1", "bytes": 1},
    PEAK_SHAVING_CHARGE_THRESHOLD: {"description": "Peak Shaving Charge Threshold", "unit": "", "sign": "U32", "multiplier": "1", "bytes": 1},
}


error_codes = {
    SYS_STATE: {
        (0,0): {"label": "waiting", "description": "Waiting state"},
        (0,1): {"label": "waiting", "description": "Detection status"},
        (0,2): {"label": "Grid-connected", "description": "Grid-connected status"},
        (0,3): {"label": "Emergency", "description": "Emergency power supply status"},
        (0,4): {"label": "Recoverable", "description": "Recoverable fault state"},
        (0,5): {"label": "Permanent", "description": "Permanent fault status"},
        (0,6): {"label": "Upgrade", "description": "Upgrade status"},
        (0,7): {"label": "Self-charging", "description": "Self-charging status"},
    },
    # Fault 1
    FAULT1: {
        # Fault Message: Byte 0
        (0, 0): {"num": "001", "label": "GridOVP", "description": "Grid over-voltage"},
        (0, 1): {"num": "002", "label": "GridUVP", "description": "Grid undervoltage"},
        (0, 2): {"num": "003", "label": "GridOFP", "description": "Grid Overfrequency"},
        (0, 3): {"num": "004", "label": "GridUFP", "description": "Grid Underfrequency"},
        (0, 4): {"num": "005", "label": "GFCI", "description": "Leakage current fault"},
        (0, 5): {"num": "006", "label": "OVRT", "description": "High penetration error"},
        (0, 6): {"num": "007", "label": "LVRT", "description": "Low penetration error"},
        (0, 7): {"num": "008", "label": "IslandFault", "description": "Islanding error"},
        # Fault Message: Byte 1
        (1, 0): {"num": "009", "label": "GridOVPInstant1", "description": "Grid voltage transient value overvoltage 1"},
        (1, 1): {"num": "010", "label": "GridOVPInstant2", "description": "Grid voltage transient value overvoltage 2"},
        (1, 2): {"num": "011", "label": "VGridLineFault", "description": "Grid line voltage error"},
        (1, 3): {"num": "012", "label": "InvVoltFault", "description": "Inverter voltage error"},
        (1, 4): {"num": "013", "label": "RefluxFault", "description": "Anti-backflow overload"},
    },
    FAULT2: {
    # Fault Message: Byte 0
    (0, 0): {"num": "017", "label": "HwADErrIGrid", "description": "Grid current sampling error"},
    (0, 1): {"num": "018", "label": "HwADErrDCI(AC)", "description": "Grid current DC component sampling error (AC side)"},
    (0, 2): {"num": "019", "label": "HwADErrVGrid(DC)", "description": "Grid voltage sampling error (DC side)"},
    (0, 3): {"num": "020", "label": "HwADErrVGrid(AC)", "description": "Grid voltage sampling error (AC side)"},
    (0, 4): {"num": "021", "label": "HwGFCIFault(DC)", "description": "Leakage current sampling error (DC side)"},
    (0, 5): {"num": "022", "label": "HwGFCIFault(AC)", "description": "Leakage current sampling error (AC side)"},
    (0, 6): {"num": "023", "label": "HwADErrDCV", "description": "Load voltage DC component sampling error"},
    (0, 7): {"num": "024", "label": "HwADErrIdc", "description": "DC input current sampling error"},
    # Fault Message: Byte 1
    (1, 0): {"num": "025", "label": "HwADErrDCI(DC)", "description": "DC component sampling error of grid current (DC side)"},
    (1, 1): {"num": "026", "label": "HwADErrIdcBranch", "description": "DC input branch current sampling error"},
    (1, 4): {"num": "029", "label": "ConsistentGFCI", "description": "Leakage current consistency error"},
    (1, 5): {"num": "030", "label": "ConsistentVgrid", "description": "Grid voltage consistency error"},
    (1, 6): {"num": "031", "label": "ConsistentDCI", "description": "DCI consistency error"},
},
FAULT3: {
    # Fault Message: Byte 0
    (0, 0): {"num": "033", "label": "SpiCommFault(DC)", "description": "SPI communication error (DC side)"},
    (0, 1): {"num": "034", "label": "SpiCommFault(AC)", "description": "SPI communication error (AC side)"},
    (0, 2): {"num": "035", "label": "SChip_Fault", "description": "Chip error (DC side)"},
    (0, 3): {"num": "036", "label": "MChip_Fault", "description": "Chip error (AC side)"},
    (0, 4): {"num": "037", "label": "HwAuxPowerFault", "description": "Auxiliary power error"},
    (0, 5): {"num": "038", "label": "InvSoftStartFail", "description": "Inverter soft start failure"},
    # Fault Message: Byte 1
    (1, 0): {"num": "041", "label": "RelayFail", "description": "Relay detection failure"},
    (1, 1): {"num": "042", "label": "IsoFault", "description": "Low insulation impedance"},
    (1, 2): {"num": "043", "label": "PEConnectFault", "description": "Grounding error"},
    (1, 3): {"num": "044", "label": "PvConfigError", "description": "Input mode setting error"},
    (1, 4): {"num": "045", "label": "CTDisconnect", "description": "CT error"},
    (1, 5): {"num": "046", "label": "ReversalConnect", "description": "Input reversal error"},
    (1, 6): {"num": "047", "label": "ParallelFault", "description": "Parallel error"},
    (1, 7): {"num": "048", "label": "SNTypeFault", "description": "Serial number error"},

},
FAULT4: {
    # Fault Message: Byte 0
    (0, 0): {"num": "049", "label": "TempErrBat", "description": "Battery temperature protection"},
    (0, 1): {"num": "050", "label": "TempErrHeatSink1", "description": "Heat sink 1 temperature protection"},
    (0, 2): {"num": "051", "label": "TempErrHeatSink2", "description": "Heater 2 temperature protection"},
    (0, 3): {"num": "052", "label": "TempErrHeatSink3", "description": "Heater 3 temperature protection"},
    (0, 4): {"num": "053", "label": "TempErrHeatSink4", "description": "Heatsink 4 temperature protection"},
    (0, 5): {"num": "054", "label": "TempErrHeatSink5", "description": "Heatsink 5 temperature protection"},
    (0, 6): {"num": "055", "label": "TempErrHeatSink6", "description": "Radiator 6 temperature protection"},
    # Fault Message: Byte 1
    (1, 0): {"num": "057", "label": "TempErrEnv1", "description": "Ambient temperature 1 protection"},
    (1, 1): {"num": "058", "label": "TempErrEnv2", "description": "Ambient temperature 2 protection"},
    (1, 2): {"num": "059", "label": "TempErrInv1", "description": "Module 1 temperature protection"},
    (1, 3): {"num": "060", "label": "TempErrInv2", "description": "Module 2 temperature protection"},
    (1, 4): {"num": "061", "label": "TempErrInv3", "description": "Module 3 temperature protection"},
    (1, 5): {"num": "062", "label": "TempDiffErrInv", "description": "Module temperature difference is too large"},
},

FAULT5: {
    # Fault Message: Byte 0
    (0, 0): {"num": "065", "label": "BusRmsUnbalance", "description": "Bus voltage RMS unbalance"},
    (0, 1): {"num": "066", "label": "BusInstUnbalance", "description": "Bus voltage transient value unbalance"},
    (0, 2): {"num": "067", "label": "BusUVP", "description": "Undervoltage of busbar during grid connection"},
    (0, 3): {"num": "068", "label": "BusZVP", "description": "Bus bar low voltage"},
    (0, 4): {"num": "069", "label": "PVOVP", "description": "PV overvoltage"},
    (0, 5): {"num": "070", "label": "BatOVP", "description": "Battery over-voltage"},
    (0, 6): {"num": "071", "label": "LLCBusOVP", "description": "LLCBus overvoltage protection"},
    (0, 7): {"num": "072", "label": "SwBusRmsOVP", "description": "Inverter bus voltage RMS software overvoltage"},
    # Fault Message: Byte 1
    (1, 0): {"num": "073", "label": "SwBusIOVP", "description": "Inverter bus voltage transient value software overvoltage"},
    (1, 1): {"num": "074", "label": "FlyingCapOVP", "description": "Flying Cross Capacitor Overvoltage Protection"},
    (1, 2): {"num": "075", "label": "FlyingCapUVP", "description": "Flying Cross capacitor undervoltage protection"},
},
FAULT6: {
    # Fault Message: Byte 0
    (0, 0): {"num": "081", "label": "SwBatOCP", "description": "Battery overcurrent software protection"},
    (0, 1): {"num": "082", "label": "DciOCP", "description": "Dci overcurrent protection"},
    (0, 2): {"num": "083", "label": "SwIOCP", "description": "Output transient current protection"},
    (0, 3): {"num": "084", "label": "SwBuckBoostOCP", "description": "BuckBoost software overcurrent"},
    (0, 4): {"num": "085", "label": "SwAcRmsOCP", "description": "Output RMS current protection"},
    (0, 5): {"num": "086", "label": "SwPvOCPInstant", "description": "PV instantaneous current overcurrent software protection"},
    (0, 6): {"num": "087", "label": "IpvUnbalance", "description": "PV parallel uneven current"},
    (0, 7): {"num": "088", "label": "IacUnbalance", "description": "Output current unbalance"},
    # Fault Message: Byte 1
    (1, 0): {"num": "089", "label": "SwPvOCP", "description": "PV software overcurrent protection"},
    (1, 1): {"num": "090", "label": "IbalanceOCP", "description": "Balanced circuit overcurrent protection"},
    (1, 2): {"num": "091", "label": "ResOver", "description": "Resonance protection"},
},
FAULT7: {
    # Fault Message: Byte 0
    (0, 0): {"num": "097", "label": "HwLLCBusOVP", "description": "LLC bus hardware overvoltage"},
    (0, 1): {"num": "098", "label": "HwBusOVP", "description": "Inverter bus hardware overvoltage"},
    (0, 2): {"num": "099", "label": "HwBuckBoostOCP", "description": "BuckBoost hardware overcurrent"},
    (0, 3): {"num": "100", "label": "HwBatOCP", "description": "Battery hardware overcurrent"},
    (0, 5): {"num": "102", "label": "HwPVOCP", "description": "PV hardware overcurrent"},
    (0, 6): {"num": "103", "label": "HwACOCP", "description": "AC output hardware overcurrent"},
    # Fault Message: Byte 1
    (1, 0): {"num": "105", "label": "MeterCommFault", "description": "Power meter error"},
    (1, 1): {"num": "106", "label": "SNMachineFault", "description": "Serial number model error"},
    (1, 5): {"num": "110", "label": "Overload1", "description": "Overload protection 1"},
    (1, 6): {"num": "111", "label": "Overload2", "description": "Overload protection 2"},
    (1, 7): {"num": "112", "label": "Overload3", "description": "Overload protection 3"},
},
FAULT8: {
    # Fault Message: Byte 0
    (0, 0): {"num": "113", "label": "OverTempDerating", "description": "Overtemperature derating"},
    (0, 1): {"num": "114", "label": "FreqDerating", "description": "Frequency down load"},
    (0, 2): {"num": "115", "label": "FreqLoading", "description": "Frequency loading"},
    (0, 3): {"num": "116", "label": "VoltDerating", "description": "Voltage down load"},
    (0, 4): {"num": "117", "label": "VoltLoading", "description": "Voltage loading"},
    # Fault Message: Byte 1
    (1, 0): {"num": "121", "label": "SpdFail(DC)", "description": "Lightning protection failure (DC)"},
    (1, 1): {"num": "122", "label": "SpdFail(AC)", "description": "Lightning protection failure (AC)"},
    (1, 3): {"num": "124", "label": "BatDchgProhibit", "description": "Battery low voltage protection"},
    (1, 4): {"num": "125", "label": "BatLowVoltShut", "description": "Battery low voltage shutdown"},
    (1, 5): {"num": "126", "label": "BatLowVoltPreAlarm", "description": "Battery low voltage pre-alarm"},
},
FAULT9: {
    # Fault Message: Byte 0
    (0, 0): {"num": "129", "label": "PermHwAcOCP", "description": "Output hardware overcurrent permanent fault"},
    (0, 1): {"num": "130", "label": "PermBusOVP", "description": "Bus overvoltage permanent fault"},
    (0, 2): {"num": "131", "label": "PermHwBusOVP", "description": "Bus hardware over-voltage permanent fault"},
    (0, 3): {"num": "132", "label": "PermIpvUnbalance", "description": "PV uneven flow permanent fault"},
    (0, 4): {"num": "133", "label": "PermEPSBatOCP", "description": "Battery overcurrent permanent fault in EPS mode"},
    (0, 5): {"num": "134", "label": "PermAcOCPInstant", "description": "Output transient overcurrent permanent fault"},
    (0, 6): {"num": "135", "label": "PermIacUnbalance", "description": "Output current unbalance permanent fault"},
    # Fault Message: Byte 1
    (1, 0): {"num": "137", "label": "PermInCfgError", "description": "Input mode setting error permanent fault"},
    (1, 1): {"num": "138", "label": "PermDCOCPInstant", "description": "Input overcurrent permanent fault"},
    (1, 2): {"num": "139", "label": "PermHwDCOCP", "description": "Input hardware overcurrent permanent fault"},
    (1, 3): {"num": "140", "label": "PermRelayFail", "description": "Relay permanent fault"},
    (1, 4): {"num": "141", "label": "PermBusUnbalance", "description": "Bus unbalance permanent fault"},
    (1, 5): {"num": "142", "label": "PermSpdFail(DC)", "description": "Lightning protection permanent fault - DC side"},
    (1, 6): {"num": "143", "label": "PermSpdFail(AC)", "description": "Lightning protection permanent fault - AC side"},
},
FAULT10: {
    # Fault Message: Byte 0
    (0, 0): {"num": "145", "label": "USBFault", "description": "USB fault"},
    (0, 1): {"num": "146", "label": "WifiFault", "description": "WIFI fault"},
    (0, 2): {"num": "147", "label": "BluetoothFault", "description": "Bluetooth fault"},
    (0, 3): {"num": "148", "label": "RTCFault", "description": "RTC clock fault"},
    (0, 4): {"num": "149", "label": "CommEEPROMFault", "description": "Communication board EEPROM error"},
    (0, 5): {"num": "150", "label": "FlashFault", "description": "Communication board FLASH error"},
    (0, 7): {"num": "152", "label": "SafetyVerFault", "description": "Safety regulation version error"},
    # Fault Message: Byte 1
    (1, 0): {"num": "153", "label": "SCILose(DC)", "description": "SCI communication error (DC side)"},
    (1, 1): {"num": "154", "label": "SCILose(AC)", "description": "SCI communication error (AC side)"},
    (1, 2): {"num": "155", "label": "SCILose(Fuse)", "description": "SCI communication error (convergence board side)"},
    (1, 3): {"num": "156", "label": "SoftVerError", "description": "Software version inconsistency"},
    (1, 4): {"num": "157", "label": "BMS1CommFault", "description": "Lithium battery 1 communication error"},
    (1, 5): {"num": "158", "label": "BMS2CommFault", "description": "Li-ion battery 2 communication error"},
    (1, 6): {"num": "159", "label": "BMS3CommFault", "description": "Lithium battery 3 communication error"},
    (1, 7): {"num": "160", "label": "BMS4CommFault", "description": "Lithium battery 4 communication failure"},
},
FAULT11: {
    # Fault Message: Byte 0
    (0, 0): {"num": "161", "label": "ForceShutdown", "description": "Forced shutdown"},
    (0, 1): {"num": "162", "label": "RemoteShutdown", "description": "Remote shutdown"},
    (0, 2): {"num": "163", "label": "Drms0Shutdown", "description": "Drms0 shutdown"},
    (0, 4): {"num": "165", "label": "RemoteDerating", "description": "Remote down load"},
    (0, 5): {"num": "166", "label": "LogicIfDerating", "description": "Logic interface down load"},
    (0, 6): {"num": "167", "label": "AlarmAntiReflux", "description": "Anti-Reverse Flow Downgrade"},
    # Fault Message: Byte 1
    (1, 0): {"num": "169", "label": "FanFault1", "description": "Fan 1 failure"},
    (1, 1): {"num": "170", "label": "FanFault2", "description": "Fan 2 failure"},
    (1, 2): {"num": "171", "label": "FanFault3", "description": "Fan 3 failure"},
    (1, 3): {"num": "172", "label": "FanFault4", "description": "Fan 4 failure"},
    (1, 4): {"num": "173", "label": "FanFault5", "description": "Fan 5 failure"},
    (1, 5): {"num": "174", "label": "FanFault6", "description": "Fan 6 failure"},
    (1, 6): {"num": "175", "label": "FanFault7", "description": "Fan 7 fault"},
    (1, 7): {"num": "176", "label": "MeterCommLose", "description": "Meter communication failure"},
},
FAULT12: {
    # Fault Message: Byte 0
    (0, 0): {"num": "177", "label": "BMS OVP", "description": "BMS over-voltage alarm"},
    (0, 1): {"num": "178", "label": "BMS UVP", "description": "BMS undervoltage alarm"},
    (0, 2): {"num": "179", "label": "BMS OTP", "description": "BMS high temperature alarm"},
    (0, 3): {"num": "180", "label": "BMS UTP", "description": "BMS low temperature alarm"},
    (0, 4): {"num": "181", "label": "BMS OCP", "description": "BMS charge/discharge overload alarm"},
    (0, 5): {"num": "182", "label": "BMS Short", "description": "BMS short circuit alarm"},
    (0, 6): {"num": "183", "label": "BMS VerFault", "description": "BMS version inconsistency"},
    (0, 7): {"num": "184", "label": "BMS CAN VerFault", "description": "BMS CAN version inconsistency"},
    # Fault Message: Byte 1
    (1, 0): {"num": "185", "label": "BMS CAN VerLow", "description": "BMS CAN version is too low"},
    (1, 4): {"num": "189", "label": "AFCICommLose", "description": "Arc device communication failure"},
    (1, 5): {"num": "190", "label": "DCArcingAlarm", "description": "DC arc alarm fault"},
    (1, 6): {"num": "191", "label": "PID_Output_Fail", "description": "PID repair failed"},
    (1, 7): {"num": "192", "label": "PLC_Com_Fail", "description": "PLC module heartbeat loss"},
},
FAULT13: {
    # Fault Message: Byte 0
    (0, 0): {"num": "193", "label": "StrFuseALM1-1", "description": "String fuse open circuit alarm 1-1"},
    (0, 1): {"num": "194", "label": "StrFuseALM1-2", "description": "String fuse open circuit alarm 1-2"},
    (0, 2): {"num": "195", "label": "StrFuseALM2-1", "description": "String fuse open circuit alarm 2-1"},
    (0, 3): {"num": "196", "label": "StrFuseALM2-2", "description": "String fuse open circuit alarm 2-2"},
    (0, 4): {"num": "197", "label": "StrFuseALM3-1", "description": "String fuse open circuit alarm 3-1"},
    (0, 5): {"num": "198", "label": "StrFuseALM3-2", "description": "String fuse open circuit alarm 3-2"},
    (0, 6): {"num": "199", "label": "StrFuseALM4-1", "description": "String fuse open circuit alarm 4-1"},
    (0, 7): {"num": "200", "label": "StrFuseALM4-2", "description": "String fuse open circuit alarm 4-2"},
    # Fault Message: Byte 1
    (1, 0): {"num": "201", "label": "StrFuseALM5-1", "description": "String fuse open circuit alarm 5-1"},
    (1, 1): {"num": "202", "label": "StrFuseALM5-2", "description": "String fuse open circuit alarm 5-2"},
    (1, 2): {"num": "203", "label": "StrFuseALM6-1", "description": "String fuse open circuit alarm 6-1"},
    (1, 3): {"num": "204", "label": "StrFuseALM6-2", "description": "String fuse open circuit alarm 6-2"},
    (1, 4): {"num": "205", "label": "StrFuseALM7-1", "description": "String fuse open circuit alarm 7-1"},
    (1, 5): {"num": "206", "label": "StrFuseALM7-2", "description": "String fuse open circuit alarm 7-2"},
    (1, 6): {"num": "207", "label": "StrFuseALM8-1", "description": "String fuse open circuit alarm 8-1"},
    (1, 7): {"num": "208", "label": "StrFuseALM8-2", "description": "String fuse open circuit alarm 8-2"},
},
FAULT14: {
    # Fault Message: Byte 0
    (0, 0): {"num": "209", "label": "StrFuseALM9-1", "description": "String fuse open circuit alarm 9-1"},
    (0, 1): {"num": "210", "label": "StrFuseALM9-2", "description": "String fuse open circuit alarm 9-2"},
    (0, 2): {"num": "211", "label": "StrFuseALM10-1", "description": "String fuse open circuit alarm 10-1"},
    (0, 3): {"num": "212", "label": "StrFuseALM10-2", "description": "String fuse open circuit alarm 10-2"},
    (0, 4): {"num": "213", "label": "StrFuseALM11-1", "description": "String fuse open circuit alarm 11-1"},
    (0, 5): {"num": "214", "label": "StrFuseALM11-2", "description": "String fuse open circuit alarm 11-2"},
    (0, 6): {"num": "215", "label": "StrFuseALM12-1", "description": "String fuse open circuit alarm 12-1"},
    (0, 7): {"num": "216", "label": "StrFuseALM12-2", "description": "String fuse open circuit alarm 12-2"},
    # Fault Message: Byte 1
    (1, 0): {"num": "217", "label": "StrFuseALM13-1", "description": "String fuse open circuit alarm 13-1"},
    (1, 1): {"num": "218", "label": "StrFuseALM13-2", "description": "String fuse open circuit alarm 13-2"},
    (1, 2): {"num": "219", "label": "StrFuseALM14-1", "description": "String fuse open circuit alarm 14-1"},
    (1, 3): {"num": "220", "label": "StrFuseALM14-2", "description": "String fuse open circuit alarm 14-2"},
    (1, 4): {"num": "221", "label": "StrFuseALM15-1", "description": "String fuse open circuit alarm 15-1"},
    (1, 5): {"num": "222", "label": "StrFuseALM15-2", "description": "String fuse open circuit alarm 15-2"},
    (1, 6): {"num": "223", "label": "StrFuseALM16-1", "description": "String fuse open circuit alarm 16-1"},
    (1, 7): {"num": "224", "label": "StrFuseALM16-2", "description": "String fuse open circuit alarm 16-2"},
},
FAULT15: {
    # Fault Message: Byte 0
    (0, 0): {"num": "225", "label": "InputFuseALM0", "description": "Battery input fuse open circuit alarm 0"},
    (0, 1): {"num": "226", "label": "InputFuseALM1", "description": "Battery input fuse open circuit alarm 1"},
    (0, 2): {"num": "227", "label": "InputFuseALM2", "description": "Battery input fuse open circuit alarm 2"},
    (0, 3): {"num": "228", "label": "InputFuseALM3", "description": "Battery input fuse open circuit alarm 3"},
    (0, 4): {"num": "229", "label": "InputFuseALM4", "description": "Battery input fuse open circuit alarm 4"},
    (0, 5): {"num": "230", "label": "InputFuseALM5", "description": "Battery input fuse open circuit alarm 5"},
    (0, 6): {"num": "231", "label": "InputFuseALM6", "description": "Battery input fuse open circuit alarm 6"},
    (0, 7): {"num": "232", "label": "InputFuseALM7", "description": "Battery input fuse open circuit alarm 7"},
    # Fault Message: Byte 1
    (1, 0): {"num": "233", "label": "InputFuseALM8", "description": "Battery input fuse open circuit alarm 8"},
    (1, 1): {"num": "234", "label": "InputFuseALM9", "description": "Battery input fuse open circuit alarm 9"},
    (1, 2): {"num": "235", "label": "InputFuseALM10", "description": "Battery input fuse open circuit alarm 10"},
    (1, 3): {"num": "236", "label": "InputFuseALM11", "description": "Battery input fuse open circuit alarm 11"},
    (1, 4): {"num": "237", "label": "InputFuseALM12", "description": "Battery input fuse open circuit alarm 12"},
    (1, 5): {"num": "238", "label": "InputFuseALM13", "description": "Battery input fuse open circuit alarm 13"},
    (1, 6): {"num": "239", "label": "InputFuseALM14", "description": "Battery input fuse open circuit alarm 14"},
    (1, 7): {"num": "240", "label": "InputFuseALM15", "description": "Battery input fuse open circuit alarm 15"},
}








}