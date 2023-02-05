
        [Code]
            File Name: Algo_Finv.py
            Object Name: King_candle
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Locals: 8
            Stack Size: 24
            Flags: 0x00000043 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)
            [Names]
                'King_Candle_Duration_Detection'
                'Trade_Nifty'
                'instrument'
                'Trade_FinNifty'
                'Trade_BankNifty'
                'get_instrument_by_symbol'
                'str'
                'int'
                'datetime'
                'now'
                'timedelta'
                'timestamp'
                'time'
                'king_interval'
                'No_of_Days_Data'
                'pd'
                'DataFrame'
                'get_historical'
                'shape'
                'iLog'
                'iloc'
                'reset_index'
                'ta'
                'rsi'
                'close'
                'RSI_Period'
                'adx'
                'high'
                'low'
                'ADX_Period'
                'supertrend'
                'ST_Period'
                'ST_Mult'
                'index'
                'drop'
                'tail'
                'RSI_Low'
                'RSI_High'
                'King_ST'
                'Queen_ST'
                'Candle_Close'
                'King_Candle_Formed'
                'king_use_adx'
                'First_King'
                'King'
                'First_King_L'
                'max'
                'min'
                'King_Candle_Min_SL'
                'King_Candle_Max_SL'
                'First_King_SL'
                'King_SL'
                'Queen_Candle_Formed'
                'First_Queen'
                'Queen'
                'First_Queen_H'
                'First_Queen_SL'
                'Queen_SL'
                'K_Direction'
                'Latest_King'
                'Latest_King_L'
                'Latest_King_SL'
                'Latest_Queen'
                'Latest_Queen_H'
                'Latest_Queen_SL'
                'round'
                'Exception'
            [Var Names]
                'from_datetime'
                'to_datetime'
                'interval'
                'indices'
                'df'
                'strMsg'
                'df2'
                'ex'
            [Free Vars]
            [Cell Vars]
            [Constants]
                None
                False
                1
                (
                    'NSE'
                    '26000'
                    'Nifty 50'
                )
                (
                    'NSE'
                    '26037'
                    'Nifty Fin Services'
                )
                'NSE'
                'Nifty Bank'
                2
                (
                    'days'
                )
                5
                3
                True
                0
                140
                4
                6
                ' No of Days used for King Candle Calculation ='
                ', No of Data points = '
                (
                    'sendTeleMsg'
                )
                -1
                (
                    'drop'
                )
                (
                    'length'
                )
                'RSI'
                (
                    'ADX'
                    'PDI'
                    'NDI'
                )
                'high'
                'low'
                'close'
                (
                    'ST'
                    'STd'
                    'ST1'
                    'STs'
                )
                'date'
                (
                    'axis'
                )
                (
                    'open'
                    'close'
                    'low'
                    'high'
                    'ADX'
                    'PDI'
                    'NDI'
                    'ST'
                    'RSI'
                )
                'RSIL'
                'RSIH'
                'H'
                -2
                'H1'
                -3
                'H2'
                'L'
                'L1'
                'L2'
                'ST'
                'PDI'
                'NDI'
                ' King Candle Formed ='
                ', King_SL = '
                ' '
                ' Queen Candle Formed ='
                ', Queen SL = '
                1000000
                ' ==Direction : '
                ', Close : '
                ', King : '
                ', King Stop Loss : '
                ', ST : '
                ', Queen : '
                ', Queen Stop Loss : '
                ', RSI : '
                ', PDI : '
                ', NDI : '
                ', H : '
                ', H1 : '
                ', H2 : '
                ',  L : '
                ', L1 : '
                ', L2 : '
                ' Exception occured in King Candle Calculation:'
            [Disassembly]
                0       SETUP_FINALLY                 1163 (to 2330)
                4       LOAD_GLOBAL                   0: King_Candle_Duration_Detection
                6       LOAD_CONST                    1: False
                8       COMPARE_OP                    2 (==)
                10      POP_JUMP_IF_FALSE             243 (to 486)
                12      LOAD_GLOBAL                   1: NULL + King_Candle_Duration_Detection
                14      LOAD_CONST                    2: 1
                16      COMPARE_OP                    2 (==)
                18      POP_JUMP_IF_FALSE             14 (to 28)
                20      BUILD_LIST                    0
                22      LOAD_CONST                    3: ('NSE', '26000', 'Nifty 50')
                24      LIST_EXTEND                   1
                26      STORE_GLOBAL                  2: instrument
                28      LOAD_GLOBAL                   3: NULL + Trade_Nifty
                30      LOAD_CONST                    2: 1
                32      COMPARE_OP                    2 (==)
                34      POP_JUMP_IF_FALSE             22 (to 44)
                36      BUILD_LIST                    0
                38      LOAD_CONST                    4: ('NSE', '26037', 'Nifty Fin Services')
                40      LIST_EXTEND                   1
                42      STORE_GLOBAL                  2: instrument
                44      LOAD_GLOBAL                   4: instrument
                46      LOAD_CONST                    2: 1
                48      COMPARE_OP                    2 (==)
                50      POP_JUMP_IF_FALSE             31 (to 62)
                52      LOAD_GLOBAL                   5: NULL + instrument
                54      LOAD_CONST                    5: 'NSE'
                56      LOAD_CONST                    6: 'Nifty Bank'
                58      CALL_FUNCTION                 2
                60      STORE_GLOBAL                  2: instrument
                62      LOAD_GLOBAL                   6: Trade_FinNifty
                64      LOAD_GLOBAL                   7: NULL + Trade_FinNifty
                66      LOAD_GLOBAL                   8: Trade_BankNifty
                68      LOAD_ATTR                     8: datetime
                70      LOAD_METHOD                   9: now
                72      CALL_METHOD                   0
                74      LOAD_GLOBAL                   8: Trade_BankNifty
                76      LOAD_ATTR                     10: timedelta
                78      LOAD_CONST                    7: 2
                80      LOAD_CONST                    8: ('days',)
                82      CALL_FUNCTION_KW              1
                84      BINARY_SUBTRACT               
                86      LOAD_METHOD                   11: timestamp
                88      CALL_METHOD                   0
                90      CALL_FUNCTION                 1
                92      CALL_FUNCTION                 1
                94      STORE_FAST                    0: from_datetime
                96      LOAD_GLOBAL                   12: str
                98      LOAD_METHOD                   12: time
                100     CALL_METHOD                   0
                102     STORE_FAST                    1: to_datetime
                104     LOAD_CONST                    9: 5
                106     STORE_FAST                    2: interval
                108     LOAD_GLOBAL                   13: NULL + str
                110     LOAD_CONST                    10: 3
                112     COMPARE_OP                    2 (==)
                114     POP_JUMP_IF_FALSE             60 (to 120)
                116     LOAD_CONST                    10: 3
                118     STORE_FAST                    2: interval
                120     LOAD_CONST                    11: True
                122     STORE_FAST                    3: indices
                124     LOAD_CONST                    7: 2
                126     STORE_GLOBAL                  14: No_of_Days_Data
                128     LOAD_GLOBAL                   15: NULL + int
                130     LOAD_METHOD                   16: DataFrame
                132     LOAD_GLOBAL                   17: NULL + datetime
                134     LOAD_GLOBAL                   2: Trade_Nifty
                136     LOAD_FAST                     0: from_datetime
                138     LOAD_FAST                     1: to_datetime
                140     LOAD_FAST                     2: interval
                142     LOAD_FAST                     3: indices
                144     CALL_FUNCTION                 5
                146     CALL_METHOD                   1
                148     STORE_FAST                    4: df
                150     LOAD_FAST                     4: df
                152     LOAD_ATTR                     18: shape
                154     LOAD_CONST                    12: 0
                156     BINARY_SUBSCR                 
                158     LOAD_CONST                    13: 140
                160     COMPARE_OP                    0 (<)
                162     POP_JUMP_IF_FALSE             223 (to 446)
                164     LOAD_GLOBAL                   6: Trade_FinNifty
                166     LOAD_GLOBAL                   7: NULL + Trade_FinNifty
                168     LOAD_GLOBAL                   8: Trade_BankNifty
                170     LOAD_ATTR                     8: datetime
                172     LOAD_METHOD                   9: now
                174     CALL_METHOD                   0
                176     LOAD_GLOBAL                   8: Trade_BankNifty
                178     LOAD_ATTR                     10: timedelta
                180     LOAD_CONST                    10: 3
                182     LOAD_CONST                    8: ('days',)
                184     CALL_FUNCTION_KW              1
                186     BINARY_SUBTRACT               
                188     LOAD_METHOD                   11: timestamp
                190     CALL_METHOD                   0
                192     CALL_FUNCTION                 1
                194     CALL_FUNCTION                 1
                196     STORE_FAST                    0: from_datetime
                198     LOAD_GLOBAL                   15: NULL + int
                200     LOAD_METHOD                   16: DataFrame
                202     LOAD_GLOBAL                   17: NULL + datetime
                204     LOAD_GLOBAL                   2: Trade_Nifty
                206     LOAD_FAST                     0: from_datetime
                208     LOAD_FAST                     1: to_datetime
                210     LOAD_FAST                     2: interval
                212     LOAD_FAST                     3: indices
                214     CALL_FUNCTION                 5
                216     CALL_METHOD                   1
                218     STORE_FAST                    4: df
                220     LOAD_CONST                    10: 3
                222     STORE_GLOBAL                  14: No_of_Days_Data
                224     LOAD_FAST                     4: df
                226     LOAD_ATTR                     18: shape
                228     LOAD_CONST                    12: 0
                230     BINARY_SUBSCR                 
                232     LOAD_CONST                    13: 140
                234     COMPARE_OP                    0 (<)
                236     POP_JUMP_IF_FALSE             223 (to 446)
                238     LOAD_GLOBAL                   6: Trade_FinNifty
                240     LOAD_GLOBAL                   7: NULL + Trade_FinNifty
                242     LOAD_GLOBAL                   8: Trade_BankNifty
                244     LOAD_ATTR                     8: datetime
                246     LOAD_METHOD                   9: now
                248     CALL_METHOD                   0
                250     LOAD_GLOBAL                   8: Trade_BankNifty
                252     LOAD_ATTR                     10: timedelta
                254     LOAD_CONST                    14: 4
                256     LOAD_CONST                    8: ('days',)
                258     CALL_FUNCTION_KW              1
                260     BINARY_SUBTRACT               
                262     LOAD_METHOD                   11: timestamp
                264     CALL_METHOD                   0
                266     CALL_FUNCTION                 1
                268     CALL_FUNCTION                 1
                270     STORE_FAST                    0: from_datetime
                272     LOAD_GLOBAL                   15: NULL + int
                274     LOAD_METHOD                   16: DataFrame
                276     LOAD_GLOBAL                   17: NULL + datetime
                278     LOAD_GLOBAL                   2: Trade_Nifty
                280     LOAD_FAST                     0: from_datetime
                282     LOAD_FAST                     1: to_datetime
                284     LOAD_FAST                     2: interval
                286     LOAD_FAST                     3: indices
                288     CALL_FUNCTION                 5
                290     CALL_METHOD                   1
                292     STORE_FAST                    4: df
                294     LOAD_CONST                    14: 4
                296     STORE_GLOBAL                  14: No_of_Days_Data
                298     LOAD_FAST                     4: df
                300     LOAD_ATTR                     18: shape
                302     LOAD_CONST                    12: 0
                304     BINARY_SUBSCR                 
                306     LOAD_CONST                    13: 140
                308     COMPARE_OP                    0 (<)
                310     POP_JUMP_IF_FALSE             223 (to 446)
                312     LOAD_GLOBAL                   6: Trade_FinNifty
                314     LOAD_GLOBAL                   7: NULL + Trade_FinNifty
                316     LOAD_GLOBAL                   8: Trade_BankNifty
                318     LOAD_ATTR                     8: datetime
                320     LOAD_METHOD                   9: now
                322     CALL_METHOD                   0
                324     LOAD_GLOBAL                   8: Trade_BankNifty
                326     LOAD_ATTR                     10: timedelta
                328     LOAD_CONST                    9: 5
                330     LOAD_CONST                    8: ('days',)
                332     CALL_FUNCTION_KW              1
                334     BINARY_SUBTRACT               
                336     LOAD_METHOD                   11: timestamp
                338     CALL_METHOD                   0
                340     CALL_FUNCTION                 1
                342     CALL_FUNCTION                 1
                344     STORE_FAST                    0: from_datetime
                346     LOAD_GLOBAL                   15: NULL + int
                348     LOAD_METHOD                   16: DataFrame
                350     LOAD_GLOBAL                   17: NULL + datetime
                352     LOAD_GLOBAL                   2: Trade_Nifty
                354     LOAD_FAST                     0: from_datetime
                356     LOAD_FAST                     1: to_datetime
                358     LOAD_FAST                     2: interval
                360     LOAD_FAST                     3: indices
                362     CALL_FUNCTION                 5
                364     CALL_METHOD                   1
                366     STORE_FAST                    4: df
                368     LOAD_CONST                    9: 5
                370     STORE_GLOBAL                  14: No_of_Days_Data
                372     LOAD_FAST                     4: df
                374     LOAD_ATTR                     18: shape
                376     LOAD_CONST                    12: 0
                378     BINARY_SUBSCR                 
                380     LOAD_CONST                    13: 140
                382     COMPARE_OP                    0 (<)
                384     POP_JUMP_IF_FALSE             223 (to 446)
                386     LOAD_GLOBAL                   6: Trade_FinNifty
                388     LOAD_GLOBAL                   7: NULL + Trade_FinNifty
                390     LOAD_GLOBAL                   8: Trade_BankNifty
                392     LOAD_ATTR                     8: datetime
                394     LOAD_METHOD                   9: now
                396     CALL_METHOD                   0
                398     LOAD_GLOBAL                   8: Trade_BankNifty
                400     LOAD_ATTR                     10: timedelta
                402     LOAD_CONST                    15: 6
                404     LOAD_CONST                    8: ('days',)
                406     CALL_FUNCTION_KW              1
                408     BINARY_SUBTRACT               
                410     LOAD_METHOD                   11: timestamp
                412     CALL_METHOD                   0
                414     CALL_FUNCTION                 1
                416     CALL_FUNCTION                 1
                418     STORE_FAST                    0: from_datetime
                420     LOAD_GLOBAL                   15: NULL + int
                422     LOAD_METHOD                   16: DataFrame
                424     LOAD_GLOBAL                   17: NULL + datetime
                426     LOAD_GLOBAL                   2: Trade_Nifty
                428     LOAD_FAST                     0: from_datetime
                430     LOAD_FAST                     1: to_datetime
                432     LOAD_FAST                     2: interval
                434     LOAD_FAST                     3: indices
                436     CALL_FUNCTION                 5
                438     CALL_METHOD                   1
                440     STORE_FAST                    4: df
                442     LOAD_CONST                    15: 6
                444     STORE_GLOBAL                  14: No_of_Days_Data
                446     LOAD_CONST                    11: True
                448     STORE_GLOBAL                  0: King_Candle_Duration_Detection
                450     LOAD_CONST                    16: ' No of Days used for King Candle Calculation ='
                452     LOAD_GLOBAL                   14: int
                454     FORMAT_VALUE                  0
                456     LOAD_CONST                    17: ', No of Data points = '
                458     LOAD_FAST                     4: df
                460     LOAD_ATTR                     18: shape
                462     LOAD_CONST                    12: 0
                464     BINARY_SUBSCR                 
                466     FORMAT_VALUE                  0
                468     BUILD_STRING                  4
                470     STORE_FAST                    5: strMsg
                472     LOAD_GLOBAL                   19: NULL + now
                474     LOAD_FAST                     5: strMsg
                476     LOAD_CONST                    7: 2
                478     LOAD_CONST                    1: False
                480     LOAD_CONST                    18: ('sendTeleMsg',)
                482     CALL_FUNCTION_KW              3
                484     POP_TOP                       
                486     LOAD_GLOBAL                   0: King_Candle_Duration_Detection
                488     LOAD_CONST                    11: True
                490     COMPARE_OP                    2 (==)
                492     POP_JUMP_IF_FALSE             319 (to 638)
                496     LOAD_GLOBAL                   1: NULL + King_Candle_Duration_Detection
                498     LOAD_CONST                    2: 1
                500     COMPARE_OP                    2 (==)
                502     POP_JUMP_IF_FALSE             257 (to 514)
                506     BUILD_LIST                    0
                508     LOAD_CONST                    3: ('NSE', '26000', 'Nifty 50')
                510     LIST_EXTEND                   1
                512     STORE_GLOBAL                  2: instrument
                514     LOAD_GLOBAL                   3: NULL + Trade_Nifty
                516     LOAD_CONST                    2: 1
                518     COMPARE_OP                    2 (==)
                520     POP_JUMP_IF_FALSE             266 (to 532)
                524     BUILD_LIST                    0
                526     LOAD_CONST                    4: ('NSE', '26037', 'Nifty Fin Services')
                528     LIST_EXTEND                   1
                530     STORE_GLOBAL                  2: instrument
                532     LOAD_GLOBAL                   4: instrument
                534     LOAD_CONST                    2: 1
                536     COMPARE_OP                    2 (==)
                538     POP_JUMP_IF_FALSE             276 (to 552)
                542     LOAD_GLOBAL                   5: NULL + instrument
                544     LOAD_CONST                    5: 'NSE'
                546     LOAD_CONST                    6: 'Nifty Bank'
                548     CALL_FUNCTION                 2
                550     STORE_GLOBAL                  2: instrument
                552     LOAD_GLOBAL                   6: Trade_FinNifty
                554     LOAD_GLOBAL                   7: NULL + Trade_FinNifty
                556     LOAD_GLOBAL                   8: Trade_BankNifty
                558     LOAD_ATTR                     8: datetime
                560     LOAD_METHOD                   9: now
                562     CALL_METHOD                   0
                564     LOAD_GLOBAL                   8: Trade_BankNifty
                566     LOAD_ATTR                     10: timedelta
                568     LOAD_GLOBAL                   14: int
                570     LOAD_CONST                    8: ('days',)
                572     CALL_FUNCTION_KW              1
                574     BINARY_SUBTRACT               
                576     LOAD_METHOD                   11: timestamp
                578     CALL_METHOD                   0
                580     CALL_FUNCTION                 1
                582     CALL_FUNCTION                 1
                584     STORE_FAST                    0: from_datetime
                586     LOAD_GLOBAL                   12: str
                588     LOAD_METHOD                   12: time
                590     CALL_METHOD                   0
                592     STORE_FAST                    1: to_datetime
                594     LOAD_CONST                    9: 5
                596     STORE_FAST                    2: interval
                598     LOAD_GLOBAL                   13: NULL + str
                600     LOAD_CONST                    10: 3
                602     COMPARE_OP                    2 (==)
                604     POP_JUMP_IF_FALSE             306 (to 612)
                608     LOAD_CONST                    10: 3
                610     STORE_FAST                    2: interval
                612     LOAD_CONST                    11: True
                614     STORE_FAST                    3: indices
                616     LOAD_GLOBAL                   15: NULL + int
                618     LOAD_METHOD                   16: DataFrame
                620     LOAD_GLOBAL                   17: NULL + datetime
                622     LOAD_GLOBAL                   2: Trade_Nifty
                624     LOAD_FAST                     0: from_datetime
                626     LOAD_FAST                     1: to_datetime
                628     LOAD_FAST                     2: interval
                630     LOAD_FAST                     3: indices
                632     CALL_FUNCTION                 5
                634     CALL_METHOD                   1
                636     STORE_FAST                    4: df
                638     LOAD_FAST                     4: df
                640     LOAD_ATTR                     20: iloc
                642     LOAD_CONST                    0: None
                644     LOAD_CONST                    0: None
                646     LOAD_CONST                    19: -1
                648     BUILD_SLICE                   3
                650     BINARY_SUBSCR                 
                652     LOAD_ATTR                     21: reset_index
                654     LOAD_CONST                    11: True
                656     LOAD_CONST                    20: ('drop',)
                658     CALL_FUNCTION_KW              1
                660     STORE_FAST                    4: df
                662     LOAD_GLOBAL                   22: timestamp
                664     LOAD_ATTR                     23: rsi
                666     LOAD_FAST                     4: df
                668     LOAD_ATTR                     24: close
                670     LOAD_GLOBAL                   25: NULL + time
                672     LOAD_CONST                    21: ('length',)
                674     CALL_FUNCTION_KW              2
                676     LOAD_FAST                     4: df
                678     LOAD_CONST                    22: 'RSI'
                680     STORE_SUBSCR                  
                682     LOAD_GLOBAL                   22: timestamp
                684     LOAD_ATTR                     26: adx
                686     LOAD_FAST                     4: df
                688     LOAD_ATTR                     27: high
                690     LOAD_FAST                     4: df
                692     LOAD_ATTR                     28: low
                694     LOAD_FAST                     4: df
                696     LOAD_ATTR                     24: close
                698     LOAD_GLOBAL                   29: NULL + No_of_Days_Data
                700     LOAD_CONST                    21: ('length',)
                702     CALL_FUNCTION_KW              4
                704     LOAD_FAST                     4: df
                706     BUILD_LIST                    0
                708     LOAD_CONST                    23: ('ADX', 'PDI', 'NDI')
                710     LIST_EXTEND                   1
                712     STORE_SUBSCR                  
                714     LOAD_GLOBAL                   22: timestamp
                716     LOAD_METHOD                   30: supertrend
                718     LOAD_FAST                     4: df
                720     LOAD_CONST                    24: 'high'
                722     BINARY_SUBSCR                 
                724     LOAD_FAST                     4: df
                726     LOAD_CONST                    25: 'low'
                728     BINARY_SUBSCR                 
                730     LOAD_FAST                     4: df
                732     LOAD_CONST                    26: 'close'
                734     BINARY_SUBSCR                 
                736     LOAD_GLOBAL                   31: NULL + pd
                738     LOAD_GLOBAL                   32: DataFrame
                740     CALL_METHOD                   5
                742     LOAD_FAST                     4: df
                744     BUILD_LIST                    0
                746     LOAD_CONST                    27: ('ST', 'STd', 'ST1', 'STs')
                748     LIST_EXTEND                   1
                750     STORE_SUBSCR                  
                752     LOAD_FAST                     4: df
                754     LOAD_CONST                    28: 'date'
                756     BINARY_SUBSCR                 
                758     LOAD_FAST                     4: df
                760     STORE_ATTR                    33: index
                762     LOAD_FAST                     4: df
                764     LOAD_ATTR                     34: drop
                766     LOAD_CONST                    28: 'date'
                768     LOAD_CONST                    2: 1
                770     LOAD_CONST                    29: ('axis',)
                772     CALL_FUNCTION_KW              2
                774     STORE_FAST                    4: df
                776     LOAD_FAST                     4: df
                778     BUILD_LIST                    0
                780     LOAD_CONST                    30: ('open', 'close', 'low', 'high', 'ADX', 'PDI', 'NDI', 'ST', 'RSI')
                782     LIST_EXTEND                   1
                784     BINARY_SUBSCR                 
                786     LOAD_METHOD                   35: tail
                788     LOAD_CONST                    10: 3
                790     CALL_METHOD                   1
                792     STORE_FAST                    6: df2
                794     LOAD_GLOBAL                   36: shape
                796     LOAD_FAST                     6: df2
                798     LOAD_CONST                    31: 'RSIL'
                800     STORE_SUBSCR                  
                802     LOAD_GLOBAL                   37: NULL + shape
                804     LOAD_FAST                     6: df2
                806     LOAD_CONST                    32: 'RSIH'
                808     STORE_SUBSCR                  
                810     LOAD_FAST                     4: df
                812     LOAD_CONST                    24: 'high'
                814     BINARY_SUBSCR                 
                816     LOAD_ATTR                     20: iloc
                818     LOAD_CONST                    19: -1
                820     BINARY_SUBSCR                 
                822     LOAD_FAST                     6: df2
                824     LOAD_CONST                    33: 'H'
                826     STORE_SUBSCR                  
                828     LOAD_FAST                     4: df
                830     LOAD_CONST                    24: 'high'
                832     BINARY_SUBSCR                 
                834     LOAD_ATTR                     20: iloc
                836     LOAD_CONST                    34: -2
                838     BINARY_SUBSCR                 
                840     LOAD_FAST                     6: df2
                842     LOAD_CONST                    35: 'H1'
                844     STORE_SUBSCR                  
                846     LOAD_FAST                     4: df
                848     LOAD_CONST                    24: 'high'
                850     BINARY_SUBSCR                 
                852     LOAD_ATTR                     20: iloc
                854     LOAD_CONST                    36: -3
                856     BINARY_SUBSCR                 
                858     LOAD_FAST                     6: df2
                860     LOAD_CONST                    37: 'H2'
                862     STORE_SUBSCR                  
                864     LOAD_FAST                     4: df
                866     LOAD_CONST                    25: 'low'
                868     BINARY_SUBSCR                 
                870     LOAD_ATTR                     20: iloc
                872     LOAD_CONST                    19: -1
                874     BINARY_SUBSCR                 
                876     LOAD_FAST                     6: df2
                878     LOAD_CONST                    38: 'L'
                880     STORE_SUBSCR                  
                882     LOAD_FAST                     4: df
                884     LOAD_CONST                    25: 'low'
                886     BINARY_SUBSCR                 
                888     LOAD_ATTR                     20: iloc
                890     LOAD_CONST                    34: -2
                892     BINARY_SUBSCR                 
                894     LOAD_FAST                     6: df2
                896     LOAD_CONST                    39: 'L1'
                898     STORE_SUBSCR                  
                900     LOAD_FAST                     4: df
                902     LOAD_CONST                    25: 'low'
                904     BINARY_SUBSCR                 
                906     LOAD_ATTR                     20: iloc
                908     LOAD_CONST                    36: -3
                910     BINARY_SUBSCR                 
                912     LOAD_FAST                     6: df2
                914     LOAD_CONST                    40: 'L2'
                916     STORE_SUBSCR                  
                918     LOAD_FAST                     6: df2
                920     LOAD_CONST                    41: 'ST'
                922     BINARY_SUBSCR                 
                924     LOAD_ATTR                     20: iloc
                926     LOAD_CONST                    19: -1
                928     BINARY_SUBSCR                 
                930     STORE_GLOBAL                  38: King_ST
                932     LOAD_FAST                     6: df2
                934     LOAD_CONST                    41: 'ST'
                936     BINARY_SUBSCR                 
                938     LOAD_ATTR                     20: iloc
                940     LOAD_CONST                    19: -1
                942     BINARY_SUBSCR                 
                944     STORE_GLOBAL                  39: Queen_ST
                946     LOAD_FAST                     6: df2
                948     LOAD_CONST                    26: 'close'
                950     BINARY_SUBSCR                 
                952     LOAD_ATTR                     20: iloc
                954     LOAD_CONST                    19: -1
                956     BINARY_SUBSCR                 
                958     STORE_GLOBAL                  40: Candle_Close
                960     LOAD_GLOBAL                   41: NULL + iloc
                962     LOAD_CONST                    1: False
                964     COMPARE_OP                    2 (==)
                966     POP_JUMP_IF_FALSE             598 (to 1196)
                970     LOAD_FAST                     6: df2
                972     LOAD_CONST                    33: 'H'
                974     BINARY_SUBSCR                 
                976     LOAD_ATTR                     20: iloc
                978     LOAD_CONST                    19: -1
                980     BINARY_SUBSCR                 
                982     LOAD_FAST                     6: df2
                984     LOAD_CONST                    35: 'H1'
                986     BINARY_SUBSCR                 
                988     LOAD_ATTR                     20: iloc
                990     LOAD_CONST                    19: -1
                992     BINARY_SUBSCR                 
                994     COMPARE_OP                    0 (<)
                996     POP_JUMP_IF_FALSE             598 (to 1196)
                1000    LOAD_FAST                     6: df2
                1002    LOAD_CONST                    35: 'H1'
                1004    BINARY_SUBSCR                 
                1006    LOAD_ATTR                     20: iloc
                1008    LOAD_CONST                    19: -1
                1010    BINARY_SUBSCR                 
                1012    LOAD_FAST                     6: df2
                1014    LOAD_CONST                    37: 'H2'
                1016    BINARY_SUBSCR                 
                1018    LOAD_ATTR                     20: iloc
                1020    LOAD_CONST                    19: -1
                1022    BINARY_SUBSCR                 
                1024    COMPARE_OP                    4 (>)
                1026    POP_JUMP_IF_FALSE             598 (to 1196)
                1030    LOAD_FAST                     6: df2
                1032    LOAD_CONST                    22: 'RSI'
                1034    BINARY_SUBSCR                 
                1036    LOAD_ATTR                     20: iloc
                1038    LOAD_CONST                    34: -2
                1040    BINARY_SUBSCR                 
                1042    LOAD_FAST                     6: df2
                1044    LOAD_CONST                    32: 'RSIH'
                1046    BINARY_SUBSCR                 
                1048    LOAD_ATTR                     20: iloc
                1050    LOAD_CONST                    19: -1
                1052    BINARY_SUBSCR                 
                1054    COMPARE_OP                    4 (>)
                1056    POP_JUMP_IF_FALSE             598 (to 1196)
                1060    LOAD_GLOBAL                   42: reset_index
                1062    LOAD_CONST                    12: 0
                1064    COMPARE_OP                    2 (==)
                1066    POP_JUMP_IF_TRUE              550 (to 1100)
                1070    LOAD_FAST                     6: df2
                1072    LOAD_CONST                    42: 'PDI'
                1074    BINARY_SUBSCR                 
                1076    LOAD_ATTR                     20: iloc
                1078    LOAD_CONST                    34: -2
                1080    BINARY_SUBSCR                 
                1082    LOAD_FAST                     6: df2
                1084    LOAD_CONST                    43: 'NDI'
                1086    BINARY_SUBSCR                 
                1088    LOAD_ATTR                     20: iloc
                1090    LOAD_CONST                    34: -2
                1092    BINARY_SUBSCR                 
                1094    COMPARE_OP                    4 (>)
                1096    POP_JUMP_IF_FALSE             598 (to 1196)
                1100    LOAD_FAST                     6: df2
                1102    LOAD_CONST                    35: 'H1'
                1104    BINARY_SUBSCR                 
                1106    LOAD_ATTR                     20: iloc
                1108    LOAD_CONST                    19: -1
                1110    BINARY_SUBSCR                 
                1112    STORE_GLOBAL                  43: First_King
                1114    LOAD_GLOBAL                   43: NULL + reset_index
                1116    STORE_GLOBAL                  44: King
                1118    LOAD_FAST                     6: df2
                1120    LOAD_CONST                    39: 'L1'
                1122    BINARY_SUBSCR                 
                1124    LOAD_ATTR                     20: iloc
                1126    LOAD_CONST                    19: -1
                1128    BINARY_SUBSCR                 
                1130    STORE_GLOBAL                  45: First_King_L
                1132    LOAD_GLOBAL                   46: rsi
                1134    LOAD_GLOBAL                   47: NULL + rsi
                1136    LOAD_GLOBAL                   43: NULL + reset_index
                1138    LOAD_GLOBAL                   48: close
                1140    BINARY_SUBTRACT               
                1142    LOAD_GLOBAL                   45: NULL + ta
                1144    CALL_FUNCTION                 2
                1146    LOAD_GLOBAL                   43: NULL + reset_index
                1148    LOAD_GLOBAL                   49: NULL + close
                1150    BINARY_SUBTRACT               
                1152    CALL_FUNCTION                 2
                1154    STORE_GLOBAL                  50: First_King_SL
                1156    LOAD_GLOBAL                   50: RSI_Period
                1158    STORE_GLOBAL                  51: King_SL
                1160    LOAD_CONST                    11: True
                1162    STORE_GLOBAL                  41: King_Candle_Formed
                1164    LOAD_CONST                    44: ' King Candle Formed ='
                1166    LOAD_GLOBAL                   43: NULL + reset_index
                1168    FORMAT_VALUE                  0
                1170    LOAD_CONST                    45: ', King_SL = '
                1172    LOAD_GLOBAL                   51: NULL + RSI_Period
                1174    FORMAT_VALUE                  0
                1176    LOAD_CONST                    46: ' '
                1178    BUILD_STRING                  5
                1180    STORE_FAST                    5: strMsg
                1182    LOAD_GLOBAL                   19: NULL + now
                1184    LOAD_FAST                     5: strMsg
                1186    LOAD_CONST                    7: 2
                1188    LOAD_CONST                    11: True
                1190    LOAD_CONST                    18: ('sendTeleMsg',)
                1192    CALL_FUNCTION_KW              3
                1194    POP_TOP                       
                1196    LOAD_GLOBAL                   52: adx
                1198    LOAD_CONST                    1: False
                1200    COMPARE_OP                    2 (==)
                1202    POP_JUMP_IF_FALSE             716 (to 1432)
                1206    LOAD_FAST                     6: df2
                1208    LOAD_CONST                    38: 'L'
                1210    BINARY_SUBSCR                 
                1212    LOAD_ATTR                     20: iloc
                1214    LOAD_CONST                    19: -1
                1216    BINARY_SUBSCR                 
                1218    LOAD_FAST                     6: df2
                1220    LOAD_CONST                    39: 'L1'
                1222    BINARY_SUBSCR                 
                1224    LOAD_ATTR                     20: iloc
                1226    LOAD_CONST                    19: -1
                1228    BINARY_SUBSCR                 
                1230    COMPARE_OP                    4 (>)
                1232    POP_JUMP_IF_FALSE             716 (to 1432)
                1236    LOAD_FAST                     6: df2
                1238    LOAD_CONST                    39: 'L1'
                1240    BINARY_SUBSCR                 
                1242    LOAD_ATTR                     20: iloc
                1244    LOAD_CONST                    19: -1
                1246    BINARY_SUBSCR                 
                1248    LOAD_FAST                     6: df2
                1250    LOAD_CONST                    40: 'L2'
                1252    BINARY_SUBSCR                 
                1254    LOAD_ATTR                     20: iloc
                1256    LOAD_CONST                    19: -1
                1258    BINARY_SUBSCR                 
                1260    COMPARE_OP                    0 (<)
                1262    POP_JUMP_IF_FALSE             716 (to 1432)
                1266    LOAD_FAST                     6: df2
                1268    LOAD_CONST                    22: 'RSI'
                1270    BINARY_SUBSCR                 
                1272    LOAD_ATTR                     20: iloc
                1274    LOAD_CONST                    34: -2
                1276    BINARY_SUBSCR                 
                1278    LOAD_FAST                     6: df2
                1280    LOAD_CONST                    31: 'RSIL'
                1282    BINARY_SUBSCR                 
                1284    LOAD_ATTR                     20: iloc
                1286    LOAD_CONST                    19: -1
                1288    BINARY_SUBSCR                 
                1290    COMPARE_OP                    0 (<)
                1292    POP_JUMP_IF_FALSE             716 (to 1432)
                1296    LOAD_GLOBAL                   42: reset_index
                1298    LOAD_CONST                    12: 0
                1300    COMPARE_OP                    2 (==)
                1302    POP_JUMP_IF_TRUE              668 (to 1336)
                1306    LOAD_FAST                     6: df2
                1308    LOAD_CONST                    43: 'NDI'
                1310    BINARY_SUBSCR                 
                1312    LOAD_ATTR                     20: iloc
                1314    LOAD_CONST                    34: -2
                1316    BINARY_SUBSCR                 
                1318    LOAD_FAST                     6: df2
                1320    LOAD_CONST                    42: 'PDI'
                1322    BINARY_SUBSCR                 
                1324    LOAD_ATTR                     20: iloc
                1326    LOAD_CONST                    34: -2
                1328    BINARY_SUBSCR                 
                1330    COMPARE_OP                    4 (>)
                1332    POP_JUMP_IF_FALSE             716 (to 1432)
                1336    LOAD_FAST                     6: df2
                1338    LOAD_CONST                    39: 'L1'
                1340    BINARY_SUBSCR                 
                1342    LOAD_ATTR                     20: iloc
                1344    LOAD_CONST                    19: -1
                1346    BINARY_SUBSCR                 
                1348    STORE_GLOBAL                  53: First_Queen
                1350    LOAD_GLOBAL                   53: NULL + adx
                1352    STORE_GLOBAL                  54: Queen
                1354    LOAD_FAST                     6: df2
                1356    LOAD_CONST                    35: 'H1'
                1358    BINARY_SUBSCR                 
                1360    LOAD_ATTR                     20: iloc
                1362    LOAD_CONST                    19: -1
                1364    BINARY_SUBSCR                 
                1366    STORE_GLOBAL                  55: First_Queen_H
                1368    LOAD_GLOBAL                   47: NULL + rsi
                1370    LOAD_GLOBAL                   46: rsi
                1372    LOAD_GLOBAL                   53: NULL + adx
                1374    LOAD_GLOBAL                   48: close
                1376    BINARY_ADD                    
                1378    LOAD_GLOBAL                   55: NULL + high
                1380    CALL_FUNCTION                 2
                1382    LOAD_GLOBAL                   53: NULL + adx
                1384    LOAD_GLOBAL                   49: NULL + close
                1386    BINARY_ADD                    
                1388    CALL_FUNCTION                 2
                1390    STORE_GLOBAL                  56: First_Queen_SL
                1392    LOAD_GLOBAL                   56: low
                1394    STORE_GLOBAL                  57: Queen_SL
                1396    LOAD_CONST                    11: True
                1398    STORE_GLOBAL                  52: Queen_Candle_Formed
                1400    LOAD_CONST                    47: ' Queen Candle Formed ='
                1402    LOAD_GLOBAL                   53: NULL + adx
                1404    FORMAT_VALUE                  0
                1406    LOAD_CONST                    48: ', Queen SL = '
                1408    LOAD_GLOBAL                   57: NULL + low
                1410    FORMAT_VALUE                  0
                1412    LOAD_CONST                    46: ' '
                1414    BUILD_STRING                  5
                1416    STORE_FAST                    5: strMsg
                1418    LOAD_GLOBAL                   19: NULL + now
                1420    LOAD_FAST                     5: strMsg
                1422    LOAD_CONST                    7: 2
                1424    LOAD_CONST                    11: True
                1426    LOAD_CONST                    18: ('sendTeleMsg',)
                1428    CALL_FUNCTION_KW              3
                1430    POP_TOP                       
                1432    LOAD_GLOBAL                   41: NULL + iloc
                1434    LOAD_CONST                    11: True
                1436    COMPARE_OP                    2 (==)
                1438    POP_JUMP_IF_FALSE             740 (to 1480)
                1442    LOAD_FAST                     6: df2
                1444    LOAD_CONST                    26: 'close'
                1446    BINARY_SUBSCR                 
                1448    LOAD_ATTR                     20: iloc
                1450    LOAD_CONST                    19: -1
                1452    BINARY_SUBSCR                 
                1454    LOAD_GLOBAL                   43: NULL + reset_index
                1456    COMPARE_OP                    0 (<)
                1458    POP_JUMP_IF_FALSE             740 (to 1480)
                1462    LOAD_GLOBAL                   58: ADX_Period
                1464    LOAD_CONST                    12: 0
                1466    COMPARE_OP                    2 (==)
                1468    POP_JUMP_IF_FALSE             740 (to 1480)
                1472    LOAD_GLOBAL                   43: NULL + reset_index
                1474    STORE_GLOBAL                  44: King
                1476    LOAD_GLOBAL                   45: NULL + ta
                1478    STORE_GLOBAL                  51: King_SL
                1480    LOAD_GLOBAL                   52: adx
                1482    LOAD_CONST                    11: True
                1484    COMPARE_OP                    2 (==)
                1486    POP_JUMP_IF_FALSE             764 (to 1528)
                1490    LOAD_FAST                     6: df2
                1492    LOAD_CONST                    26: 'close'
                1494    BINARY_SUBSCR                 
                1496    LOAD_ATTR                     20: iloc
                1498    LOAD_CONST                    19: -1
                1500    BINARY_SUBSCR                 
                1502    LOAD_GLOBAL                   53: NULL + adx
                1504    COMPARE_OP                    4 (>)
                1506    POP_JUMP_IF_FALSE             764 (to 1528)
                1510    LOAD_GLOBAL                   58: ADX_Period
                1512    LOAD_CONST                    12: 0
                1514    COMPARE_OP                    2 (==)
                1516    POP_JUMP_IF_FALSE             764 (to 1528)
                1520    LOAD_GLOBAL                   53: NULL + adx
                1522    STORE_GLOBAL                  54: Queen
                1524    LOAD_GLOBAL                   56: low
                1526    STORE_GLOBAL                  57: Queen_SL
                1528    LOAD_GLOBAL                   58: ADX_Period
                1530    LOAD_CONST                    2: 1
                1532    COMPARE_OP                    2 (==)
                1534    POP_JUMP_IF_FALSE             825 (to 1650)
                1538    LOAD_FAST                     6: df2
                1540    LOAD_CONST                    26: 'close'
                1542    BINARY_SUBSCR                 
                1544    LOAD_ATTR                     20: iloc
                1546    LOAD_CONST                    19: -1
                1548    BINARY_SUBSCR                 
                1550    LOAD_FAST                     6: df2
                1552    LOAD_CONST                    41: 'ST'
                1554    BINARY_SUBSCR                 
                1556    LOAD_ATTR                     20: iloc
                1558    LOAD_CONST                    19: -1
                1560    BINARY_SUBSCR                 
                1562    COMPARE_OP                    4 (>)
                1564    POP_JUMP_IF_FALSE             825 (to 1650)
                1568    LOAD_GLOBAL                   59: NULL + ADX_Period
                1570    LOAD_CONST                    49: 1000000
                1572    COMPARE_OP                    2 (==)
                1574    POP_JUMP_IF_FALSE             799 (to 1598)
                1578    LOAD_GLOBAL                   46: rsi
                1580    LOAD_FAST                     6: df2
                1582    LOAD_CONST                    24: 'high'
                1584    BINARY_SUBSCR                 
                1586    LOAD_ATTR                     20: iloc
                1588    LOAD_CONST                    19: -1
                1590    BINARY_SUBSCR                 
                1592    LOAD_GLOBAL                   44: ta
                1594    CALL_FUNCTION                 2
                1596    STORE_GLOBAL                  59: Latest_King
                1598    LOAD_GLOBAL                   46: rsi
                1600    LOAD_FAST                     6: df2
                1602    LOAD_CONST                    24: 'high'
                1604    BINARY_SUBSCR                 
                1606    LOAD_ATTR                     20: iloc
                1608    LOAD_CONST                    19: -1
                1610    BINARY_SUBSCR                 
                1612    LOAD_GLOBAL                   59: NULL + ADX_Period
                1614    CALL_FUNCTION                 2
                1616    STORE_GLOBAL                  59: Latest_King
                1618    LOAD_GLOBAL                   59: NULL + ADX_Period
                1620    STORE_GLOBAL                  44: King
                1622    LOAD_FAST                     6: df2
                1624    LOAD_CONST                    41: 'ST'
                1626    BINARY_SUBSCR                 
                1628    LOAD_ATTR                     20: iloc
                1630    LOAD_CONST                    19: -1
                1632    BINARY_SUBSCR                 
                1634    STORE_GLOBAL                  38: King_ST
                1636    LOAD_FAST                     6: df2
                1638    LOAD_CONST                    26: 'close'
                1640    BINARY_SUBSCR                 
                1642    LOAD_ATTR                     20: iloc
                1644    LOAD_CONST                    19: -1
                1646    BINARY_SUBSCR                 
                1648    STORE_GLOBAL                  40: Candle_Close
                1650    LOAD_GLOBAL                   58: ADX_Period
                1652    LOAD_CONST                    12: 0
                1654    COMPARE_OP                    2 (==)
                1656    POP_JUMP_IF_FALSE             856 (to 1712)
                1660    LOAD_GLOBAL                   44: ta
                1662    LOAD_GLOBAL                   59: NULL + ADX_Period
                1664    COMPARE_OP                    2 (==)
                1666    POP_JUMP_IF_FALSE             856 (to 1712)
                1670    LOAD_FAST                     6: df2
                1672    LOAD_CONST                    25: 'low'
                1674    BINARY_SUBSCR                 
                1676    LOAD_ATTR                     20: iloc
                1678    LOAD_CONST                    19: -1
                1680    BINARY_SUBSCR                 
                1682    STORE_GLOBAL                  60: Latest_King_L
                1684    LOAD_GLOBAL                   46: rsi
                1686    LOAD_GLOBAL                   47: NULL + rsi
                1688    LOAD_GLOBAL                   59: NULL + ADX_Period
                1690    LOAD_GLOBAL                   48: close
                1692    BINARY_SUBTRACT               
                1694    LOAD_GLOBAL                   60: supertrend
                1696    CALL_FUNCTION                 2
                1698    LOAD_GLOBAL                   59: NULL + ADX_Period
                1700    LOAD_GLOBAL                   49: NULL + close
                1702    BINARY_SUBTRACT               
                1704    CALL_FUNCTION                 2
                1706    STORE_GLOBAL                  61: Latest_King_SL
                1708    LOAD_GLOBAL                   61: NULL + supertrend
                1710    STORE_GLOBAL                  51: King_SL
                1712    LOAD_GLOBAL                   58: ADX_Period
                1714    LOAD_CONST                    19: -1
                1716    COMPARE_OP                    2 (==)
                1718    POP_JUMP_IF_FALSE             917 (to 1834)
                1722    LOAD_FAST                     6: df2
                1724    LOAD_CONST                    26: 'close'
                1726    BINARY_SUBSCR                 
                1728    LOAD_ATTR                     20: iloc
                1730    LOAD_CONST                    19: -1
                1732    BINARY_SUBSCR                 
                1734    LOAD_FAST                     6: df2
                1736    LOAD_CONST                    41: 'ST'
                1738    BINARY_SUBSCR                 
                1740    LOAD_ATTR                     20: iloc
                1742    LOAD_CONST                    19: -1
                1744    BINARY_SUBSCR                 
                1746    COMPARE_OP                    0 (<)
                1748    POP_JUMP_IF_FALSE             917 (to 1834)
                1752    LOAD_GLOBAL                   62: ST_Period
                1754    LOAD_CONST                    12: 0
                1756    COMPARE_OP                    2 (==)
                1758    POP_JUMP_IF_FALSE             891 (to 1782)
                1762    LOAD_GLOBAL                   47: NULL + rsi
                1764    LOAD_FAST                     6: df2
                1766    LOAD_CONST                    25: 'low'
                1768    BINARY_SUBSCR                 
                1770    LOAD_ATTR                     20: iloc
                1772    LOAD_CONST                    19: -1
                1774    BINARY_SUBSCR                 
                1776    LOAD_GLOBAL                   54: high
                1778    CALL_FUNCTION                 2
                1780    STORE_GLOBAL                  62: Latest_Queen
                1782    LOAD_GLOBAL                   47: NULL + rsi
                1784    LOAD_FAST                     6: df2
                1786    LOAD_CONST                    25: 'low'
                1788    BINARY_SUBSCR                 
                1790    LOAD_ATTR                     20: iloc
                1792    LOAD_CONST                    19: -1
                1794    BINARY_SUBSCR                 
                1796    LOAD_GLOBAL                   62: ST_Period
                1798    CALL_FUNCTION                 2
                1800    STORE_GLOBAL                  62: Latest_Queen
                1802    LOAD_GLOBAL                   62: ST_Period
                1804    STORE_GLOBAL                  54: Queen
                1806    LOAD_FAST                     6: df2
                1808    LOAD_CONST                    41: 'ST'
                1810    BINARY_SUBSCR                 
                1812    LOAD_ATTR                     20: iloc
                1814    LOAD_CONST                    19: -1
                1816    BINARY_SUBSCR                 
                1818    STORE_GLOBAL                  39: Queen_ST
                1820    LOAD_FAST                     6: df2
                1822    LOAD_CONST                    26: 'close'
                1824    BINARY_SUBSCR                 
                1826    LOAD_ATTR                     20: iloc
                1828    LOAD_CONST                    19: -1
                1830    BINARY_SUBSCR                 
                1832    STORE_GLOBAL                  40: Candle_Close
                1834    LOAD_GLOBAL                   58: ADX_Period
                1836    LOAD_CONST                    12: 0
                1838    COMPARE_OP                    2 (==)
                1840    POP_JUMP_IF_FALSE             948 (to 1896)
                1844    LOAD_GLOBAL                   54: high
                1846    LOAD_GLOBAL                   62: ST_Period
                1848    COMPARE_OP                    2 (==)
                1850    POP_JUMP_IF_FALSE             948 (to 1896)
                1854    LOAD_FAST                     6: df2
                1856    LOAD_CONST                    24: 'high'
                1858    BINARY_SUBSCR                 
                1860    LOAD_ATTR                     20: iloc
                1862    LOAD_CONST                    19: -1
                1864    BINARY_SUBSCR                 
                1866    STORE_GLOBAL                  63: Latest_Queen_H
                1868    LOAD_GLOBAL                   47: NULL + rsi
                1870    LOAD_GLOBAL                   46: rsi
                1872    LOAD_GLOBAL                   62: ST_Period
                1874    LOAD_GLOBAL                   48: close
                1876    BINARY_ADD                    
                1878    LOAD_GLOBAL                   63: NULL + ST_Period
                1880    CALL_FUNCTION                 2
                1882    LOAD_GLOBAL                   62: ST_Period
                1884    LOAD_GLOBAL                   49: NULL + close
                1886    BINARY_ADD                    
                1888    CALL_FUNCTION                 2
                1890    STORE_GLOBAL                  64: Latest_Queen_SL
                1892    LOAD_GLOBAL                   64: ST_Mult
                1894    STORE_GLOBAL                  57: Queen_SL
                1896    LOAD_GLOBAL                   41: NULL + iloc
                1898    POP_JUMP_IF_FALSE             994 (to 1988)
                1902    LOAD_CONST                    50: ' ==Direction : '
                1904    LOAD_GLOBAL                   58: ADX_Period
                1906    FORMAT_VALUE                  0
                1908    LOAD_CONST                    51: ', Close : '
                1910    LOAD_GLOBAL                   65: NULL + ST_Mult
                1912    LOAD_FAST                     6: df2
                1914    LOAD_CONST                    26: 'close'
                1916    BINARY_SUBSCR                 
                1918    LOAD_ATTR                     20: iloc
                1920    LOAD_CONST                    19: -1
                1922    BINARY_SUBSCR                 
                1924    LOAD_CONST                    2: 1
                1926    CALL_FUNCTION                 2
                1928    FORMAT_VALUE                  0
                1930    LOAD_CONST                    52: ', King : '
                1932    LOAD_GLOBAL                   44: ta
                1934    FORMAT_VALUE                  0
                1936    LOAD_CONST                    53: ', King Stop Loss : '
                1938    LOAD_GLOBAL                   65: NULL + ST_Mult
                1940    LOAD_GLOBAL                   51: NULL + RSI_Period
                1942    LOAD_CONST                    2: 1
                1944    CALL_FUNCTION                 2
                1946    FORMAT_VALUE                  0
                1948    LOAD_CONST                    54: ', ST : '
                1950    LOAD_GLOBAL                   65: NULL + ST_Mult
                1952    LOAD_FAST                     6: df2
                1954    LOAD_CONST                    41: 'ST'
                1956    BINARY_SUBSCR                 
                1958    LOAD_ATTR                     20: iloc
                1960    LOAD_CONST                    19: -1
                1962    BINARY_SUBSCR                 
                1964    LOAD_CONST                    2: 1
                1966    CALL_FUNCTION                 2
                1968    FORMAT_VALUE                  0
                1970    BUILD_STRING                  10
                1972    STORE_FAST                    5: strMsg
                1974    LOAD_GLOBAL                   19: NULL + now
                1976    LOAD_FAST                     5: strMsg
                1978    LOAD_CONST                    15: 6
                1980    LOAD_CONST                    1: False
                1982    LOAD_CONST                    18: ('sendTeleMsg',)
                1984    CALL_FUNCTION_KW              3
                1986    POP_TOP                       
                1988    LOAD_GLOBAL                   52: adx
                1990    POP_JUMP_IF_FALSE             1040 (to 2080)
                1994    LOAD_CONST                    50: ' ==Direction : '
                1996    LOAD_GLOBAL                   58: ADX_Period
                1998    FORMAT_VALUE                  0
                2000    LOAD_CONST                    51: ', Close : '
                2002    LOAD_GLOBAL                   65: NULL + ST_Mult
                2004    LOAD_FAST                     6: df2
                2006    LOAD_CONST                    26: 'close'
                2008    BINARY_SUBSCR                 
                2010    LOAD_ATTR                     20: iloc
                2012    LOAD_CONST                    19: -1
                2014    BINARY_SUBSCR                 
                2016    LOAD_CONST                    2: 1
                2018    CALL_FUNCTION                 2
                2020    FORMAT_VALUE                  0
                2022    LOAD_CONST                    55: ', Queen : '
                2024    LOAD_GLOBAL                   54: high
                2026    FORMAT_VALUE                  0
                2028    LOAD_CONST                    56: ', Queen Stop Loss : '
                2030    LOAD_GLOBAL                   65: NULL + ST_Mult
                2032    LOAD_GLOBAL                   57: NULL + low
                2034    LOAD_CONST                    2: 1
                2036    CALL_FUNCTION                 2
                2038    FORMAT_VALUE                  0
                2040    LOAD_CONST                    54: ', ST : '
                2042    LOAD_GLOBAL                   65: NULL + ST_Mult
                2044    LOAD_FAST                     6: df2
                2046    LOAD_CONST                    41: 'ST'
                2048    BINARY_SUBSCR                 
                2050    LOAD_ATTR                     20: iloc
                2052    LOAD_CONST                    19: -1
                2054    BINARY_SUBSCR                 
                2056    LOAD_CONST                    2: 1
                2058    CALL_FUNCTION                 2
                2060    FORMAT_VALUE                  0
                2062    BUILD_STRING                  10
                2064    STORE_FAST                    5: strMsg
                2066    LOAD_GLOBAL                   19: NULL + now
                2068    LOAD_FAST                     5: strMsg
                2070    LOAD_CONST                    15: 6
                2072    LOAD_CONST                    1: False
                2074    LOAD_CONST                    18: ('sendTeleMsg',)
                2076    CALL_FUNCTION_KW              3
                2078    POP_TOP                       
                2080    LOAD_CONST                    50: ' ==Direction : '
                2082    LOAD_GLOBAL                   58: ADX_Period
                2084    FORMAT_VALUE                  0
                2086    LOAD_CONST                    51: ', Close : '
                2088    LOAD_GLOBAL                   65: NULL + ST_Mult
                2090    LOAD_FAST                     6: df2
                2092    LOAD_CONST                    26: 'close'
                2094    BINARY_SUBSCR                 
                2096    LOAD_ATTR                     20: iloc
                2098    LOAD_CONST                    19: -1
                2100    BINARY_SUBSCR                 
                2102    LOAD_CONST                    2: 1
                2104    CALL_FUNCTION                 2
                2106    FORMAT_VALUE                  0
                2108    LOAD_CONST                    57: ', RSI : '
                2110    LOAD_GLOBAL                   65: NULL + ST_Mult
                2112    LOAD_FAST                     6: df2
                2114    LOAD_CONST                    22: 'RSI'
                2116    BINARY_SUBSCR                 
                2118    LOAD_ATTR                     20: iloc
                2120    LOAD_CONST                    19: -1
                2122    BINARY_SUBSCR                 
                2124    LOAD_CONST                    2: 1
                2126    CALL_FUNCTION                 2
                2128    FORMAT_VALUE                  0
                2130    LOAD_CONST                    58: ', PDI : '
                2132    LOAD_GLOBAL                   65: NULL + ST_Mult
                2134    LOAD_FAST                     6: df2
                2136    LOAD_CONST                    42: 'PDI'
                2138    BINARY_SUBSCR                 
                2140    LOAD_ATTR                     20: iloc
                2142    LOAD_CONST                    19: -1
                2144    BINARY_SUBSCR                 
                2146    LOAD_CONST                    2: 1
                2148    CALL_FUNCTION                 2
                2150    FORMAT_VALUE                  0
                2152    LOAD_CONST                    59: ', NDI : '
                2154    LOAD_GLOBAL                   65: NULL + ST_Mult
                2156    LOAD_FAST                     6: df2
                2158    LOAD_CONST                    43: 'NDI'
                2160    BINARY_SUBSCR                 
                2162    LOAD_ATTR                     20: iloc
                2164    LOAD_CONST                    19: -1
                2166    BINARY_SUBSCR                 
                2168    LOAD_CONST                    2: 1
                2170    CALL_FUNCTION                 2
                2172    FORMAT_VALUE                  0
                2174    LOAD_CONST                    60: ', H : '
                2176    LOAD_GLOBAL                   65: NULL + ST_Mult
                2178    LOAD_FAST                     6: df2
                2180    LOAD_CONST                    33: 'H'
                2182    BINARY_SUBSCR                 
                2184    LOAD_ATTR                     20: iloc
                2186    LOAD_CONST                    19: -1
                2188    BINARY_SUBSCR                 
                2190    LOAD_CONST                    2: 1
                2192    CALL_FUNCTION                 2
                2194    FORMAT_VALUE                  0
                2196    LOAD_CONST                    61: ', H1 : '
                2198    LOAD_GLOBAL                   65: NULL + ST_Mult
                2200    LOAD_FAST                     6: df2
                2202    LOAD_CONST                    35: 'H1'
                2204    BINARY_SUBSCR                 
                2206    LOAD_ATTR                     20: iloc
                2208    LOAD_CONST                    19: -1
                2210    BINARY_SUBSCR                 
                2212    LOAD_CONST                    2: 1
                2214    CALL_FUNCTION                 2
                2216    FORMAT_VALUE                  0
                2218    LOAD_CONST                    62: ', H2 : '
                2220    LOAD_GLOBAL                   65: NULL + ST_Mult
                2222    LOAD_FAST                     6: df2
                2224    LOAD_CONST                    37: 'H2'
                2226    BINARY_SUBSCR                 
                2228    LOAD_ATTR                     20: iloc
                2230    LOAD_CONST                    19: -1
                2232    BINARY_SUBSCR                 
                2234    LOAD_CONST                    2: 1
                2236    CALL_FUNCTION                 2
                2238    FORMAT_VALUE                  0
                2240    LOAD_CONST                    63: ',  L : '
                2242    LOAD_GLOBAL                   65: NULL + ST_Mult
                2244    LOAD_FAST                     6: df2
                2246    LOAD_CONST                    38: 'L'
                2248    BINARY_SUBSCR                 
                2250    LOAD_ATTR                     20: iloc
                2252    LOAD_CONST                    19: -1
                2254    BINARY_SUBSCR                 
                2256    LOAD_CONST                    2: 1
                2258    CALL_FUNCTION                 2
                2260    FORMAT_VALUE                  0
                2262    LOAD_CONST                    64: ', L1 : '
                2264    LOAD_GLOBAL                   65: NULL + ST_Mult
                2266    LOAD_FAST                     6: df2
                2268    LOAD_CONST                    39: 'L1'
                2270    BINARY_SUBSCR                 
                2272    LOAD_ATTR                     20: iloc
                2274    LOAD_CONST                    19: -1
                2276    BINARY_SUBSCR                 
                2278    LOAD_CONST                    2: 1
                2280    CALL_FUNCTION                 2
                2282    FORMAT_VALUE                  0
                2284    LOAD_CONST                    65: ', L2 : '
                2286    LOAD_GLOBAL                   65: NULL + ST_Mult
                2288    LOAD_FAST                     6: df2
                2290    LOAD_CONST                    40: 'L2'
                2292    BINARY_SUBSCR                 
                2294    LOAD_ATTR                     20: iloc
                2296    LOAD_CONST                    19: -1
                2298    BINARY_SUBSCR                 
                2300    LOAD_CONST                    2: 1
                2302    CALL_FUNCTION                 2
                2304    FORMAT_VALUE                  0
                2306    BUILD_STRING                  22
                2308    STORE_FAST                    5: strMsg
                2310    LOAD_GLOBAL                   19: NULL + now
                2312    LOAD_FAST                     5: strMsg
                2314    LOAD_CONST                    15: 6
                2316    LOAD_CONST                    1: False
                2318    LOAD_CONST                    18: ('sendTeleMsg',)
                2320    CALL_FUNCTION_KW              3
                2322    POP_TOP                       
                2324    POP_BLOCK                     
                2326    LOAD_CONST                    0: None
                2328    RETURN_VALUE                  
                2330    DUP_TOP                       
                2332    LOAD_GLOBAL                   66: index
                2334    JUMP_IF_NOT_EXC_MATCH         1195 (to 2390)
                2338    POP_TOP                       
                2340    STORE_FAST                    7: ex
                2342    POP_TOP                       
                2344    SETUP_FINALLY                 18 (to 2382)
                2346    LOAD_GLOBAL                   19: NULL + now
                2348    LOAD_CONST                    66: ' Exception occured in King Candle Calculation:'
                2350    LOAD_GLOBAL                   6: Trade_FinNifty
                2352    LOAD_FAST                     7: ex
                2354    CALL_FUNCTION                 1
                2356    BINARY_ADD                    
                2358    LOAD_CONST                    10: 3
                2360    LOAD_CONST                    11: True
                2362    LOAD_CONST                    18: ('sendTeleMsg',)
                2364    CALL_FUNCTION_KW              3
                2366    POP_TOP                       
                2368    POP_BLOCK                     
                2370    POP_EXCEPT                    
                2372    LOAD_CONST                    0: None
                2374    STORE_FAST                    7: ex
                2376    DELETE_FAST                   7: ex
                2378    LOAD_CONST                    0: None
                2380    RETURN_VALUE                  
                2382    LOAD_CONST                    0: None
                2384    STORE_FAST                    7: ex
                2386    DELETE_FAST                   7: ex
                2388    RERAISE                       1
                2390    RERAISE                       0
        'King_candle'
        