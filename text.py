[Code]
            File Name: Algo_Finv.py
            Object Name: close_callback
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Locals: 0
            Stack Size: 2
            Flags: 0x00000043 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)
            [Names]
                'iLog'
            [Var Names]
            [Free Vars]
            [Cell Vars]
            [Constants]
                None
                ' In close_callback().'
            [Disassembly]
                0       LOAD_GLOBAL                   0: iLog
                2       LOAD_CONST                    1: ' In close_callback().'
                4       CALL_FUNCTION                 1
                6       POP_TOP                       
                8       LOAD_CONST                    0: None
                10      RETURN_VALUE                  
        'close_callback'
        'Username'
        'Algo_King'
        ' Shutter down... Calling sys.exit() @ '
        ' User = '
        'holidays.json'
        'r'
        3
        7
        (
            'days'
        )
        ' Expiry Date = '
        '%d%b%y'
        ' Today is market holiday. Stopping Algo for the day'
        ' Algo_Trading flag Disabled or no of lots set to zero. No trading for the day'
        ' Only one of these flag should be set to 1, check settings and restart: Trade_Nifty,Trade_BankNifty,Trade_FinNifty'
        (
            'INI_FILE'
        )
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
        'Nifty Bank'
        ' get_instrument_by_symbol: Exception='
        ' Exiting Algo'
        ' Starting Websocket.'
        (
            'order_update_callback'
            'subscribe_callback'
            'socket_open_callback'
        )
        'ExitTradenow'
        5
        ' get_option_tokens(): Exception='
        ' Waiting for First Short Straddle time'
        '%H%M%S'
        -1
        ' Wait_for_movement enabled. Short straddle will be triggered when LTP '
        ' move '
        ' UP or '
        ' down points before '
        ' Hrs'
        ' Max Entry time exceeded. Exiting Algo'
        ' Max Entry time Reached. Skipping wait for movement'
        ' Current LTP : '
        ', Starting LTP : '
        ', Pos Difference (Cur,Req) : ('
        ','
        '), Neg Difference (Cur,Req) : ('
        ')'
        ' Wait for premium enabled. Short straddle will be triggered when LTP current difference '
        ' is close to ATM strike by '
        ' Required Premium difference : '
        ' Starting tick processing.'
        'BANK'
        ' Place Hedge order for Short Straddle for CE/PE Strike=('
        '), ATM(CE,PE)=('
        ', '
        ') '
        'CE'
        'PE'
        ' Place First Short Straddle order for CE/PE ATM Strike=('
        'B'
        'norenordno'
        'stat'
        'REJECTED'
        ' Error in Order Placement Ord_ID = '
        ', Ord_STS = '
        ', Ret_STS = '
        '.Exiting Algo'
        ' Exiting Algo.Cross Check for any Open positions'
        'COMPLETE'
        ' Placed First Hedge CE Buy Market order Stike: '
        ' ATM CE='
        ', Qty ='
        ', Ord_ID = '
        'Buy'
        '.'
        ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        ' Placed First Hedge PE Buy Market order Stike: '
        ' ATM PE='
        'S'
        ' Placed First ATM SS CE Sell Market order Stike: '
        'Sell'
        ' Placed First ATM SS PE Sell Market order Stike: '
        'NQ'
        ' CE Leg Stoploss/Target reached : Max order_limit_per_day Reached. Exiting trade for the day '
        ' CE Leg Stoploss/Target reached : Position change after MaxPositionChangeTime. Exiting trade for the day '
        ' CE Leg Target Reached: (Current,Target) = ('
        ') Strike (Old,New) = ('
        ') Starting New ATM CE Tick processing.'
        ' CE Leg Stop Loss Reached: (Current,SL) = ('
        '  Place Buy order for Closing Existing '
        ' CE at '
        'CEC'
        '  Place SELL order for new  '
        ' Placed CE Buy Market order for ATM Strike='
        ', ATM CE='
        ' Placed CE Sell Market order for ATM Strike='
        ' CE Leg Re-entry Triggered : Max order_limit_per_day Reached. Exiting trade for the day '
        ' CE Leg Re-entry Triggered : Position change after MaxPositionChangeTime. Exiting trade for the day '
        ' CE Leg Re-entry triggered (LTP,ATM_CE_Strike,ATM_PE_Strike,Delta_Limit,Actual_Delta): ('
        '  Place SELL order for  '
        ' PE Leg Stoploss/Target reached : Max order_limit_per_day Reached. Exiting trade for the day '
        ' PE Leg Stoploss/Target reached : Position change after MaxPositionChangeTime. Exiting trade for the day '
        ' PE Leg Target Reached: (Current,Target) =  ('
        ' PE Leg Stoploss Reached: (Current,SL) =  ('
        ' PE at '
        'PEF'
        ' Placed PE Buy Market order for ATM Strike='
        ', ATM PE='
        ' Placed PE Sell Market order for ATM Strike='
        ' PE Leg Re-entry triggered : Max order_limit_per_day Reached. Exiting trade for the day '
        ' PE Leg Re-entry triggered : Position change after MaxPositionChangeTime. Exiting trade for the day '
        ' PE Leg Re-entry triggered (LTP,ATM_CE_Strike,ATM_PE_Strike,Delta_Limit,Actual_Delta): ('
        '  Place SELL order for '
        'MTM'
        2000
        ' ExitTime Triggered : closing all Trades'
        '_Current_legs.txt'
        '_Current_legs_hedge.txt'
        './PNL/'
        '_PNL.txt'
        ''
        (
            'newline'
        )
        ' Current LTP = '
        ' ATM CE = ('
        '), '
        ' ATM PE = ('
        '),MTM SL='
        ',MTM TGT='
        ', Calc MTM = '
        ' Legs(CE,PE)=('
        ') LTP= '
        ' ATM CE=('
        '),'
        ',MTM= '
        ' Reentry LTP : '
        ' , '
        '  ATM CE=('
        '  ATM PE=('
        ' LTP = '
        ' ATM CE = '
        ' ATM PE = '
        ' Direction change: Max order_limit_per_day Reached. Exiting trade for the day '
        ' Direction change after MaxPositionChangeTime. Exiting trade for the day '
        9
        55
        10
        ' King Candle Breakout LTP = '
        ', higher than King Candle= '
        ' '
        ' Queen Candle Breakout LTP ='
        ', lower than Queen Candle= '
        '  Place CE Buy order for '
        '  Place CE Buy order for addtional '
        '  Place PE Buy order for '
        '  Place PE Buy order for addtional '
        ' King Stoploss triggered : Max order_limit_per_day Reached. Exiting trade for the day '
        ' King Stoploss triggered : Position change after MaxPositionChangeTime. Exiting trade for the day '
        ' King Candle SL Hit LTP = '
        ', lower than King SL= '
        ' King Candle SuperTrend SL Hit Candle Close = '
        ', lower than King SuperTrend SL= '
        ' King Candle SuperTrend SL Hit LTP = '
        '  Place SELL order for Closing Existing '
        '  Place SELL order for new '
        ' Queen Stoploss triggered : Max order_limit_per_day Reached. Exiting trade for the day '
        ' Queen Stoploss triggered : Position change after MaxPositionChangeTime. Exiting trade for the day '
        ' Queen Candle SL Hit LTP = '
        ', higher than Queen SL= '
        ' Queen Candle SuperTrend SL Hit Candle Close = '
        ', higher than Queen SuperTrend SL= '
        ' Queen Candle SuperTrend SL LTP = '
        '  Place Sell order for Closing Existing '
        30
        ' CE LTP '
        ' not updating for 1 Mins:'
        60
        ' not updating for 2 Mins:'
        90
        ' not updating for 3 Mins:'
        120
        ' not updating for 4 Mins:'
        150
        ' not updating for more than 5 Mins: Consider exiting Algo manually'
        300
        ' not updating for more than 10 Mins: Consider exiting Algo manually'
        ' not updating for '
        ' Secs: ExitTradenow Triggered : closing all Trades'
        ' PE LTP '
        ' ExitTradenow Triggered : closing all Trades'
        2
        'Processing time(secs)= {0:.2f}'
        1530
        1532
        './log/df_king.json'
        'records'
        'infer'
        'true'
        (
            'orient'
            'compression'
            'index'
        )
        './log/df_runtime.json'
        (
            1
            False
        )
        (
            True
        )
        (
            'tokens'
            'Settings.ini'
        )
        (
            'BANKNIFTY'
            '22022022'
            False
            37000
            True
        )
        (
            'NSE'
            'NIFTY BANK'
        )
        (
            'NFO'
            260105
        )
        (
            'NIFTY'
            33000
            75
            '01SEP22'
        )
        (
            'ALL'
        )
        (
            False
        )
    [Disassembly]
        0       LOAD_CONST                    0: 0
        2       LOAD_CONST                    1: None
        4       IMPORT_NAME                   0: sys
        6       STORE_NAME                    0: sys
        8       LOAD_CONST                    0: 0
        10      LOAD_CONST                    1: None
        12      IMPORT_NAME                   1: os
        14      STORE_NAME                    1: os
        16      LOAD_CONST                    0: 0
        18      LOAD_CONST                    1: None
        20      IMPORT_NAME                   2: time
        22      STORE_NAME                    2: time
        24      LOAD_CONST                    0: 0
        26      LOAD_CONST                    1: None
        28      IMPORT_NAME                   3: threading
        30      STORE_NAME                    3: threading
        32      LOAD_CONST                    0: 0
        34      LOAD_CONST                    1: None
        36      IMPORT_NAME                   4: math
        38      STORE_NAME                    4: math
        40      LOAD_CONST                    0: 0
        42      LOAD_CONST                    1: None
        44      IMPORT_NAME                   5: json
        46      STORE_NAME                    5: json
        48      LOAD_CONST                    0: 0
        50      LOAD_CONST                    1: None
        52      IMPORT_NAME                   6: calendar
        54      STORE_NAME                    6: calendar
        56      LOAD_CONST                    0: 0
        58      LOAD_CONST                    2: ('writer',)
        60      IMPORT_NAME                   7: csv
        62      IMPORT_FROM                   8: writer
        64      STORE_NAME                    8: writer
        66      POP_TOP                       
        68      LOAD_CONST                    0: 0
        70      LOAD_CONST                    1: None
        72      IMPORT_NAME                   9: base64
        74      STORE_NAME                    9: base64
        76      LOAD_CONST                    0: 0
        78      LOAD_CONST                    1: None
        80      IMPORT_NAME                   10: dateutil.parser
        82      STORE_NAME                    11: dateutil
        84      LOAD_CONST                    0: 0
        86      LOAD_CONST                    3: ('add_all_ta_features',)
        88      IMPORT_NAME                   12: ta
        90      IMPORT_FROM                   13: add_all_ta_features
        92      STORE_NAME                    13: add_all_ta_features
        94      POP_TOP                       
        96      LOAD_CONST                    0: 0
        98      LOAD_CONST                    4: ('dropna',)
        100     IMPORT_NAME                   14: ta.utils
        102     IMPORT_FROM                   15: dropna
        104     STORE_NAME                    15: dropna
        106     POP_TOP                       
        108     LOAD_CONST                    0: 0
        110     LOAD_CONST                    1: None
        112     IMPORT_NAME                   16: pandas_ta
        114     STORE_NAME                    12: ta
        116     LOAD_CONST                    0: 0
        118     LOAD_CONST                    5: ('tabulate',)
        120     IMPORT_NAME                   17: tabulate
        122     IMPORT_FROM                   17: tabulate
        124     STORE_NAME                    17: tabulate
        126     POP_TOP                       
        128     LOAD_CONST                    0: 0
        130     LOAD_CONST                    6: ('NorenApi',)
        132     IMPORT_NAME                   18: NorenApi
        134     IMPORT_FROM                   18: NorenApi
        136     STORE_NAME                    18: NorenApi
        138     POP_TOP                       
        140     LOAD_CONST                    0: 0
        142     LOAD_CONST                    1: None
        144     IMPORT_NAME                   19: yaml
        146     STORE_NAME                    19: yaml
        148     LOAD_CONST                    0: 0
        150     LOAD_CONST                    1: None
        152     IMPORT_NAME                   20: configparser
        154     STORE_NAME                    20: configparser
        156     LOAD_CONST                    0: 0
        158     LOAD_CONST                    1: None
        160     IMPORT_NAME                   21: datetime
        162     STORE_NAME                    21: datetime
        164     LOAD_CONST                    0: 0
        166     LOAD_CONST                    1: None
        168     IMPORT_NAME                   22: requests
        170     STORE_NAME                    22: requests
        172     LOAD_CONST                    0: 0
        174     LOAD_CONST                    1: None
        176     IMPORT_NAME                   23: pandas
        178     STORE_NAME                    24: pd
        180     LOAD_CONST                    0: 0
        182     LOAD_CONST                    1: None
        184     IMPORT_NAME                   25: numpy
        186     STORE_NAME                    26: np
        188     LOAD_CONST                    0: 0
        190     LOAD_CONST                    7: ('relativedelta', 'FR')
        192     IMPORT_NAME                   27: dateutil.relativedelta
        194     IMPORT_FROM                   28: relativedelta
        196     STORE_NAME                    28: relativedelta
        198     IMPORT_FROM                   29: FR
        200     STORE_NAME                    29: FR
        202     POP_TOP                       
        204     LOAD_CONST                    0: 0
        206     LOAD_CONST                    1: None
        208     IMPORT_NAME                   2: time
        210     STORE_NAME                    2: time
        212     LOAD_CONST                    0: 0
        214     LOAD_CONST                    1: None
        216     IMPORT_NAME                   30: ctypes
        218     STORE_NAME                    30: ctypes
        220     LOAD_NAME                     18: NorenApi
        222     CALL_FUNCTION                 0
        224     STORE_GLOBAL                  31: api
        226     LOAD_CONST                    1: None
        228     LOAD_NAME                     24: pd
        230     LOAD_ATTR                     32: options
        232     LOAD_ATTR                     33: mode
        234     STORE_ATTR                    34: chained_assignment
        236     LOAD_CONST                    8: 'Settings.ini'
        238     STORE_NAME                    35: INI_FILE
        240     LOAD_NAME                     20: configparser
        242     LOAD_METHOD                   36: ConfigParser
        244     CALL_METHOD                   0
        246     STORE_GLOBAL                  37: cfg
        248     LOAD_GLOBAL                   37: NULL + NorenApi
        250     LOAD_METHOD                   38: read
        252     LOAD_NAME                     35: INI_FILE
        254     CALL_METHOD                   1
        256     POP_TOP                       
        258     LOAD_GLOBAL                   37: NULL + NorenApi
        260     LOAD_METHOD                   39: get
        262     LOAD_CONST                    9: 'tokens'
        264     LOAD_CONST                    10: 'admin_chat_id'
        266     CALL_METHOD                   2
        268     STORE_NAME                    40: strAdminChatID
        270     LOAD_GLOBAL                   37: NULL + NorenApi
        272     LOAD_METHOD                   39: get
        274     LOAD_CONST                    9: 'tokens'
        276     LOAD_CONST                    11: 'chat_id'
        278     CALL_METHOD                   2
        280     STORE_NAME                    41: strChatID
        282     LOAD_CONST                    12: 'bot'
        284     LOAD_GLOBAL                   37: NULL + NorenApi
        286     LOAD_METHOD                   39: get
        288     LOAD_CONST                    9: 'tokens'
        290     LOAD_CONST                    13: 'bot_token'
        292     CALL_METHOD                   2
        294     BINARY_ADD                    
        296     STORE_NAME                    42: strBotToken
        298     LOAD_GLOBAL                   37: NULL + NorenApi
        300     LOAD_METHOD                   39: get
        302     LOAD_CONST                    9: 'tokens'
        304     LOAD_CONST                    13: 'bot_token'
        306     CALL_METHOD                   2
        308     STORE_NAME                    43: strBotTokenWObot
        310     LOAD_NAME                     44: int
        312     LOAD_GLOBAL                   37: NULL + NorenApi
        314     LOAD_METHOD                   39: get
        316     LOAD_CONST                    14: 'general'
        318     LOAD_CONST                    15: 'send_telegram'
        320     CALL_METHOD                   2
        322     CALL_FUNCTION                 1
        324     STORE_GLOBAL                  45: Send_Telegram
        326     LOAD_GLOBAL                   37: NULL + NorenApi
        328     LOAD_METHOD                   39: get
        330     LOAD_CONST                    9: 'tokens'
        332     LOAD_CONST                    16: 'log_file_name'
        334     CALL_METHOD                   2
        336     STORE_GLOBAL                  46: log_file_name
        338     LOAD_NAME                     44: int
        340     LOAD_GLOBAL                   37: NULL + NorenApi
        342     LOAD_METHOD                   39: get
        344     LOAD_CONST                    9: 'tokens'
        346     LOAD_CONST                    17: 'login_token'
        348     CALL_METHOD                   2
        350     CALL_FUNCTION                 1
        352     STORE_NAME                    47: login_token
        354     LOAD_GLOBAL                   46: pandas
        356     FORMAT_VALUE                  0
        358     LOAD_CONST                    18: " Started. Don't Close this Window."
        360     BUILD_STRING                  2
        362     STORE_NAME                    48: strLogText
        364     LOAD_NAME                     49: print
        366     LOAD_CONST                    19: '{}|{}'
        368     LOAD_METHOD                   50: format
        370     LOAD_NAME                     21: datetime
        372     LOAD_ATTR                     21: datetime
        374     LOAD_METHOD                   51: now
        376     CALL_METHOD                   0
        378     LOAD_NAME                     48: strLogText
        380     CALL_METHOD                   2
        382     LOAD_CONST                    20: True
        384     LOAD_CONST                    21: ('flush',)
        386     CALL_FUNCTION_KW              2
        388     POP_TOP                       
        390     LOAD_CONST                    22: 'Refer ./log/'
        392     LOAD_GLOBAL                   46: pandas
        394     FORMAT_VALUE                  0
        396     LOAD_CONST                    23: '_'
        398     LOAD_NAME                     21: datetime
        400     LOAD_ATTR                     21: datetime
        402     LOAD_METHOD                   51: now
        404     CALL_METHOD                   0
        406     LOAD_METHOD                   52: strftime
        408     LOAD_CONST                    24: '%Y%m%d'
        410     CALL_METHOD                   1
        412     FORMAT_VALUE                  0
        414     LOAD_CONST                    25: '.log for Continuous Update'
        416     BUILD_STRING                  5
        418     STORE_NAME                    48: strLogText
        420     LOAD_NAME                     49: print
        422     LOAD_CONST                    19: '{}|{}'
        424     LOAD_METHOD                   50: format
        426     LOAD_NAME                     21: datetime
        428     LOAD_ATTR                     21: datetime
        430     LOAD_METHOD                   51: now
        432     CALL_METHOD                   0
        434     LOAD_NAME                     48: strLogText
        436     CALL_METHOD                   2
        438     LOAD_CONST                    20: True
        440     LOAD_CONST                    21: ('flush',)
        442     CALL_FUNCTION_KW              2
        444     POP_TOP                       
        446     SETUP_FINALLY                 9 (to 466)
        448     LOAD_NAME                     30: ctypes
        450     LOAD_ATTR                     53: windll
        452     LOAD_ATTR                     54: kernel32
        454     LOAD_METHOD                   55: SetConsoleTitleW
        456     LOAD_GLOBAL                   46: pandas
        458     CALL_METHOD                   1
        460     POP_TOP                       
        462     POP_BLOCK                     
        464     JUMP_FORWARD                  4 (to 474)
        466     POP_TOP                       
        468     POP_TOP                       
        470     POP_TOP                       
        472     POP_EXCEPT                    
        474     LOAD_NAME                     56: open
        476     LOAD_CONST                    26: './log/'
        478     LOAD_GLOBAL                   46: pandas
        480     BINARY_ADD                    
        482     LOAD_CONST                    23: '_'
        484     BINARY_ADD                    
        486     LOAD_NAME                     21: datetime
        488     LOAD_ATTR                     21: datetime
        490     LOAD_METHOD                   51: now
        492     CALL_METHOD                   0
        494     LOAD_METHOD                   52: strftime
        496     LOAD_CONST                    24: '%Y%m%d'
        498     CALL_METHOD                   1
        500     BINARY_ADD                    
        502     LOAD_CONST                    27: '.log'
        504     BINARY_ADD                    
        506     LOAD_CONST                    28: 'a'
        508     CALL_FUNCTION                 2
        510     DUP_TOP                       
        512     LOAD_NAME                     0: sys
        514     STORE_ATTR                    57: stdout
        516     LOAD_NAME                     0: sys
        518     STORE_ATTR                    58: stderr
        520     LOAD_CONST                    458: (1, False)
        524     LOAD_CONST                    31: <CODE> iLog
        526     LOAD_CONST                    32: 'iLog'
        528     MAKE_FUNCTION                 1
        530     STORE_NAME                    59: iLog
        532     LOAD_BUILD_CLASS              
        534     LOAD_CONST                    33: <CODE> TradeLog
        536     LOAD_CONST                    34: 'TradeLog'
        538     MAKE_FUNCTION                 0
        540     LOAD_CONST                    34: 'TradeLog'
        542     CALL_FUNCTION                 2
        544     STORE_NAME                    60: TradeLog
        546     LOAD_CONST                    35: <CODE> set_config_value
        548     LOAD_CONST                    36: 'set_config_value'
        550     MAKE_FUNCTION                 0
        552     STORE_NAME                    61: set_config_value
        554     LOAD_CONST                    459: (True,)
        558     LOAD_CONST                    37: <CODE> savedata
        560     LOAD_CONST                    38: 'savedata'
        562     MAKE_FUNCTION                 1
        564     STORE_NAME                    62: savedata
        566     LOAD_CONST                    460: ('tokens', 'Settings.ini')
        570     LOAD_CONST                    39: <CODE> getAccessToken
        572     LOAD_CONST                    40: 'getAccessToken'
        574     MAKE_FUNCTION                 1
        576     STORE_NAME                    63: getAccessToken
        578     LOAD_CONST                    41: ' Initialising '
        580     LOAD_NAME                     64: __file__
        582     BINARY_ADD                    
        584     STORE_NAME                    65: strMsg
        586     LOAD_NAME                     59: iLog
        588     LOAD_NAME                     65: strMsg
        590     LOAD_CONST                    42: 4
        592     LOAD_CONST                    20: True
        594     LOAD_CONST                    43: ('sendTeleMsg',)
        596     CALL_FUNCTION_KW              3
        598     POP_TOP                       
        600     LOAD_NAME                     56: open
        602     LOAD_CONST                    44: 'cred.yml'
        604     CALL_FUNCTION                 1
        606     SETUP_WITH                    16
        608     STORE_NAME                    66: f
        610     LOAD_NAME                     19: yaml
        612     LOAD_ATTR                     67: load
        614     LOAD_NAME                     66: f
        616     LOAD_NAME                     19: yaml
        618     LOAD_ATTR                     68: FullLoader
        620     LOAD_CONST                    45: ('Loader',)
        622     CALL_FUNCTION_KW              2
        624     STORE_NAME                    69: cred
        626     POP_BLOCK                     
        628     LOAD_CONST                    1: None
        630     DUP_TOP                       
        632     DUP_TOP                       
        634     CALL_FUNCTION                 3
        636     POP_TOP                       
        638     JUMP_FORWARD                  9 (to 658)
        640     WITH_EXCEPT_START             
        642     POP_JUMP_IF_TRUE              324 (to 648)
        646     RERAISE                       1
        648     POP_TOP                       
        650     POP_TOP                       
        652     POP_TOP                       
        654     POP_EXCEPT                    
        656     POP_TOP                       
        658     LOAD_NAME                     69: cred
        660     LOAD_CONST                    46: 'user'
        662     BINARY_SUBSCR                 
        664     STORE_NAME                    70: susr
        666     LOAD_NAME                     69: cred
        668     LOAD_CONST                    47: 'pwd'
        670     BINARY_SUBSCR                 
        672     STORE_NAME                    71: spassword
        674     LOAD_NAME                     60: TradeLog
        676     CALL_FUNCTION                 0
        678     STORE_NAME                    72: tl
        680     LOAD_CONST                    20: True
        682     STORE_GLOBAL                  73: place_orders
        684     LOAD_CONST                    0: 0
        686     STORE_GLOBAL                  74: order_count
        688     LOAD_NAME                     44: int
        690     LOAD_GLOBAL                   37: NULL + NorenApi
        692     LOAD_METHOD                   39: get
        694     LOAD_CONST                    48: 'status'
        696     LOAD_CONST                    49: 'algo_running_status'
        698     CALL_METHOD                   2
        700     CALL_FUNCTION                 1
        702     STORE_GLOBAL                  75: Algo_Running_Status
        704     LOAD_NAME                     44: int
        706     LOAD_NAME                     21: datetime
        708     LOAD_ATTR                     21: datetime
        710     LOAD_METHOD                   51: now
        712     CALL_METHOD                   0
        714     LOAD_METHOD                   52: strftime
        716     LOAD_CONST                    50: '%H%M'
        718     CALL_METHOD                   1
        720     CALL_FUNCTION                 1
        722     STORE_GLOBAL                  76: cur_HHMM
        724     LOAD_GLOBAL                   75: NULL + cfg
        726     LOAD_CONST                    29: 1
        728     COMPARE_OP                    2 (==)
        730     POP_JUMP_IF_FALSE             376 (to 752)
        734     LOAD_CONST                    51: ' Algo running status is showing 1. Check if any additional algo is running'
        736     STORE_NAME                    65: strMsg
        738     LOAD_NAME                     59: iLog
        740     LOAD_NAME                     65: strMsg
        742     LOAD_CONST                    52: 2
        744     LOAD_CONST                    20: True
        746     LOAD_CONST                    43: ('sendTeleMsg',)
        748     CALL_FUNCTION_KW              3
        750     POP_TOP                       
        752     LOAD_NAME                     44: int
        754     LOAD_NAME                     21: datetime
        756     LOAD_ATTR                     21: datetime
        758     LOAD_METHOD                   51: now
        760     CALL_METHOD                   0
        762     LOAD_METHOD                   52: strftime
        764     LOAD_CONST                    50: '%H%M'
        766     CALL_METHOD                   1
        768     CALL_FUNCTION                 1
        770     STORE_GLOBAL                  76: cur_HHMM
        772     LOAD_GLOBAL                   75: NULL + cfg
        774     LOAD_CONST                    0: 0
        776     COMPARE_OP                    2 (==)
        778     POP_JUMP_IF_FALSE             409 (to 818)
        782     LOAD_CONST                    53: ' Setting algo running status to 1'
        784     STORE_NAME                    65: strMsg
        786     LOAD_NAME                     59: iLog
        788     LOAD_NAME                     65: strMsg
        790     LOAD_CONST                    29: 1
        792     LOAD_CONST                    20: True
        794     LOAD_CONST                    43: ('sendTeleMsg',)
        796     CALL_FUNCTION_KW              3
        798     POP_TOP                       
        800     LOAD_NAME                     61: set_config_value
        802     LOAD_CONST                    48: 'status'
        804     LOAD_CONST                    49: 'algo_running_status'
        806     LOAD_CONST                    54: '1'
        808     CALL_FUNCTION                 3
        810     POP_TOP                       
        812     LOAD_NAME                     62: savedata
        814     CALL_FUNCTION                 0
        816     POP_TOP                       
        818     LOAD_NAME                     44: int
        820     LOAD_GLOBAL                   37: NULL + NorenApi
        822     LOAD_METHOD                   39: get
        824     LOAD_CONST                    55: 'algo'
        826     LOAD_CONST                    56: 'algo_trading'
        828     CALL_METHOD                   2
        830     CALL_FUNCTION                 1
        832     STORE_GLOBAL                  77: Algo_Trading
        834     LOAD_NAME                     44: int
        836     LOAD_GLOBAL                   37: NULL + NorenApi
        838     LOAD_METHOD                   39: get
        840     LOAD_CONST                    55: 'algo'
        842     LOAD_CONST                    57: 'papertrade'
        844     CALL_METHOD                   2
        846     CALL_FUNCTION                 1
        848     STORE_GLOBAL                  78: papertrade
        850     LOAD_GLOBAL                   78: get
        852     LOAD_CONST                    29: 1
        854     COMPARE_OP                    2 (==)
        856     POP_JUMP_IF_FALSE             439 (to 878)
        860     LOAD_CONST                    58: ' Paper Trade Enabled. Orders will not be placed'
        862     STORE_NAME                    65: strMsg
        864     LOAD_NAME                     59: iLog
        866     LOAD_NAME                     65: strMsg
        868     LOAD_CONST                    59: 6
        870     LOAD_CONST                    20: True
        872     LOAD_CONST                    43: ('sendTeleMsg',)
        874     CALL_FUNCTION_KW              3
        876     POP_TOP                       
        878     LOAD_GLOBAL                   78: get
        880     LOAD_CONST                    0: 0
        882     COMPARE_OP                    2 (==)
        884     POP_JUMP_IF_FALSE             453 (to 906)
        888     LOAD_CONST                    60: ' Live Trade Enabled. Orders will be placed. Monitor your trades closely'
        890     STORE_NAME                    65: strMsg
        892     LOAD_NAME                     59: iLog
        894     LOAD_NAME                     65: strMsg
        896     LOAD_CONST                    52: 2
        898     LOAD_CONST                    20: True
        900     LOAD_CONST                    43: ('sendTeleMsg',)
        902     CALL_FUNCTION_KW              3
        904     POP_TOP                       
        906     LOAD_NAME                     44: int
        908     LOAD_GLOBAL                   37: NULL + NorenApi
        910     LOAD_METHOD                   39: get
        912     LOAD_CONST                    55: 'algo'
        914     LOAD_CONST                    61: 'no_of_lots'
        916     CALL_METHOD                   2
        918     CALL_FUNCTION                 1
        920     STORE_GLOBAL                  79: no_of_lots
        922     LOAD_NAME                     44: int
        924     LOAD_GLOBAL                   37: NULL + NorenApi
        926     LOAD_METHOD                   39: get
        928     LOAD_CONST                    55: 'algo'
        930     LOAD_CONST                    62: 'exittradenow'
        932     CALL_METHOD                   2
        934     CALL_FUNCTION                 1
        936     STORE_GLOBAL                  80: ExitTradenow
        938     LOAD_NAME                     44: int
        940     LOAD_GLOBAL                   37: NULL + NorenApi
        942     LOAD_METHOD                   39: get
        944     LOAD_CONST                    55: 'algo'
        946     LOAD_CONST                    63: 'trade_nifty'
        948     CALL_METHOD                   2
        950     CALL_FUNCTION                 1
        952     STORE_GLOBAL                  81: Trade_Nifty
        954     LOAD_NAME                     44: int
        956     LOAD_GLOBAL                   37: NULL + NorenApi
        958     LOAD_METHOD                   39: get
        960     LOAD_CONST                    55: 'algo'
        962     LOAD_CONST                    64: 'trade_banknifty'
        964     CALL_METHOD                   2
        966     CALL_FUNCTION                 1
        968     STORE_GLOBAL                  82: Trade_BankNifty
        970     LOAD_NAME                     44: int
        972     LOAD_GLOBAL                   37: NULL + NorenApi
        974     LOAD_METHOD                   39: get
        976     LOAD_CONST                    55: 'algo'
        978     LOAD_CONST                    65: 'trade_finnifty'
        980     CALL_METHOD                   2
        982     CALL_FUNCTION                 1
        984     STORE_GLOBAL                  83: Trade_FinNifty
        986     LOAD_NAME                     44: int
        988     LOAD_GLOBAL                   37: NULL + NorenApi
        990     LOAD_METHOD                   39: get
        992     LOAD_CONST                    55: 'algo'
        994     LOAD_CONST                    66: 'king_candle_min_sl'
        996     CALL_METHOD                   2
        998     CALL_FUNCTION                 1
        1000    STORE_GLOBAL                  84: King_Candle_Min_SL
        1002    LOAD_NAME                     44: int
        1004    LOAD_GLOBAL                   37: NULL + NorenApi
        1006    LOAD_METHOD                   39: get
        1008    LOAD_CONST                    55: 'algo'
        1010    LOAD_CONST                    67: 'king_candle_max_sl'
        1012    CALL_METHOD                   2
        1014    CALL_FUNCTION                 1
        1016    STORE_GLOBAL                  85: King_Candle_Max_SL
        1018    LOAD_NAME                     44: int
        1020    LOAD_GLOBAL                   37: NULL + NorenApi
        1022    LOAD_METHOD                   39: get
        1024    LOAD_CONST                    55: 'algo'
        1026    LOAD_CONST                    68: 'time_offset_sec'
        1028    CALL_METHOD                   2
        1030    CALL_FUNCTION                 1
        1032    STORE_GLOBAL                  86: time_offset_sec
        1034    LOAD_NAME                     44: int
        1036    LOAD_GLOBAL                   37: NULL + NorenApi
        1038    LOAD_METHOD                   39: get
        1040    LOAD_CONST                    55: 'algo'
        1042    LOAD_CONST                    69: 'straddleentrytime'
        1044    CALL_METHOD                   2
        1046    CALL_FUNCTION                 1
        1048    STORE_GLOBAL                  87: StraddleEntryTime
        1050    LOAD_NAME                     44: int
        1052    LOAD_GLOBAL                   37: NULL + NorenApi
        1054    LOAD_METHOD                   39: get
        1056    LOAD_CONST                    55: 'algo'
        1058    LOAD_CONST                    70: 'kingstarttime'
        1060    CALL_METHOD                   2
        1062    CALL_FUNCTION                 1
        1064    STORE_GLOBAL                  88: KingStartTime
        1066    LOAD_NAME                     44: int
        1068    LOAD_GLOBAL                   37: NULL + NorenApi
        1070    LOAD_METHOD                   39: get
        1072    LOAD_CONST                    55: 'algo'
        1074    LOAD_CONST                    71: 'exitTime'
        1076    CALL_METHOD                   2
        1078    CALL_FUNCTION                 1
        1080    STORE_GLOBAL                  89: ExitTime
        1082    LOAD_NAME                     44: int
        1084    LOAD_GLOBAL                   37: NULL + NorenApi
        1086    LOAD_METHOD                   39: get
        1088    LOAD_CONST                    55: 'algo'
        1090    LOAD_CONST                    72: 'maxpositionchangetime'
        1092    CALL_METHOD                   2
        1094    CALL_FUNCTION                 1
        1096    STORE_GLOBAL                  90: MaxPositionChangeTime
        1098    LOAD_GLOBAL                   87: NULL + strBotTokenWObot
        1100    LOAD_CONST                    73: 100
        1102    BINARY_MULTIPLY               
        1104    LOAD_GLOBAL                   86: strBotTokenWObot
        1106    BINARY_ADD                    
        1108    STORE_GLOBAL                  87: StraddleEntryTime
        1110    LOAD_GLOBAL                   89: NULL + int
        1112    LOAD_CONST                    73: 100
        1114    BINARY_MULTIPLY               
        1116    LOAD_GLOBAL                   86: strBotTokenWObot
        1118    BINARY_ADD                    
        1120    STORE_GLOBAL                  89: ExitTime
        1122    LOAD_NAME                     91: float
        1124    LOAD_GLOBAL                   37: NULL + NorenApi
        1126    LOAD_METHOD                   39: get
        1128    LOAD_CONST                    55: 'algo'
        1130    LOAD_CONST                    74: 'expiry_day_directional'
        1132    CALL_METHOD                   2
        1134    CALL_FUNCTION                 1
        1136    STORE_GLOBAL                  92: expiry_day_directional
        1138    LOAD_NAME                     91: float
        1140    LOAD_GLOBAL                   37: NULL + NorenApi
        1142    LOAD_METHOD                   39: get
        1144    LOAD_CONST                    55: 'algo'
        1146    LOAD_CONST                    75: 'normal_day_directional'
        1148    CALL_METHOD                   2
        1150    CALL_FUNCTION                 1
        1152    STORE_GLOBAL                  93: normal_day_directional
        1154    LOAD_NAME                     91: float
        1156    LOAD_GLOBAL                   37: NULL + NorenApi
        1158    LOAD_METHOD                   39: get
        1160    LOAD_CONST                    55: 'algo'
        1162    LOAD_CONST                    76: 'expiry_perlot_mtm_sl'
        1164    CALL_METHOD                   2
        1166    CALL_FUNCTION                 1
        1168    STORE_GLOBAL                  94: expiry_Perlot_MTM_SL
        1170    LOAD_NAME                     44: int
        1172    LOAD_GLOBAL                   37: NULL + NorenApi
        1174    LOAD_METHOD                   39: get
        1176    LOAD_CONST                    55: 'algo'
        1178    LOAD_CONST                    77: 'expiry_perlot_mtm_target'
        1180    CALL_METHOD                   2
        1182    CALL_FUNCTION                 1
        1184    STORE_GLOBAL                  95: expiry_Perlot_MTM_Target
        1186    LOAD_NAME                     44: int
        1188    LOAD_GLOBAL                   37: NULL + NorenApi
        1190    LOAD_METHOD                   39: get
        1192    LOAD_CONST                    55: 'algo'
        1194    LOAD_CONST                    78: 'normal_perlot_mtm_sl'
        1196    CALL_METHOD                   2
        1198    CALL_FUNCTION                 1
        1200    STORE_GLOBAL                  96: normal_Perlot_MTM_SL
        1202    LOAD_NAME                     44: int
        1204    LOAD_GLOBAL                   37: NULL + NorenApi
        1206    LOAD_METHOD                   39: get
        1208    LOAD_CONST                    55: 'algo'
        1210    LOAD_CONST                    79: 'normal_perlot_mtm_target'
        1212    CALL_METHOD                   2
        1214    CALL_FUNCTION                 1
        1216    STORE_GLOBAL                  97: normal_Perlot_MTM_Target
        1218    LOAD_NAME                     91: float
        1220    LOAD_GLOBAL                   37: NULL + NorenApi
        1222    LOAD_METHOD                   39: get
        1224    LOAD_CONST                    55: 'algo'
        1226    LOAD_CONST                    80: 'expiry_stikeadj_slper'
        1228    CALL_METHOD                   2
        1230    CALL_FUNCTION                 1
        1232    STORE_GLOBAL                  98: expiry_StikeAdj_SLPer
        1234    LOAD_NAME                     91: float
        1236    LOAD_GLOBAL                   37: NULL + NorenApi
        1238    LOAD_METHOD                   39: get
        1240    LOAD_CONST                    55: 'algo'
        1242    LOAD_CONST                    81: 'expiry_stikeadj_tgtper'
        1244    CALL_METHOD                   2
        1246    CALL_FUNCTION                 1
        1248    STORE_GLOBAL                  99: expiry_StikeAdj_TgtPer
        1250    LOAD_NAME                     91: float
        1252    LOAD_GLOBAL                   37: NULL + NorenApi
        1254    LOAD_METHOD                   39: get
        1256    LOAD_CONST                    55: 'algo'
        1258    LOAD_CONST                    82: 'normal_stikeadj_slper'
        1260    CALL_METHOD                   2
        1262    CALL_FUNCTION                 1
        1264    STORE_GLOBAL                  100: normal_StikeAdj_SLPer
        1266    LOAD_NAME                     91: float
        1268    LOAD_GLOBAL                   37: NULL + NorenApi
        1270    LOAD_METHOD                   39: get
        1272    LOAD_CONST                    55: 'algo'
        1274    LOAD_CONST                    83: 'normal_stikeadj_tgtper'
        1276    CALL_METHOD                   2
        1278    CALL_FUNCTION                 1
        1280    STORE_GLOBAL                  101: normal_StikeAdj_TgtPer
        1282    LOAD_NAME                     91: float
        1284    LOAD_GLOBAL                   37: NULL + NorenApi
        1286    LOAD_METHOD                   39: get
        1288    LOAD_CONST                    55: 'algo'
        1290    LOAD_CONST                    84: 'expiry_tgtpremium'
        1292    CALL_METHOD                   2
        1294    CALL_FUNCTION                 1
        1296    STORE_GLOBAL                  102: expiry_TgtPremium
        1298    LOAD_NAME                     91: float
        1300    LOAD_GLOBAL                   37: NULL + NorenApi
        1302    LOAD_METHOD                   39: get
        1304    LOAD_CONST                    55: 'algo'
        1306    LOAD_CONST                    85: 'normal_tgtpremium'
        1308    CALL_METHOD                   2
        1310    CALL_FUNCTION                 1
        1312    STORE_GLOBAL                  103: normal_TgtPremium
        1314    LOAD_NAME                     91: float
        1316    LOAD_GLOBAL                   37: NULL + NorenApi
        1318    LOAD_METHOD                   39: get
        1320    LOAD_CONST                    55: 'algo'
        1322    LOAD_CONST                    86: 'expiry_stikeadj_sl_min_points'
        1324    CALL_METHOD                   2
        1326    CALL_FUNCTION                 1
        1328    STORE_GLOBAL                  104: expiry_StikeAdj_SL_Min_Points
        1330    LOAD_NAME                     91: float
        1332    LOAD_GLOBAL                   37: NULL + NorenApi
        1334    LOAD_METHOD                   39: get
        1336    LOAD_CONST                    55: 'algo'
        1338    LOAD_CONST                    87: 'normal_stikeadj_sl_min_points'
        1340    CALL_METHOD                   2
        1342    CALL_FUNCTION                 1
        1344    STORE_GLOBAL                  105: normal_StikeAdj_SL_Min_Points
        1346    LOAD_NAME                     91: float
        1348    LOAD_GLOBAL                   37: NULL + NorenApi
        1350    LOAD_METHOD                   39: get
        1352    LOAD_CONST                    55: 'algo'
        1354    LOAD_CONST                    88: 'expiry_stikeadj_tgt_min_points'
        1356    CALL_METHOD                   2
        1358    CALL_FUNCTION                 1
        1360    STORE_GLOBAL                  106: expiry_StikeAdj_TGT_Min_Points
        1362    LOAD_NAME                     91: float
        1364    LOAD_GLOBAL                   37: NULL + NorenApi
        1366    LOAD_METHOD                   39: get
        1368    LOAD_CONST                    55: 'algo'
        1370    LOAD_CONST                    89: 'normal_stikeadj_tgt_min_points'
        1372    CALL_METHOD                   2
        1374    CALL_FUNCTION                 1
        1376    STORE_GLOBAL                  107: normal_StikeAdj_TGT_Min_Points
        1378    LOAD_NAME                     91: float
        1380    LOAD_GLOBAL                   37: NULL + NorenApi
        1382    LOAD_METHOD                   39: get
        1384    LOAD_CONST                    55: 'algo'
        1386    LOAD_CONST                    90: 'atm_strike_ce_offset'
        1388    CALL_METHOD                   2
        1390    CALL_FUNCTION                 1
        1392    STORE_GLOBAL                  108: ATM_strike_ce_offset
        1394    LOAD_NAME                     91: float
        1396    LOAD_GLOBAL                   37: NULL + NorenApi
        1398    LOAD_METHOD                   39: get
        1400    LOAD_CONST                    55: 'algo'
        1402    LOAD_CONST                    91: 'atm_strike_pe_offset'
        1404    CALL_METHOD                   2
        1406    CALL_FUNCTION                 1
        1408    STORE_GLOBAL                  109: ATM_strike_pe_offset
        1410    LOAD_NAME                     44: int
        1412    LOAD_GLOBAL                   37: NULL + NorenApi
        1414    LOAD_METHOD                   39: get
        1416    LOAD_CONST                    55: 'algo'
        1418    LOAD_CONST                    92: 'strike_offset'
        1420    CALL_METHOD                   2
        1422    CALL_FUNCTION                 1
        1424    STORE_GLOBAL                  110: strike_offset
        1426    LOAD_NAME                     91: float
        1428    LOAD_GLOBAL                   37: NULL + NorenApi
        1430    LOAD_METHOD                   39: get
        1432    LOAD_CONST                    55: 'algo'
        1434    LOAD_CONST                    93: 'entry_price'
        1436    CALL_METHOD                   2
        1438    CALL_FUNCTION                 1
        1440    STORE_GLOBAL                  111: entry_price
        1442    LOAD_NAME                     91: float
        1444    LOAD_GLOBAL                   37: NULL + NorenApi
        1446    LOAD_METHOD                   39: get
        1448    LOAD_CONST                    55: 'algo'
        1450    LOAD_CONST                    94: 'entry_price_buffer'
        1452    CALL_METHOD                   2
        1454    CALL_FUNCTION                 1
        1456    STORE_GLOBAL                  112: entry_price_buffer
        1458    LOAD_NAME                     91: float
        1460    LOAD_GLOBAL                   37: NULL + NorenApi
        1462    LOAD_METHOD                   39: get
        1464    LOAD_CONST                    55: 'algo'
        1466    LOAD_CONST                    95: 'enable_mtm_trailing'
        1468    CALL_METHOD                   2
        1470    CALL_FUNCTION                 1
        1472    STORE_GLOBAL                  113: Enable_MTM_Trailing
        1474    LOAD_NAME                     91: float
        1476    LOAD_GLOBAL                   37: NULL + NorenApi
        1478    LOAD_METHOD                   39: get
        1480    LOAD_CONST                    55: 'algo'
        1482    LOAD_CONST                    96: 'normal_perlot_mtm_lock_profit_threshold'
        1484    CALL_METHOD                   2
        1486    CALL_FUNCTION                 1
        1488    STORE_GLOBAL                  114: normal_Perlot_MTM_lock_profit_threshold
        1490    LOAD_NAME                     91: float
        1492    LOAD_GLOBAL                   37: NULL + NorenApi
        1494    LOAD_METHOD                   39: get
        1496    LOAD_CONST                    55: 'algo'
        1498    LOAD_CONST                    97: 'normal_perlot_mtm_lock_profit'
        1500    CALL_METHOD                   2
        1502    CALL_FUNCTION                 1
        1504    STORE_GLOBAL                  115: normal_Perlot_MTM_lock_profit
        1506    LOAD_NAME                     91: float
        1508    LOAD_GLOBAL                   37: NULL + NorenApi
        1510    LOAD_METHOD                   39: get
        1512    LOAD_CONST                    55: 'algo'
        1514    LOAD_CONST                    98: 'normal_perlot_mtm_trailing'
        1516    CALL_METHOD                   2
        1518    CALL_FUNCTION                 1
        1520    STORE_GLOBAL                  116: normal_Perlot_MTM_Trailing
        1522    LOAD_NAME                     91: float
        1524    LOAD_GLOBAL                   37: NULL + NorenApi
        1526    LOAD_METHOD                   39: get
        1528    LOAD_CONST                    55: 'algo'
        1530    LOAD_CONST                    99: 'expiry_perlot_mtm_lock_profit_threshold'
        1532    CALL_METHOD                   2
        1534    CALL_FUNCTION                 1
        1536    STORE_GLOBAL                  117: expiry_Perlot_MTM_lock_profit_threshold
        1538    LOAD_NAME                     91: float
        1540    LOAD_GLOBAL                   37: NULL + NorenApi
        1542    LOAD_METHOD                   39: get
        1544    LOAD_CONST                    55: 'algo'
        1546    LOAD_CONST                    100: 'expiry_perlot_mtm_lock_profit'
        1548    CALL_METHOD                   2
        1550    CALL_FUNCTION                 1
        1552    STORE_GLOBAL                  118: expiry_Perlot_MTM_lock_profit
        1554    LOAD_NAME                     91: float
        1556    LOAD_GLOBAL                   37: NULL + NorenApi
        1558    LOAD_METHOD                   39: get
        1560    LOAD_CONST                    55: 'algo'
        1562    LOAD_CONST                    101: 'expiry_perlot_mtm_trailing'
        1564    CALL_METHOD                   2
        1566    CALL_FUNCTION                 1
        1568    STORE_GLOBAL                  119: expiry_Perlot_MTM_Trailing
        1570    LOAD_NAME                     91: float
        1572    LOAD_GLOBAL                   37: NULL + NorenApi
        1574    LOAD_METHOD                   39: get
        1576    LOAD_CONST                    55: 'algo'
        1578    LOAD_CONST                    102: 'rsi_low'
        1580    CALL_METHOD                   2
        1582    CALL_FUNCTION                 1
        1584    STORE_GLOBAL                  120: RSI_Low
        1586    LOAD_NAME                     91: float
        1588    LOAD_GLOBAL                   37: NULL + NorenApi
        1590    LOAD_METHOD                   39: get
        1592    LOAD_CONST                    55: 'algo'
        1594    LOAD_CONST                    103: 'rsi_high'
        1596    CALL_METHOD                   2
        1598    CALL_FUNCTION                 1
        1600    STORE_GLOBAL                  121: RSI_High
        1602    LOAD_NAME                     91: float
        1604    LOAD_GLOBAL                   37: NULL + NorenApi
        1606    LOAD_METHOD                   39: get
        1608    LOAD_CONST                    55: 'algo'
        1610    LOAD_CONST                    104: 'rsi_period'
        1612    CALL_METHOD                   2
        1614    CALL_FUNCTION                 1
        1616    STORE_GLOBAL                  122: RSI_Period
        1618    LOAD_NAME                     91: float
        1620    LOAD_GLOBAL                   37: NULL + NorenApi
        1622    LOAD_METHOD                   39: get
        1624    LOAD_CONST                    55: 'algo'
        1626    LOAD_CONST                    105: 'adx_period'
        1628    CALL_METHOD                   2
        1630    CALL_FUNCTION                 1
        1632    STORE_GLOBAL                  123: ADX_Period
        1634    LOAD_NAME                     91: float
        1636    LOAD_GLOBAL                   37: NULL + NorenApi
        1638    LOAD_METHOD                   39: get
        1640    LOAD_CONST                    55: 'algo'
        1642    LOAD_CONST                    106: 'st_period'
        1644    CALL_METHOD                   2
        1646    CALL_FUNCTION                 1
        1648    STORE_GLOBAL                  124: ST_Period
        1650    LOAD_NAME                     91: float
        1652    LOAD_GLOBAL                   37: NULL + NorenApi
        1654    LOAD_METHOD                   39: get
        1656    LOAD_CONST                    55: 'algo'
        1658    LOAD_CONST                    107: 'st_mult'
        1660    CALL_METHOD                   2
        1662    CALL_FUNCTION                 1
        1664    STORE_GLOBAL                  125: ST_Mult
        1666    LOAD_NAME                     91: float
        1668    LOAD_GLOBAL                   37: NULL + NorenApi
        1670    LOAD_METHOD                   39: get
        1672    LOAD_CONST                    55: 'algo'
        1674    LOAD_CONST                    108: 'st_close'
        1676    CALL_METHOD                   2
        1678    CALL_FUNCTION                 1
        1680    STORE_GLOBAL                  126: ST_Close
        1682    LOAD_NAME                     91: float
        1684    LOAD_GLOBAL                   37: NULL + NorenApi
        1686    LOAD_METHOD                   39: get
        1688    LOAD_CONST                    55: 'algo'
        1690    LOAD_CONST                    109: 'candle_close_breakout'
        1692    CALL_METHOD                   2
        1694    CALL_FUNCTION                 1
        1696    STORE_GLOBAL                  127: candle_close_breakout
        1698    LOAD_NAME                     91: float
        1700    LOAD_GLOBAL                   37: NULL + NorenApi
        1702    LOAD_METHOD                   39: get
        1704    LOAD_CONST                    55: 'algo'
        1706    LOAD_CONST                    110: 'normal_synthetic_fut'
        1708    CALL_METHOD                   2
        1710    CALL_FUNCTION                 1
        1712    STORE_GLOBAL                  128: normal_Synthetic_Fut
        1714    LOAD_NAME                     91: float
        1716    LOAD_GLOBAL                   37: NULL + NorenApi
        1718    LOAD_METHOD                   39: get
        1720    LOAD_CONST                    55: 'algo'
        1722    LOAD_CONST                    111: 'normal_single_leg_adj'
        1724    CALL_METHOD                   2
        1726    CALL_FUNCTION                 1
        1728    STORE_GLOBAL                  129: normal_Single_Leg_Adj
        1730    LOAD_NAME                     91: float
        1732    LOAD_GLOBAL                   37: NULL + NorenApi
        1734    LOAD_METHOD                   39: get
        1736    LOAD_CONST                    55: 'algo'
        1738    LOAD_CONST                    112: 'normal_single_leg_adj_delta_pct'
        1740    CALL_METHOD                   2
        1742    CALL_FUNCTION                 1
        1744    STORE_GLOBAL                  130: normal_Single_Leg_Adj_Delta_PCT
        1746    LOAD_NAME                     91: float
        1748    LOAD_GLOBAL                   37: NULL + NorenApi
        1750    LOAD_METHOD                   39: get
        1752    LOAD_CONST                    55: 'algo'
        1754    LOAD_CONST                    113: 'expiry_synthetic_fut'
        1756    CALL_METHOD                   2
        1758    CALL_FUNCTION                 1
        1760    STORE_GLOBAL                  131: expiry_Synthetic_Fut
        1762    LOAD_NAME                     91: float
        1764    LOAD_GLOBAL                   37: NULL + NorenApi
        1766    LOAD_METHOD                   39: get
        1768    LOAD_CONST                    55: 'algo'
        1770    LOAD_CONST                    114: 'expiry_single_leg_adj'
        1772    CALL_METHOD                   2
        1774    CALL_FUNCTION                 1
        1776    STORE_GLOBAL                  132: expiry_Single_Leg_Adj
        1778    LOAD_NAME                     91: float
        1780    LOAD_GLOBAL                   37: NULL + NorenApi
        1782    LOAD_METHOD                   39: get
        1784    LOAD_CONST                    55: 'algo'
        1786    LOAD_CONST                    115: 'expiry_single_leg_adj_delta_pct'
        1788    CALL_METHOD                   2
        1790    CALL_FUNCTION                 1
        1792    STORE_GLOBAL                  133: expiry_Single_Leg_Adj_Delta_PCT
        1794    LOAD_NAME                     91: float
        1796    LOAD_GLOBAL                   37: NULL + NorenApi
        1798    LOAD_METHOD                   39: get
        1800    LOAD_CONST                    55: 'algo'
        1802    LOAD_CONST                    116: 'partial_profit_booking_enable'
        1804    CALL_METHOD                   2
        1806    CALL_FUNCTION                 1
        1808    STORE_GLOBAL                  134: partial_profit_booking_enable
        1810    LOAD_NAME                     91: float
        1812    LOAD_GLOBAL                   37: NULL + NorenApi
        1814    LOAD_METHOD                   39: get
        1816    LOAD_CONST                    55: 'algo'
        1818    LOAD_CONST                    117: 'partial_profit_booking_no_of_lots'
        1820    CALL_METHOD                   2
        1822    CALL_FUNCTION                 1
        1824    STORE_GLOBAL                  135: partial_profit_booking_no_of_lots
        1826    LOAD_NAME                     91: float
        1828    LOAD_GLOBAL                   37: NULL + NorenApi
        1830    LOAD_METHOD                   39: get
        1832    LOAD_CONST                    55: 'algo'
        1834    LOAD_CONST                    118: 'partial_profit_booking_perlot_target'
        1836    CALL_METHOD                   2
        1838    CALL_FUNCTION                 1
        1840    STORE_GLOBAL                  136: partial_profit_booking_perlot_target
        1842    LOAD_GLOBAL                   134: load
        1844    LOAD_CONST                    29: 1
        1846    COMPARE_OP                    2 (==)
        1848    POP_JUMP_IF_FALSE             934 (to 1868)
        1852    LOAD_GLOBAL                   135: NULL + load
        1854    LOAD_GLOBAL                   79: NULL + get
        1856    COMPARE_OP                    0 (<)
        1858    POP_JUMP_IF_FALSE             934 (to 1868)
        1862    LOAD_CONST                    29: 1
        1864    STORE_GLOBAL                  134: partial_profit_booking_enable
        1866    JUMP_FORWARD                  35 (to 1938)
        1868    LOAD_GLOBAL                   134: load
        1870    LOAD_CONST                    29: 1
        1872    COMPARE_OP                    2 (==)
        1874    POP_JUMP_IF_FALSE             969 (to 1938)
        1878    LOAD_GLOBAL                   135: NULL + load
        1880    LOAD_GLOBAL                   79: NULL + get
        1882    COMPARE_OP                    5 (>=)
        1884    POP_JUMP_IF_FALSE             969 (to 1938)
        1888    LOAD_CONST                    0: 0
        1890    STORE_GLOBAL                  134: partial_profit_booking_enable
        1892    LOAD_NAME                     59: iLog
        1894    LOAD_CONST                    119: 'partial_profit_booking_no_of_lots '
        1896    LOAD_GLOBAL                   135: NULL + load
        1898    FORMAT_VALUE                  0
        1900    LOAD_CONST                    120: " can't be equal to or than more total no of lots"
        1902    LOAD_GLOBAL                   79: NULL + get
        1904    FORMAT_VALUE                  0
        1906    LOAD_CONST                    121: ', setting partial_profit_booking_enable to 0'
        1908    BUILD_STRING                  5
        1910    LOAD_CONST                    52: 2
        1912    LOAD_CONST                    20: True
        1914    LOAD_CONST                    43: ('sendTeleMsg',)
        1916    CALL_FUNCTION_KW              3
        1918    POP_TOP                       
        1920    LOAD_NAME                     61: set_config_value
        1922    LOAD_CONST                    55: 'algo'
        1924    LOAD_CONST                    116: 'partial_profit_booking_enable'
        1926    LOAD_CONST                    122: '0'
        1928    CALL_FUNCTION                 3
        1930    POP_TOP                       
        1932    LOAD_NAME                     62: savedata
        1934    CALL_FUNCTION                 0
        1936    POP_TOP                       
        1938    LOAD_NAME                     44: int
        1940    LOAD_GLOBAL                   37: NULL + NorenApi
        1942    LOAD_METHOD                   39: get
        1944    LOAD_CONST                    55: 'algo'
        1946    LOAD_CONST                    123: 'wait_for_premium'
        1948    CALL_METHOD                   2
        1950    CALL_FUNCTION                 1
        1952    STORE_GLOBAL                  137: wait_for_premium
        1954    LOAD_NAME                     44: int
        1956    LOAD_GLOBAL                   37: NULL + NorenApi
        1958    LOAD_METHOD                   39: get
        1960    LOAD_CONST                    55: 'algo'
        1962    LOAD_CONST                    124: 'premium_difference'
        1964    CALL_METHOD                   2
        1966    CALL_FUNCTION                 1
        1968    STORE_GLOBAL                  138: premium_difference
        1970    LOAD_NAME                     44: int
        1972    LOAD_GLOBAL                   37: NULL + NorenApi
        1974    LOAD_METHOD                   39: get
        1976    LOAD_CONST                    55: 'algo'
        1978    LOAD_CONST                    125: 'wait_for_movement'
        1980    CALL_METHOD                   2
        1982    CALL_FUNCTION                 1
        1984    STORE_GLOBAL                  139: wait_for_movement
        1986    LOAD_NAME                     44: int
        1988    LOAD_GLOBAL                   37: NULL + NorenApi
        1990    LOAD_METHOD                   39: get
        1992    LOAD_CONST                    55: 'algo'
        1994    LOAD_CONST                    126: 'movement_pos_points'
        1996    CALL_METHOD                   2
        1998    CALL_FUNCTION                 1
        2000    STORE_GLOBAL                  140: movement_pos_points
        2002    LOAD_NAME                     44: int
        2004    LOAD_GLOBAL                   37: NULL + NorenApi
        2006    LOAD_METHOD                   39: get
        2008    LOAD_CONST                    55: 'algo'
        2010    LOAD_CONST                    127: 'movement_neg_points'
        2012    CALL_METHOD                   2
        2014    CALL_FUNCTION                 1
        2016    STORE_GLOBAL                  141: movement_neg_points
        2018    LOAD_NAME                     44: int
        2020    LOAD_GLOBAL                   37: NULL + NorenApi
        2022    LOAD_METHOD                   39: get
        2024    LOAD_CONST                    55: 'algo'
        2026    LOAD_CONST                    128: 'max_entry_time'
        2028    CALL_METHOD                   2
        2030    CALL_FUNCTION                 1
        2032    STORE_GLOBAL                  142: max_entry_time
        2034    LOAD_NAME                     44: int
        2036    LOAD_GLOBAL                   37: NULL + NorenApi
        2038    LOAD_METHOD                   39: get
        2040    LOAD_CONST                    55: 'algo'
        2042    LOAD_CONST                    129: 'max_entry_time_exit'
        2044    CALL_METHOD                   2
        2046    CALL_FUNCTION                 1
        2048    STORE_GLOBAL                  143: max_entry_time_exit
        2050    LOAD_NAME                     44: int
        2052    LOAD_GLOBAL                   37: NULL + NorenApi
        2054    LOAD_METHOD                   39: get
        2056    LOAD_CONST                    55: 'algo'
        2058    LOAD_CONST                    130: 'hedge_buy'
        2060    CALL_METHOD                   2
        2062    CALL_FUNCTION                 1
        2064    STORE_GLOBAL                  144: hedge_buy
        2066    LOAD_NAME                     91: float
        2068    LOAD_GLOBAL                   37: NULL + NorenApi
        2070    LOAD_METHOD                   39: get
        2072    LOAD_CONST                    55: 'algo'
        2074    LOAD_CONST                    131: 'hedge_buy_offset'
        2076    CALL_METHOD                   2
        2078    CALL_FUNCTION                 1
        2080    STORE_GLOBAL                  145: hedge_buy_offset
        2082    LOAD_NAME                     44: int
        2084    LOAD_GLOBAL                   37: NULL + NorenApi
        2086    LOAD_METHOD                   39: get
        2088    LOAD_CONST                    55: 'algo'
        2090    LOAD_CONST                    132: 'hedge_buy_strike_offset'
        2092    CALL_METHOD                   2
        2094    CALL_FUNCTION                 1
        2096    STORE_GLOBAL                  146: hedge_buy_strike
        2098    LOAD_NAME                     91: float
        2100    LOAD_GLOBAL                   37: NULL + NorenApi
        2102    LOAD_METHOD                   39: get
        2104    LOAD_CONST                    55: 'algo'
        2106    LOAD_CONST                    133: 'hedge_buy_price'
        2108    CALL_METHOD                   2
        2110    CALL_FUNCTION                 1
        2112    STORE_GLOBAL                  147: hedge_buy_price
        2114    LOAD_NAME                     91: float
        2116    LOAD_GLOBAL                   37: NULL + NorenApi
        2118    LOAD_METHOD                   39: get
        2120    LOAD_CONST                    55: 'algo'
        2122    LOAD_CONST                    134: 'hedge_buy_price_buffer'
        2124    CALL_METHOD                   2
        2126    CALL_FUNCTION                 1
        2128    STORE_GLOBAL                  148: hedge_buy_price_buffer
        2130    LOAD_NAME                     44: int
        2132    LOAD_GLOBAL                   37: NULL + NorenApi
        2134    LOAD_METHOD                   39: get
        2136    LOAD_CONST                    55: 'algo'
        2138    LOAD_CONST                    135: 'king_use_adx'
        2140    CALL_METHOD                   2
        2142    CALL_FUNCTION                 1
        2144    STORE_GLOBAL                  149: king_use_adx
        2146    LOAD_NAME                     44: int
        2148    LOAD_GLOBAL                   37: NULL + NorenApi
        2150    LOAD_METHOD                   39: get
        2152    LOAD_CONST                    55: 'algo'
        2154    LOAD_CONST                    136: 'candle_close_leg_change'
        2156    CALL_METHOD                   2
        2158    CALL_FUNCTION                 1
        2160    STORE_GLOBAL                  150: candle_close_leg_change
        2162    LOAD_NAME                     44: int
        2164    LOAD_GLOBAL                   37: NULL + NorenApi
        2166    LOAD_METHOD                   39: get
        2168    LOAD_CONST                    55: 'algo'
        2170    LOAD_CONST                    137: 'mtm_based_leg_change'
        2172    CALL_METHOD                   2
        2174    CALL_FUNCTION                 1
        2176    STORE_GLOBAL                  151: mtm_based_leg_change
        2178    LOAD_NAME                     91: float
        2180    LOAD_GLOBAL                   37: NULL + NorenApi
        2182    LOAD_METHOD                   39: get
        2184    LOAD_CONST                    55: 'algo'
        2186    LOAD_CONST                    138: 'mtm_perlot_limit_leg_change'
        2188    CALL_METHOD                   2
        2190    CALL_FUNCTION                 1
        2192    STORE_GLOBAL                  152: mtm_perlot_limit_leg_change
        2194    LOAD_NAME                     44: int
        2196    LOAD_GLOBAL                   37: NULL + NorenApi
        2198    LOAD_METHOD                   39: get
        2200    LOAD_CONST                    55: 'algo'
        2202    LOAD_CONST                    139: 'limit_order'
        2204    CALL_METHOD                   2
        2206    CALL_FUNCTION                 1
        2208    STORE_GLOBAL                  153: limit_order
        2210    LOAD_NAME                     44: int
        2212    LOAD_GLOBAL                   37: NULL + NorenApi
        2214    LOAD_METHOD                   39: get
        2216    LOAD_CONST                    55: 'algo'
        2218    LOAD_CONST                    140: 'pos_order'
        2220    CALL_METHOD                   2
        2222    CALL_FUNCTION                 1
        2224    STORE_GLOBAL                  154: pos_order
        2226    LOAD_NAME                     44: int
        2228    LOAD_GLOBAL                   37: NULL + NorenApi
        2230    LOAD_METHOD                   39: get
        2232    LOAD_CONST                    55: 'algo'
        2234    LOAD_CONST                    141: 'ord_wait_sec'
        2236    CALL_METHOD                   2
        2238    CALL_FUNCTION                 1
        2240    STORE_GLOBAL                  155: ord_wait_sec
        2242    LOAD_NAME                     44: int
        2244    LOAD_GLOBAL                   37: NULL + NorenApi
        2246    LOAD_METHOD                   39: get
        2248    LOAD_CONST                    55: 'algo'
        2250    LOAD_CONST                    142: 'ord_max_retry'
        2252    CALL_METHOD                   2
        2254    CALL_FUNCTION                 1
        2256    STORE_GLOBAL                  156: ord_max_retry
        2258    LOAD_NAME                     44: int
        2260    LOAD_GLOBAL                   37: NULL + NorenApi
        2262    LOAD_METHOD                   39: get
        2264    LOAD_CONST                    55: 'algo'
        2266    LOAD_CONST                    143: 'single_leg_reentry_buffer'
        2268    CALL_METHOD                   2
        2270    CALL_FUNCTION                 1
        2272    STORE_GLOBAL                  157: single_leg_reentry_buffer
        2274    LOAD_NAME                     44: int
        2276    LOAD_GLOBAL                   37: NULL + NorenApi
        2278    LOAD_METHOD                   39: get
        2280    LOAD_CONST                    14: 'general'
        2282    LOAD_CONST                    144: 'king_interval'
        2284    CALL_METHOD                   2
        2286    CALL_FUNCTION                 1
        2288    STORE_GLOBAL                  158: king_interval
        2290    LOAD_NAME                     44: int
        2292    LOAD_GLOBAL                   37: NULL + NorenApi
        2294    LOAD_METHOD                   39: get
        2296    LOAD_CONST                    14: 'general'
        2298    LOAD_CONST                    145: 'log_interval'
        2300    CALL_METHOD                   2
        2302    CALL_FUNCTION                 1
        2304    STORE_GLOBAL                  159: log_interval
        2306    LOAD_NAME                     44: int
        2308    LOAD_GLOBAL                   37: NULL + NorenApi
        2310    LOAD_METHOD                   39: get
        2312    LOAD_CONST                    14: 'general'
        2314    LOAD_CONST                    146: 'continuous_logging'
        2316    CALL_METHOD                   2
        2318    CALL_FUNCTION                 1
        2320    STORE_GLOBAL                  160: Continuous_Logging
        2322    LOAD_NAME                     44: int
        2324    LOAD_GLOBAL                   37: NULL + NorenApi
        2326    LOAD_METHOD                   39: get
        2328    LOAD_CONST                    14: 'general'
        2330    LOAD_CONST                    147: 'weekend_testing'
        2332    CALL_METHOD                   2
        2334    CALL_FUNCTION                 1
        2336    STORE_GLOBAL                  161: weekend_testing
        2338    LOAD_NAME                     44: int
        2340    LOAD_GLOBAL                   37: NULL + NorenApi
        2342    LOAD_METHOD                   39: get
        2344    LOAD_CONST                    14: 'general'
        2346    LOAD_CONST                    148: 'order_limit_per_day'
        2348    CALL_METHOD                   2
        2350    CALL_FUNCTION                 1
        2352    STORE_GLOBAL                  162: order_limit_per_day
        2354    LOAD_NAME                     44: int
        2356    LOAD_GLOBAL                   37: NULL + NorenApi
        2358    LOAD_METHOD                   39: get
        2360    LOAD_CONST                    14: 'general'
        2362    LOAD_CONST                    149: 'ltp_not_updating_exit'
        2364    CALL_METHOD                   2
        2366    CALL_FUNCTION                 1
        2368    STORE_GLOBAL                  163: ltp_not_updating_exit
        2370    LOAD_NAME                     44: int
        2372    LOAD_GLOBAL                   37: NULL + NorenApi
        2374    LOAD_METHOD                   39: get
        2376    LOAD_CONST                    14: 'general'
        2378    LOAD_CONST                    150: 'ltp_not_updating_limit_secs'
        2380    CALL_METHOD                   2
        2382    CALL_FUNCTION                 1
        2384    STORE_GLOBAL                  164: ltp_not_updating_limit_secs
        2386    BUILD_LIST                    0
        2388    STORE_GLOBAL                  165: lst_Index_ltp
        2390    LOAD_CONST                    151: '%Y-%m-%d'
        2392    STORE_NAME                    166: dateFormat
        2394    LOAD_CONST                    152: '%H:%M:%S'
        2396    STORE_NAME                    167: timeFormat
        2398    LOAD_CONST                    153: '%Y-%m-%d %H:%M:%S'
        2400    STORE_NAME                    168: dateTimeFormat
        2402    LOAD_CONST                    30: False
        2404    STORE_GLOBAL                  169: socket_opened
        2406    LOAD_CONST                    30: False
        2408    STORE_GLOBAL                  170: First_Straddle
        2410    LOAD_CONST                    30: False
        2412    STORE_GLOBAL                  171: King_Order_Placed
        2414    LOAD_CONST                    30: False
        2416    STORE_GLOBAL                  172: Queen_Order_Placed
        2418    LOAD_CONST                    30: False
        2420    STORE_GLOBAL                  173: King_Candle_Formed
        2422    LOAD_CONST                    30: False
        2424    STORE_GLOBAL                  174: Queen_Candle_Formed
        2426    LOAD_CONST                    30: False
        2428    STORE_GLOBAL                  175: K_Direction_Formed
        2430    LOAD_CONST                    30: False
        2432    STORE_GLOBAL                  176: King_Candle_Duration_Detection
        2434    LOAD_CONST                    30: False
        2436    STORE_NAME                    177: CE_SL_Triggered
        2438    LOAD_CONST                    30: False
        2440    STORE_NAME                    178: PE_SL_Triggered
        2442    LOAD_CONST                    30: False
        2444    STORE_NAME                    179: CE_TGT_Triggered
        2446    LOAD_CONST                    30: False
        2448    STORE_NAME                    180: PE_TGT_Triggered
        2450    LOAD_CONST                    30: False
        2452    STORE_GLOBAL                  181: partial_profit_booking_triggered
        2454    LOAD_CONST                    0: 0
        2456    STORE_GLOBAL                  182: partial_profit_booked
        2458    LOAD_CONST                    0: 0
        2460    STORE_NAME                    183: CE_LTP_Update_Count
        2462    LOAD_CONST                    0: 0
        2464    STORE_NAME                    184: PE_LTP_Update_Count
        2466    LOAD_CONST                    0: 0
        2468    STORE_NAME                    185: CE_LTP_old
        2470    LOAD_CONST                    0: 0
        2472    STORE_NAME                    186: PE_LTP_old
        2474    LOAD_CONST                    154: 35000
        2476    STORE_NAME                    187: Starting_LTP
        2478    LOAD_CONST                    155: 200
        2480    STORE_GLOBAL                  188: current_premium_delta
        2482    LOAD_CONST                    30: False
        2484    STORE_NAME                    189: Usr_Lic
        2486    LOAD_CONST                    0: 0
        2488    STORE_GLOBAL                  190: df_king_cnt
        2490    BUILD_LIST                    0
        2492    LOAD_CONST                    156: ('cur_HHMM', 'INST', 'Symbol', 'CE_PE', 'buy_sell', 'quantity', 'price', 'MTM')
        2494    LIST_EXTEND                   1
        2496    STORE_NAME                    191: df_cols
        2498    LOAD_NAME                     24: pd
        2500    LOAD_ATTR                     192: DataFrame
        2502    BUILD_LIST                    0
        2504    LOAD_NAME                     191: df_cols
        2506    LOAD_CONST                    157: ('data', 'columns')
        2508    CALL_FUNCTION_KW              2
        2510    STORE_GLOBAL                  193: df_king
        2512    LOAD_CONST                    0: 0
        2514    STORE_NAME                    194: df_runtime_cnt
        2516    BUILD_LIST                    0
        2518    LOAD_CONST                    158: ('cur_HHMM', 'CE_Leg_Position', 'PE_Leg_Position', 'Current_LTP', 'strike_ce', 'CE_Leg_Target', 'ltp_Index_ATM_CE', 'CE_Leg_SL', 'strike_pe', 'PE_Leg_Target', 'ltp_Index_ATM_PE', 'PE_Leg_SL', 'MTM_SL', 'MTM_TGT', 'Calc_MTM', 'Direction', 'King', 'King_SL', 'Queen', 'Queen_SL', 'King_ST', 'Queen_ST', 'Last_Traded_CE_Price', 'Last_Traded_PE_Price', 'MTM_Index')
        2520    LIST_EXTEND                   1
        2522    STORE_NAME                    195: df_runtime_cols
        2524    LOAD_NAME                     24: pd
        2526    LOAD_ATTR                     192: DataFrame
        2528    BUILD_LIST                    0
        2530    LOAD_NAME                     195: df_runtime_cols
        2532    LOAD_CONST                    157: ('data', 'columns')
        2534    CALL_FUNCTION_KW              2
        2536    STORE_NAME                    196: df_runtime
        2538    BUILD_LIST                    0
        2540    LOAD_CONST                    159: ('cur_HHMM', 'EXCH', 'TKN', 'NQ')
        2542    LIST_EXTEND                   1
        2544    STORE_NAME                    197: leg_cols
        2546    LOAD_NAME                     24: pd
        2548    LOAD_ATTR                     192: DataFrame
        2550    BUILD_LIST                    0
        2552    LOAD_NAME                     197: leg_cols
        2554    LOAD_CONST                    157: ('data', 'columns')
        2556    CALL_FUNCTION_KW              2
        2558    STORE_GLOBAL                  198: Current_CE_Leg
        2560    LOAD_NAME                     24: pd
        2562    LOAD_ATTR                     192: DataFrame
        2564    BUILD_LIST                    0
        2566    LOAD_NAME                     197: leg_cols
        2568    LOAD_CONST                    157: ('data', 'columns')
        2570    CALL_FUNCTION_KW              2
        2572    STORE_GLOBAL                  199: Current_PE_Leg
        2574    LOAD_NAME                     24: pd
        2576    LOAD_ATTR                     192: DataFrame
        2578    BUILD_LIST                    0
        2580    LOAD_NAME                     197: leg_cols
        2582    LOAD_CONST                    157: ('data', 'columns')
        2584    CALL_FUNCTION_KW              2
        2586    STORE_GLOBAL                  200: Current_legs
        2588    LOAD_NAME                     24: pd
        2590    LOAD_ATTR                     192: DataFrame
        2592    BUILD_LIST                    0
        2594    LOAD_NAME                     197: leg_cols
        2596    LOAD_CONST                    157: ('data', 'columns')
        2598    CALL_FUNCTION_KW              2
        2600    STORE_GLOBAL                  201: Current_CE_Leg_hedge
        2602    LOAD_NAME                     24: pd
        2604    LOAD_ATTR                     192: DataFrame
        2606    BUILD_LIST                    0
        2608    LOAD_NAME                     197: leg_cols
        2610    LOAD_CONST                    157: ('data', 'columns')
        2612    CALL_FUNCTION_KW              2
        2614    STORE_GLOBAL                  202: Current_PE_Leg_hedge
        2616    LOAD_NAME                     24: pd
        2618    LOAD_ATTR                     192: DataFrame
        2620    BUILD_LIST                    0
        2622    LOAD_NAME                     197: leg_cols
        2624    LOAD_CONST                    157: ('data', 'columns')
        2626    CALL_FUNCTION_KW              2
        2628    STORE_GLOBAL                  203: Current_legs_hedge
        2630    BUILD_MAP                     0
        2632    STORE_GLOBAL                  204: dict_ltp
        2634    BUILD_MAP                     0
        2636    STORE_NAME                    205: dict_sl_orders
        2638    LOAD_CONST                    160: '/export?format=csv&gid=0'
        2640    STORE_NAME                    206: param
        2642    LOAD_CONST                    0: 0
        2644    STORE_NAME                    207: cur_min
        2646    LOAD_CONST                    0: 0
        2648    STORE_NAME                    208: algo_min
        2650    LOAD_CONST                    0: 0
        2652    STORE_NAME                    209: king_min
        2654    LOAD_CONST                    0: 0
        2656    STORE_NAME                    210: log_min
        2658    LOAD_CONST                    0: 0
        2660    STORE_NAME                    211: log1_min
        2662    LOAD_CONST                    0: 0
        2664    STORE_NAME                    212: algo_min1
        2666    LOAD_CONST                    0: 0
        2668    STORE_NAME                    213: algo_3min
        2670    LOAD_CONST                    0: 0
        2672    STORE_NAME                    214: algo_sec1
        2674    LOAD_CONST                    0: 0
        2676    STORE_NAME                    215: King_ST_min
        2678    LOAD_CONST                    0: 0
        2680    STORE_NAME                    216: Queen_ST_min
        2682    LOAD_CONST                    52: 2
        2684    STORE_GLOBAL                  217: No_of_Days_Data
        2686    LOAD_NAME                     44: int
        2688    LOAD_NAME                     21: datetime
        2690    LOAD_ATTR                     21: datetime
        2692    LOAD_METHOD                   51: now
        2694    CALL_METHOD                   0
        2696    LOAD_METHOD                   52: strftime
        2698    LOAD_CONST                    24: '%Y%m%d'
        2700    CALL_METHOD                   1
        2702    CALL_FUNCTION                 1
        2704    STORE_NAME                    218: a
        2706    LOAD_CONST                    161: 0
        2708    STORE_GLOBAL                  219: Paper_MTM
        2710    LOAD_CONST                    161: 0
        2712    STORE_NAME                    220: Paper_MTM_old
        2714    LOAD_CONST                    161: 0
        2716    STORE_GLOBAL                  221: Last_Traded_PE_Price
        2718    LOAD_CONST                    161: 0
        2720    STORE_GLOBAL                  222: Last_Traded_CE_Price
        2722    LOAD_CONST                    161: 0
        2724    STORE_GLOBAL                  223: Last_Traded_PE_Price_hedge
        2726    LOAD_CONST                    161: 0
        2728    STORE_GLOBAL                  224: Last_Traded_CE_Price_hedge
        2730    LOAD_CONST                    161: 0
        2732    STORE_GLOBAL                  225: Last_Traded_PE_Price_PP
        2734    LOAD_CONST                    161: 0
        2736    STORE_GLOBAL                  226: Last_Traded_CE_Price_PP
        2738    LOAD_CONST                    161: 0
        2740    STORE_GLOBAL                  227: Last_Traded_PE_Price_hedge_PP
        2742    LOAD_CONST                    161: 0
        2744    STORE_GLOBAL                  228: Last_Traded_CE_Price_hedge_PP
        2746    LOAD_CONST                    161: 0
        2748    STORE_NAME                    229: MTM
        2750    LOAD_CONST                    161: 0
        2752    STORE_GLOBAL                  230: MTM_BANK
        2754    LOAD_CONST                    161: 0
        2756    STORE_GLOBAL                  231: MTM_Index
        2758    LOAD_CONST                    0: 0
        2760    STORE_GLOBAL                  232: pos_bank
        2762    LOAD_CONST                    161: 0
        2764    STORE_GLOBAL                  233: MTM_NIFTY
        2766    LOAD_CONST                    0: 0
        2768    STORE_GLOBAL                  234: pos_nifty
        2770    LOAD_NAME                     44: int
        2772    LOAD_NAME                     218: a
        2774    LOAD_CONST                    59: 6
        2776    BINARY_MULTIPLY               
        2778    CALL_FUNCTION                 1
        2780    STORE_NAME                    235: b
        2782    LOAD_CONST                    30: False
        2784    STORE_GLOBAL                  236: processIndexExitTradenow
        2786    LOAD_CONST                    162: 60690993
        2788    STORE_NAME                    237: d
        2790    LOAD_CONST                    163: '1mtBg2KYcL4KipCdtXszwi8rPm3WwpajJyD9laoODgdo'
        2792    STORE_NAME                    238: key
        2794    LOAD_CONST                    164: -5000
        2796    STORE_GLOBAL                  239: Perlot_MTM_SL
        2798    LOAD_CONST                    165: 15000
        2800    STORE_GLOBAL                  240: Perlot_MTM_Target
        2802    LOAD_CONST                    73: 100
        2804    STORE_GLOBAL                  241: StikeAdj_SLPer
        2806    LOAD_CONST                    166: 75
        2808    STORE_GLOBAL                  242: StikeAdj_TgtPer
        2810    LOAD_CONST                    167: 1000
        2812    STORE_GLOBAL                  243: Perlot_MTM_lock_profit_threshold
        2814    LOAD_CONST                    168: -3500
        2816    STORE_GLOBAL                  244: Perlot_MTM_lock_profit
        2818    LOAD_CONST                    167: 1000
        2820    STORE_GLOBAL                  245: Perlot_MTM_Trailing
        2822    LOAD_CONST                    0: 0
        2824    STORE_GLOBAL                  246: Perlot_MTM_Trailing_New
        2826    LOAD_CONST                    29: 1
        2828    STORE_GLOBAL                  247: Synthetic_Fut
        2830    LOAD_CONST                    29: 1
        2832    STORE_GLOBAL                  248: Single_Leg_Adj
        2834    LOAD_CONST                    169: 50
        2836    STORE_GLOBAL                  249: Single_Leg_Adj_Delta_PCT
        2838    LOAD_CONST                    167: 1000
        2840    STORE_GLOBAL                  250: CE_Leg_SL
        2842    LOAD_CONST                    167: 1000
        2844    STORE_GLOBAL                  251: PE_Leg_SL
        2846    LOAD_CONST                    0: 0
        2848    STORE_GLOBAL                  252: CE_Leg_Target
        2850    LOAD_CONST                    0: 0
        2852    STORE_GLOBAL                  253: PE_Leg_Target
        2854    LOAD_CONST                    170: 1111
        2856    STORE_GLOBAL                  254: token_Index_ce
        2858    LOAD_CONST                    171: 2222
        2860    STORE_GLOBAL                  255: token_Index_pe
        2862    LOAD_CONST                    170: 1111
        2864    STORE_GLOBAL                  256: token_Index_ce_hedge
        2868    LOAD_CONST                    171: 2222
        2870    STORE_GLOBAL                  257: token_Index_pe_hedge
        2874    LOAD_CONST                    172: 1122
        2876    STORE_GLOBAL                  258: token_Index_ce_old
        2880    LOAD_CONST                    173: 2233
        2882    STORE_GLOBAL                  259: token_Index_pe_old
        2886    LOAD_CONST                    0: 0
        2888    STORE_GLOBAL                  260: Index_CE_atm
        2892    LOAD_CONST                    0: 0
        2894    STORE_GLOBAL                  261: Index_PE_atm
        2898    LOAD_CONST                    0: 0
        2900    STORE_NAME                    262: current_strike_ce
        2904    LOAD_CONST                    0: 0
        2906    STORE_NAME                    263: current_strike_pe
        2910    LOAD_CONST                    0: 0
        2912    STORE_GLOBAL                  264: ltp_Index_ATM_CE
        2916    LOAD_CONST                    0: 0
        2918    STORE_GLOBAL                  265: ltp_Index_ATM_PE
        2922    LOAD_CONST                    0: 0
        2924    STORE_GLOBAL                  266: ltp_Index_ATM_CE_hedge
        2928    LOAD_CONST                    0: 0
        2930    STORE_GLOBAL                  267: ltp_Index_ATM_PE_hedge
        2934    LOAD_CONST                    174: 1000000
        2936    STORE_GLOBAL                  268: King
        2940    LOAD_CONST                    175: 100000
        2942    STORE_GLOBAL                  269: King_SL
        2946    LOAD_CONST                    174: 1000000
        2948    STORE_GLOBAL                  270: First_King
        2952    LOAD_CONST                    174: 1000000
        2954    STORE_GLOBAL                  271: First_King_L
        2958    LOAD_CONST                    174: 1000000
        2960    STORE_GLOBAL                  272: First_King_SL
        2964    LOAD_CONST                    174: 1000000
        2966    STORE_GLOBAL                  273: Latest_King
        2970    LOAD_CONST                    174: 1000000
        2972    STORE_GLOBAL                  274: Latest_King_L
        2976    LOAD_CONST                    174: 1000000
        2978    STORE_GLOBAL                  275: Latest_King_SL
        2982    LOAD_NAME                     44: int
        2984    LOAD_NAME                     235: b
        2986    LOAD_CONST                    52: 2
        2988    BINARY_TRUE_DIVIDE            
        2990    CALL_FUNCTION                 1
        2992    STORE_NAME                    276: c
        2996    LOAD_NAME                     70: susr
        2998    STORE_NAME                    66: f
        3000    LOAD_CONST                    176: 'NTUzMjM5'
        3002    STORE_NAME                    277: base64_string
        3006    LOAD_NAME                     277: base64_string
        3010    LOAD_METHOD                   278: encode
        3014    LOAD_CONST                    177: 'ascii'
        3016    CALL_METHOD                   1
        3018    STORE_NAME                    279: base64_bytes
        3022    LOAD_NAME                     9: base64
        3024    LOAD_METHOD                   280: b64decode
        3028    LOAD_NAME                     279: base64_bytes
        3032    CALL_METHOD                   1
        3034    STORE_NAME                    281: sample_string_bytes
        3038    LOAD_NAME                     281: sample_string_bytes
        3042    LOAD_METHOD                   282: decode
        3046    LOAD_CONST                    177: 'ascii'
        3048    CALL_METHOD                   1
        3050    STORE_NAME                    283: sample_string
        3054    LOAD_CONST                    178: 'https://docs.google.com/spreadsheets/d/'
        3056    STORE_NAME                    284: link
        3060    LOAD_CONST                    0: 0
        3062    STORE_GLOBAL                  285: Queen
        3066    LOAD_CONST                    0: 0
        3068    STORE_GLOBAL                  286: Queen_SL
        3072    LOAD_CONST                    0: 0
        3074    STORE_GLOBAL                  287: First_Queen
        3078    LOAD_CONST                    0: 0
        3080    STORE_GLOBAL                  288: First_Queen_H
        3084    LOAD_CONST                    0: 0
        3086    STORE_GLOBAL                  289: First_Queen_SL
        3090    LOAD_CONST                    0: 0
        3092    STORE_GLOBAL                  290: Latest_Queen
        3096    LOAD_CONST                    0: 0
        3098    STORE_GLOBAL                  291: Latest_Queen_H
        3102    LOAD_CONST                    0: 0
        3104    STORE_GLOBAL                  292: Latest_Queen_SL
        3108    LOAD_CONST                    0: 0
        3110    STORE_GLOBAL                  293: King_ST
        3114    LOAD_CONST                    175: 100000
        3116    STORE_GLOBAL                  294: Queen_ST
        3120    LOAD_CONST                    179: 30000
        3122    STORE_GLOBAL                  295: Candle_Close
        3126    LOAD_CONST                    0: 0
        3128    STORE_GLOBAL                  296: K_Direction
        3132    LOAD_CONST                    0: 0
        3134    STORE_NAME                    297: K_Direction_Change_Count
        3138    LOAD_CONST                    161: 0
        3140    STORE_NAME                    298: Single_Leg_Triggered_LTP
        3144    LOAD_NAME                     284: link
        3148    LOAD_NAME                     238: key
        3150    BINARY_ADD                    
        3152    LOAD_NAME                     206: param
        3154    BINARY_ADD                    
        3156    STORE_NAME                    299: url
        3160    LOAD_NAME                     24: pd
        3162    LOAD_METHOD                   300: read_csv
        3166    LOAD_NAME                     299: url
        3170    CALL_METHOD                   1
        3172    STORE_NAME                    301: dfurl
        3176    LOAD_NAME                     44: int
        3178    LOAD_NAME                     21: datetime
        3180    LOAD_ATTR                     21: datetime
        3182    LOAD_METHOD                   51: now
        3184    CALL_METHOD                   0
        3186    LOAD_METHOD                   52: strftime
        3188    LOAD_CONST                    24: '%Y%m%d'
        3190    CALL_METHOD                   1
        3192    CALL_FUNCTION                 1
        3194    STORE_NAME                    302: lic
        3198    LOAD_CONST                    180: <CODE> getHolidays
        3200    LOAD_CONST                    181: 'getHolidays'
        3202    MAKE_FUNCTION                 0
        3204    STORE_NAME                    303: getHolidays
        3208    LOAD_CONST                    182: <CODE> isHoliday
        3210    LOAD_CONST                    183: 'isHoliday'
        3212    MAKE_FUNCTION                 0
        3214    STORE_NAME                    304: isHoliday
        3218    LOAD_CONST                    184: <CODE> isTodayHoliday
        3220    LOAD_CONST                    185: 'isTodayHoliday'
        3222    MAKE_FUNCTION                 0
        3224    STORE_NAME                    305: isTodayHoliday
        3228    LOAD_CONST                    186: <CODE> convertToDateStr
        3230    LOAD_CONST                    187: 'convertToDateStr'
        3232    MAKE_FUNCTION                 0
        3234    STORE_NAME                    306: convertToDateStr
        3238    LOAD_CONST                    188: <CODE> get_realtime_config
        3240    LOAD_CONST                    189: 'get_realtime_config'
        3242    MAKE_FUNCTION                 0
        3244    STORE_NAME                    307: get_realtime_config
        3248    LOAD_CONST                    190: <CODE> place_order
        3250    LOAD_CONST                    191: 'place_order'
        3252    MAKE_FUNCTION                 0
        3254    STORE_NAME                    308: place_order
        3258    LOAD_CONST                    192: <CODE> get_order_status
        3260    LOAD_CONST                    193: 'get_order_status'
        3262    MAKE_FUNCTION                 0
        3264    STORE_NAME                    309: get_order_status
        3268    LOAD_CONST                    194: <CODE> get_order_price
        3270    LOAD_CONST                    195: 'get_order_price'
        3272    MAKE_FUNCTION                 0
        3274    STORE_NAME                    310: get_order_price
        3278    LOAD_CONST                    196: <CODE> get_order_symbol
        3280    LOAD_CONST                    197: 'get_order_symbol'
        3282    MAKE_FUNCTION                 0
        3284    STORE_NAME                    311: get_order_symbol
        3288    LOAD_CONST                    461: ('BANKNIFTY', '22022022', False, 37000, True)
        3292    LOAD_CONST                    201: <CODE> get_instrument_for_fno
        3294    LOAD_CONST                    202: 'get_instrument_for_fno'
        3296    MAKE_FUNCTION                 1
        3298    STORE_NAME                    312: get_instrument_for_fno
        3302    LOAD_CONST                    461: ('BANKNIFTY', '22022022', False, 37000, True)
        3306    LOAD_CONST                    203: <CODE> get_lot_size
        3308    LOAD_CONST                    204: 'get_lot_size'
        3310    MAKE_FUNCTION                 1
        3312    STORE_NAME                    313: get_lot_size
        3316    LOAD_CONST                    462: ('NSE', 'NIFTY BANK')
        3320    LOAD_CONST                    207: <CODE> get_instrument_by_symbol
        3322    LOAD_CONST                    208: 'get_instrument_by_symbol'
        3324    MAKE_FUNCTION                 1
        3326    STORE_NAME                    314: get_instrument_by_symbol
        3330    LOAD_CONST                    463: ('NFO', 260105)
        3334    LOAD_CONST                    211: <CODE> get_instrument_by_token
        3336    LOAD_CONST                    212: 'get_instrument_by_token'
        3338    MAKE_FUNCTION                 1
        3340    STORE_NAME                    315: get_instrument_by_token
        3344    LOAD_CONST                    213: <CODE> getLTP
        3346    LOAD_CONST                    214: 'getLTP'
        3348    MAKE_FUNCTION                 0
        3350    STORE_NAME                    316: getLTP
        3354    LOAD_CONST                    215: <CODE> get_bid_ask
        3356    LOAD_CONST                    216: 'get_bid_ask'
        3358    MAKE_FUNCTION                 0
        3360    STORE_NAME                    317: get_bid_ask
        3364    LOAD_CONST                    217: <CODE> round_nearest
        3366    LOAD_CONST                    218: 'round_nearest'
        3368    MAKE_FUNCTION                 0
        3370    STORE_NAME                    318: round_nearest
        3374    LOAD_CONST                    219: <CODE> close_partial_orders
        3376    LOAD_CONST                    220: 'close_partial_orders'
        3378    MAKE_FUNCTION                 0
        3380    STORE_NAME                    319: close_partial_orders
        3384    LOAD_CONST                    221: <CODE> close_partial_hedge_orders
        3386    LOAD_CONST                    222: 'close_partial_hedge_orders'
        3388    MAKE_FUNCTION                 0
        3390    STORE_NAME                    320: close_partial_hedge_orders
        3394    LOAD_CONST                    223: <CODE> partial_squareoff
        3396    LOAD_CONST                    224: 'partial_squareoff'
        3398    MAKE_FUNCTION                 0
        3400    STORE_NAME                    321: partial_squareoff
        3404    LOAD_CONST                    225: <CODE> close_all_orders
        3406    LOAD_CONST                    226: 'close_all_orders'
        3408    MAKE_FUNCTION                 0
        3410    STORE_NAME                    322: close_all_orders
        3414    LOAD_CONST                    227: <CODE> close_all_hedge_orders
        3416    LOAD_CONST                    228: 'close_all_hedge_orders'
        3418    MAKE_FUNCTION                 0
        3420    STORE_NAME                    323: close_all_hedge_orders
        3424    LOAD_CONST                    229: <CODE> squareoff
        3426    LOAD_CONST                    230: 'squareoff'
        3428    MAKE_FUNCTION                 0
        3430    STORE_NAME                    324: squareoff
        3434    LOAD_CONST                    231: <CODE> check_MTM_Limit
        3436    LOAD_CONST                    232: 'check_MTM_Limit'
        3438    MAKE_FUNCTION                 0
        3440    STORE_NAME                    325: check_MTM_Limit
        3444    LOAD_CONST                    233: <CODE> closest
        3446    LOAD_CONST                    234: 'closest'
        3448    MAKE_FUNCTION                 0
        3450    STORE_NAME                    326: closest
        3454    LOAD_CONST                    464: ('NIFTY', 33000, 75, '01SEP22')
        3458    LOAD_CONST                    238: <CODE> get_ce_strike
        3460    LOAD_CONST                    239: 'get_ce_strike'
        3462    MAKE_FUNCTION                 1
        3464    STORE_NAME                    327: get_ce_strike
        3468    LOAD_CONST                    464: ('NIFTY', 33000, 75, '01SEP22')
        3472    LOAD_CONST                    240: <CODE> get_pe_strike
        3474    LOAD_CONST                    241: 'get_pe_strike'
        3476    MAKE_FUNCTION                 1
        3478    STORE_NAME                    328: get_pe_strike
        3482    LOAD_CONST                    464: ('NIFTY', 33000, 75, '01SEP22')
        3486    LOAD_CONST                    242: <CODE> get_ce_hedge_strike
        3488    LOAD_CONST                    243: 'get_ce_hedge_strike'
        3490    MAKE_FUNCTION                 1
        3492    STORE_NAME                    329: get_ce_hedge_strike
        3496    LOAD_CONST                    464: ('NIFTY', 33000, 75, '01SEP22')
        3500    LOAD_CONST                    244: <CODE> get_pe_hedge_strike
        3502    LOAD_CONST                    245: 'get_pe_hedge_strike'
        3504    MAKE_FUNCTION                 1
        3506    STORE_NAME                    330: get_pe_hedge_strike
        3510    LOAD_CONST                    465: ('ALL',)
        3514    LOAD_CONST                    247: <CODE> get_option_tokens
        3516    LOAD_CONST                    248: 'get_option_tokens'
        3518    MAKE_FUNCTION                 1
        3520    STORE_NAME                    331: get_option_tokens
        3524    LOAD_CONST                    249: <CODE> King_candle
        3526    LOAD_CONST                    250: 'King_candle'
        3528    MAKE_FUNCTION                 0
        3530    STORE_NAME                    332: King_candle
        3534    LOAD_CONST                    251: <CODE> subscribe_ins
        3536    LOAD_CONST                    252: 'subscribe_ins'
        3538    MAKE_FUNCTION                 0
        3540    STORE_NAME                    333: subscribe_ins
        3544    LOAD_CONST                    466: (False,)
        3548    LOAD_CONST                    253: <CODE> get_historical
        3550    LOAD_CONST                    254: 'get_historical'
        3552    MAKE_FUNCTION                 1
        3554    STORE_NAME                    334: get_historical
        3558    LOAD_CONST                    255: <CODE> event_handler_order_update
        3560    LOAD_CONST                    256: 'event_handler_order_update'
        3564    MAKE_FUNCTION                 0
        3566    STORE_NAME                    335: event_handler_order_update
        3570    LOAD_CONST                    257: <CODE> event_handler_quote_update
        3574    LOAD_CONST                    258: 'event_handler_quote_update'
        3578    MAKE_FUNCTION                 0
        3580    STORE_NAME                    336: event_handler_quote_update
        3584    LOAD_CONST                    259: <CODE> open_callback
        3588    LOAD_CONST                    260: 'open_callback'
        3592    MAKE_FUNCTION                 0
        3594    STORE_NAME                    337: open_callback
        3598    LOAD_CONST                    261: <CODE> error_callback
        3602    LOAD_CONST                    262: 'error_callback'
        3606    MAKE_FUNCTION                 0
        3608    STORE_NAME                    338: error_callback
        3612    LOAD_CONST                    263: <CODE> close_callback
        3616    LOAD_CONST                    264: 'close_callback'
        3620    MAKE_FUNCTION                 0
        3622    STORE_NAME                    339: close_callback
        3626    LOAD_NAME                     301: dfurl
        3630    LOAD_METHOD                   340: iterrows
        3634    CALL_METHOD                   0
        3636    GET_ITER                      
        3638    FOR_ITER                      28 (to 3696)
        3640    UNPACK_SEQUENCE               2
        3642    STORE_NAME                    341: index
        3646    STORE_NAME                    342: row
        3650    LOAD_NAME                     342: row
        3654    LOAD_CONST                    265: 'Username'
        3658    BINARY_SUBSCR                 
        3660    LOAD_NAME                     70: susr
        3662    COMPARE_OP                    2 (==)
        3664    POP_JUMP_IF_FALSE             1846 (to 3692)
        3668    LOAD_NAME                     302: lic
        3672    LOAD_NAME                     342: row
        3676    LOAD_CONST                    266: 'Algo_King'
        3680    BINARY_SUBSCR                 
        3682    COMPARE_OP                    0 (<)
        3684    POP_JUMP_IF_FALSE             1846 (to 3692)
        3688    LOAD_CONST                    20: True
        3690    STORE_NAME                    189: Usr_Lic
        3692    JUMP_ABSOLUTE                 1819 (to 3638)
        3696    LOAD_NAME                     44: int
        3698    LOAD_NAME                     21: datetime
        3700    LOAD_ATTR                     21: datetime
        3702    LOAD_METHOD                   51: now
        3704    CALL_METHOD                   0
        3706    LOAD_METHOD                   52: strftime
        3708    LOAD_CONST                    50: '%H%M'
        3710    CALL_METHOD                   1
        3712    CALL_FUNCTION                 1
        3714    STORE_GLOBAL                  76: cur_HHMM
        3716    LOAD_NAME                     189: Usr_Lic
        3718    POP_JUMP_IF_TRUE              1888 (to 3776)
        3722    LOAD_NAME                     61: set_config_value
        3724    LOAD_CONST                    48: 'status'
        3726    LOAD_CONST                    49: 'algo_running_status'
        3728    LOAD_CONST                    122: '0'
        3730    CALL_FUNCTION                 3
        3732    POP_TOP                       
        3734    LOAD_NAME                     62: savedata
        3736    CALL_FUNCTION                 0
        3738    POP_TOP                       
        3740    LOAD_NAME                     59: iLog
        3742    LOAD_CONST                    267: ' Shutter down... Calling sys.exit() @ '
        3746    LOAD_NAME                     343: str
        3750    LOAD_GLOBAL                   76: read
        3752    CALL_FUNCTION                 1
        3754    BINARY_ADD                    
        3756    LOAD_CONST                    42: 4
        3758    LOAD_CONST                    20: True
        3760    LOAD_CONST                    43: ('sendTeleMsg',)
        3762    CALL_FUNCTION_KW              3
        3764    POP_TOP                       
        3766    LOAD_NAME                     0: sys
        3768    LOAD_METHOD                   344: exit
        3772    CALL_METHOD                   0
        3774    POP_TOP                       
        3776    LOAD_NAME                     59: iLog
        3778    LOAD_CONST                    268: ' User = '
        3782    LOAD_NAME                     70: susr
        3784    BINARY_ADD                    
        3786    CALL_FUNCTION                 1
        3788    POP_TOP                       
        3790    LOAD_NAME                     56: open
        3792    LOAD_CONST                    269: 'holidays.json'
        3796    LOAD_CONST                    270: 'r'
        3800    CALL_FUNCTION                 2
        3802    SETUP_WITH                    16
        3804    STORE_NAME                    345: holidays
        3808    LOAD_NAME                     5: json
        3810    LOAD_METHOD                   67: load
        3812    LOAD_NAME                     345: holidays
        3816    CALL_METHOD                   1
        3818    STORE_NAME                    346: holidaysData
        3822    POP_BLOCK                     
        3824    LOAD_CONST                    1: None
        3826    DUP_TOP                       
        3828    DUP_TOP                       
        3830    CALL_FUNCTION                 3
        3832    POP_TOP                       
        3834    JUMP_FORWARD                  9 (to 3854)
        3836    WITH_EXCEPT_START             
        3838    POP_JUMP_IF_TRUE              1922 (to 3844)
        3842    RERAISE                       1
        3844    POP_TOP                       
        3846    POP_TOP                       
        3848    POP_TOP                       
        3850    POP_EXCEPT                    
        3852    POP_TOP                       
        3854    LOAD_NAME                     21: datetime
        3856    LOAD_ATTR                     347: date
        3860    LOAD_METHOD                   348: today
        3864    CALL_METHOD                   0
        3866    LOAD_NAME                     21: datetime
        3868    LOAD_METHOD                   349: timedelta
        3872    LOAD_CONST                    271: 3
        3876    LOAD_NAME                     21: datetime
        3878    LOAD_ATTR                     347: date
        3882    LOAD_METHOD                   348: today
        3886    CALL_METHOD                   0
        3888    LOAD_METHOD                   350: weekday
        3892    CALL_METHOD                   0
        3894    BINARY_SUBTRACT               
        3896    LOAD_CONST                    272: 7
        3900    BINARY_MODULO                 
        3902    CALL_METHOD                   1
        3904    BINARY_ADD                    
        3906    STORE_GLOBAL                  351: expiry_date
        3910    LOAD_NAME                     343: str
        3914    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        3918    CALL_FUNCTION                 1
        3920    LOAD_NAME                     346: holidaysData
        3924    CONTAINS_OP                   0 (in)
        3926    POP_JUMP_IF_FALSE             1977 (to 3954)
        3930    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        3934    LOAD_NAME                     21: datetime
        3936    LOAD_ATTR                     349: timedelta
        3940    LOAD_CONST                    29: 1
        3942    LOAD_CONST                    273: ('days',)
        3946    CALL_FUNCTION_KW              1
        3948    BINARY_SUBTRACT               
        3950    STORE_GLOBAL                  351: expiry_date
        3954    LOAD_NAME                     343: str
        3958    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        3962    CALL_FUNCTION                 1
        3964    LOAD_NAME                     346: holidaysData
        3968    CONTAINS_OP                   0 (in)
        3970    POP_JUMP_IF_FALSE             1999 (to 3998)
        3974    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        3978    LOAD_NAME                     21: datetime
        3980    LOAD_ATTR                     349: timedelta
        3984    LOAD_CONST                    29: 1
        3986    LOAD_CONST                    273: ('days',)
        3990    CALL_FUNCTION_KW              1
        3992    BINARY_SUBTRACT               
        3994    STORE_GLOBAL                  351: expiry_date
        3998    LOAD_NAME                     343: str
        4002    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4006    CALL_FUNCTION                 1
        4008    LOAD_NAME                     346: holidaysData
        4012    CONTAINS_OP                   0 (in)
        4014    POP_JUMP_IF_FALSE             2021 (to 4042)
        4018    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4022    LOAD_NAME                     21: datetime
        4024    LOAD_ATTR                     349: timedelta
        4028    LOAD_CONST                    29: 1
        4030    LOAD_CONST                    273: ('days',)
        4034    CALL_FUNCTION_KW              1
        4036    BINARY_SUBTRACT               
        4038    STORE_GLOBAL                  351: expiry_date
        4042    LOAD_GLOBAL                   83: NULL + strChatID
        4044    LOAD_CONST                    29: 1
        4046    COMPARE_OP                    2 (==)
        4048    POP_JUMP_IF_FALSE             2120 (to 4240)
        4052    LOAD_NAME                     21: datetime
        4054    LOAD_ATTR                     347: date
        4058    LOAD_METHOD                   348: today
        4062    CALL_METHOD                   0
        4064    LOAD_NAME                     21: datetime
        4066    LOAD_METHOD                   349: timedelta
        4070    LOAD_CONST                    29: 1
        4072    LOAD_NAME                     21: datetime
        4074    LOAD_ATTR                     347: date
        4078    LOAD_METHOD                   348: today
        4082    CALL_METHOD                   0
        4084    LOAD_METHOD                   350: weekday
        4088    CALL_METHOD                   0
        4090    BINARY_SUBTRACT               
        4092    LOAD_CONST                    272: 7
        4096    BINARY_MODULO                 
        4098    CALL_METHOD                   1
        4100    BINARY_ADD                    
        4102    STORE_GLOBAL                  351: expiry_date
        4106    LOAD_NAME                     343: str
        4110    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4114    CALL_FUNCTION                 1
        4116    LOAD_NAME                     346: holidaysData
        4120    CONTAINS_OP                   0 (in)
        4122    POP_JUMP_IF_FALSE             2075 (to 4150)
        4126    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4130    LOAD_NAME                     21: datetime
        4132    LOAD_ATTR                     349: timedelta
        4136    LOAD_CONST                    29: 1
        4138    LOAD_CONST                    273: ('days',)
        4142    CALL_FUNCTION_KW              1
        4144    BINARY_SUBTRACT               
        4146    STORE_GLOBAL                  351: expiry_date
        4150    LOAD_NAME                     343: str
        4154    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4158    CALL_FUNCTION                 1
        4160    LOAD_NAME                     346: holidaysData
        4164    CONTAINS_OP                   0 (in)
        4166    POP_JUMP_IF_FALSE             2098 (to 4196)
        4170    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4174    LOAD_NAME                     21: datetime
        4176    LOAD_ATTR                     349: timedelta
        4180    LOAD_CONST                    271: 3
        4184    LOAD_CONST                    273: ('days',)
        4188    CALL_FUNCTION_KW              1
        4190    BINARY_SUBTRACT               
        4192    STORE_GLOBAL                  351: expiry_date
        4196    LOAD_NAME                     343: str
        4200    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4204    CALL_FUNCTION                 1
        4206    LOAD_NAME                     346: holidaysData
        4210    CONTAINS_OP                   0 (in)
        4212    POP_JUMP_IF_FALSE             2120 (to 4240)
        4216    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4220    LOAD_NAME                     21: datetime
        4222    LOAD_ATTR                     349: timedelta
        4226    LOAD_CONST                    29: 1
        4228    LOAD_CONST                    273: ('days',)
        4232    CALL_FUNCTION_KW              1
        4234    BINARY_SUBTRACT               
        4236    STORE_GLOBAL                  351: expiry_date
        4240    LOAD_NAME                     59: iLog
        4242    LOAD_CONST                    274: ' Expiry Date = '
        4246    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        4250    LOAD_METHOD                   52: strftime
        4252    LOAD_CONST                    275: '%d%b%y'
        4256    CALL_METHOD                   1
        4258    LOAD_METHOD                   352: upper
        4262    CALL_METHOD                   0
        4264    FORMAT_VALUE                  0
        4266    BUILD_STRING                  2
        4268    LOAD_CONST                    29: 1
        4270    LOAD_CONST                    20: True
        4272    LOAD_CONST                    43: ('sendTeleMsg',)
        4274    CALL_FUNCTION_KW              3
        4276    POP_TOP                       
        4278    LOAD_NAME                     44: int
        4280    LOAD_NAME                     21: datetime
        4282    LOAD_ATTR                     21: datetime
        4284    LOAD_METHOD                   51: now
        4286    CALL_METHOD                   0
        4288    LOAD_METHOD                   52: strftime
        4290    LOAD_CONST                    50: '%H%M'
        4292    CALL_METHOD                   1
        4294    CALL_FUNCTION                 1
        4296    STORE_GLOBAL                  76: cur_HHMM
        4298    LOAD_NAME                     305: isTodayHoliday
        4302    CALL_FUNCTION                 0
        4304    POP_JUMP_IF_FALSE             2196 (to 4392)
        4308    LOAD_GLOBAL                   161: NULL + ExitTradenow
        4310    LOAD_CONST                    0: 0
        4312    COMPARE_OP                    2 (==)
        4314    POP_JUMP_IF_FALSE             2196 (to 4392)
        4318    LOAD_CONST                    276: ' Today is market holiday. Stopping Algo for the day'
        4322    STORE_NAME                    65: strMsg
        4324    LOAD_NAME                     59: iLog
        4326    LOAD_NAME                     65: strMsg
        4328    LOAD_CONST                    42: 4
        4330    LOAD_CONST                    20: True
        4332    LOAD_CONST                    43: ('sendTeleMsg',)
        4334    CALL_FUNCTION_KW              3
        4336    POP_TOP                       
        4338    LOAD_NAME                     61: set_config_value
        4340    LOAD_CONST                    48: 'status'
        4342    LOAD_CONST                    49: 'algo_running_status'
        4344    LOAD_CONST                    122: '0'
        4346    CALL_FUNCTION                 3
        4348    POP_TOP                       
        4350    LOAD_NAME                     62: savedata
        4352    CALL_FUNCTION                 0
        4354    POP_TOP                       
        4356    LOAD_NAME                     59: iLog
        4358    LOAD_CONST                    267: ' Shutter down... Calling sys.exit() @ '
        4362    LOAD_NAME                     343: str
        4366    LOAD_GLOBAL                   76: read
        4368    CALL_FUNCTION                 1
        4370    BINARY_ADD                    
        4372    LOAD_CONST                    42: 4
        4374    LOAD_CONST                    20: True
        4376    LOAD_CONST                    43: ('sendTeleMsg',)
        4378    CALL_FUNCTION_KW              3
        4380    POP_TOP                       
        4382    LOAD_NAME                     0: sys
        4384    LOAD_METHOD                   344: exit
        4388    CALL_METHOD                   0
        4390    POP_TOP                       
        4392    LOAD_NAME                     44: int
        4394    LOAD_NAME                     21: datetime
        4396    LOAD_ATTR                     21: datetime
        4398    LOAD_METHOD                   51: now
        4400    CALL_METHOD                   0
        4402    LOAD_METHOD                   52: strftime
        4404    LOAD_CONST                    50: '%H%M'
        4406    CALL_METHOD                   1
        4408    CALL_FUNCTION                 1
        4410    STORE_GLOBAL                  76: cur_HHMM
        4412    LOAD_GLOBAL                   77: NULL + read
        4414    LOAD_CONST                    29: 1
        4416    COMPARE_OP                    3 (!=)
        4418    POP_JUMP_IF_TRUE              2216 (to 4432)
        4422    LOAD_GLOBAL                   79: NULL + get
        4424    LOAD_CONST                    0: 0
        4426    COMPARE_OP                    2 (==)
        4428    POP_JUMP_IF_FALSE             2253 (to 4506)
        4432    LOAD_CONST                    277: ' Algo_Trading flag Disabled or no of lots set to zero. No trading for the day'
        4436    STORE_NAME                    65: strMsg
        4438    LOAD_NAME                     59: iLog
        4440    LOAD_NAME                     65: strMsg
        4442    LOAD_CONST                    42: 4
        4444    LOAD_CONST                    20: True
        4446    LOAD_CONST                    43: ('sendTeleMsg',)
        4448    CALL_FUNCTION_KW              3
        4450    POP_TOP                       
        4452    LOAD_NAME                     61: set_config_value
        4454    LOAD_CONST                    48: 'status'
        4456    LOAD_CONST                    49: 'algo_running_status'
        4458    LOAD_CONST                    122: '0'
        4460    CALL_FUNCTION                 3
        4462    POP_TOP                       
        4464    LOAD_NAME                     62: savedata
        4466    CALL_FUNCTION                 0
        4468    POP_TOP                       
        4470    LOAD_NAME                     59: iLog
        4472    LOAD_CONST                    267: ' Shutter down... Calling sys.exit() @ '
        4476    LOAD_NAME                     343: str
        4480    LOAD_GLOBAL                   76: read
        4482    CALL_FUNCTION                 1
        4484    BINARY_ADD                    
        4486    LOAD_CONST                    42: 4
        4488    LOAD_CONST                    20: True
        4490    LOAD_CONST                    43: ('sendTeleMsg',)
        4492    CALL_FUNCTION_KW              3
        4494    POP_TOP                       
        4496    LOAD_NAME                     0: sys
        4498    LOAD_METHOD                   344: exit
        4502    CALL_METHOD                   0
        4504    POP_TOP                       
        4506    LOAD_NAME                     44: int
        4508    LOAD_NAME                     21: datetime
        4510    LOAD_ATTR                     21: datetime
        4512    LOAD_METHOD                   51: now
        4514    CALL_METHOD                   0
        4516    LOAD_METHOD                   52: strftime
        4518    LOAD_CONST                    50: '%H%M'
        4520    CALL_METHOD                   1
        4522    CALL_FUNCTION                 1
        4524    STORE_GLOBAL                  76: cur_HHMM
        4526    LOAD_GLOBAL                   81: NULL + strAdminChatID
        4528    LOAD_GLOBAL                   82: strChatID
        4530    BINARY_ADD                    
        4532    LOAD_GLOBAL                   83: NULL + strChatID
        4534    BINARY_ADD                    
        4536    LOAD_CONST                    29: 1
        4538    COMPARE_OP                    3 (!=)
        4540    POP_JUMP_IF_FALSE             2309 (to 4618)
        4544    LOAD_CONST                    278: ' Only one of these flag should be set to 1, check settings and restart: Trade_Nifty,Trade_BankNifty,Trade_FinNifty'
        4548    STORE_NAME                    65: strMsg
        4550    LOAD_NAME                     59: iLog
        4552    LOAD_NAME                     65: strMsg
        4554    LOAD_CONST                    42: 4
        4556    LOAD_CONST                    20: True
        4558    LOAD_CONST                    43: ('sendTeleMsg',)
        4560    CALL_FUNCTION_KW              3
        4562    POP_TOP                       
        4564    LOAD_NAME                     61: set_config_value
        4566    LOAD_CONST                    48: 'status'
        4568    LOAD_CONST                    49: 'algo_running_status'
        4570    LOAD_CONST                    122: '0'
        4572    CALL_FUNCTION                 3
        4574    POP_TOP                       
        4576    LOAD_NAME                     62: savedata
        4578    CALL_FUNCTION                 0
        4580    POP_TOP                       
        4582    LOAD_NAME                     59: iLog
        4584    LOAD_CONST                    267: ' Shutter down... Calling sys.exit() @ '
        4588    LOAD_NAME                     343: str
        4592    LOAD_GLOBAL                   76: read
        4594    CALL_FUNCTION                 1
        4596    BINARY_ADD                    
        4598    LOAD_CONST                    42: 4
        4600    LOAD_CONST                    20: True
        4602    LOAD_CONST                    43: ('sendTeleMsg',)
        4604    CALL_FUNCTION_KW              3
        4606    POP_TOP                       
        4608    LOAD_NAME                     0: sys
        4610    LOAD_METHOD                   344: exit
        4614    CALL_METHOD                   0
        4616    POP_TOP                       
        4618    LOAD_NAME                     47: login_token
        4620    LOAD_CONST                    0: 0
        4622    COMPARE_OP                    2 (==)
        4624    POP_JUMP_IF_FALSE             2321 (to 4642)
        4628    LOAD_NAME                     63: getAccessToken
        4630    LOAD_NAME                     35: INI_FILE
        4632    LOAD_CONST                    279: ('INI_FILE',)
        4636    CALL_FUNCTION_KW              1
        4638    STORE_NAME                    353: access_token
        4642    LOAD_NAME                     47: login_token
        4644    LOAD_CONST                    29: 1
        4646    COMPARE_OP                    2 (==)
        4648    POP_JUMP_IF_FALSE             2337 (to 4674)
        4652    LOAD_GLOBAL                   31: NULL + dropna
        4654    LOAD_METHOD                   354: set_common_token
        4658    CALL_METHOD                   0
        4660    STORE_NAME                    353: access_token
        4664    LOAD_NAME                     59: iLog
        4666    LOAD_NAME                     353: access_token
        4670    CALL_FUNCTION                 1
        4672    POP_TOP                       
        4674    LOAD_NAME                     2: time
        4676    LOAD_METHOD                   355: sleep
        4680    LOAD_CONST                    52: 2
        4682    CALL_METHOD                   1
        4684    POP_TOP                       
        4686    SETUP_FINALLY                 37 (to 4762)
        4688    LOAD_GLOBAL                   81: NULL + strAdminChatID
        4690    LOAD_CONST                    29: 1
        4692    COMPARE_OP                    2 (==)
        4694    POP_JUMP_IF_FALSE             2355 (to 4710)
        4698    BUILD_LIST                    0
        4700    LOAD_CONST                    280: ('NSE', '26000', 'Nifty 50')
        4704    LIST_EXTEND                   1
        4706    STORE_GLOBAL                  356: ins_Index
        4710    LOAD_GLOBAL                   83: NULL + strChatID
        4712    LOAD_CONST                    29: 1
        4714    COMPARE_OP                    2 (==)
        4716    POP_JUMP_IF_FALSE             2366 (to 4732)
        4720    BUILD_LIST                    0
        4722    LOAD_CONST                    281: ('NSE', '26037', 'Nifty Fin Services')
        4726    LIST_EXTEND                   1
        4728    STORE_GLOBAL                  356: ins_Index
        4732    LOAD_GLOBAL                   82: strChatID
        4734    LOAD_CONST                    29: 1
        4736    COMPARE_OP                    2 (==)
        4738    POP_JUMP_IF_FALSE             2379 (to 4758)
        4742    LOAD_NAME                     314: get_instrument_by_symbol
        4746    LOAD_CONST                    205: 'NSE'
        4748    LOAD_CONST                    282: 'Nifty Bank'
        4752    CALL_FUNCTION                 2
        4754    STORE_GLOBAL                  356: ins_Index
        4758    POP_BLOCK                     
        4760    JUMP_FORWARD                  62 (to 4886)
        4762    DUP_TOP                       
        4764    LOAD_NAME                     357: Exception
        4768    JUMP_IF_NOT_EXC_MATCH         2442 (to 4884)
        4772    POP_TOP                       
        4774    STORE_NAME                    358: ex
        4778    POP_TOP                       
        4780    SETUP_FINALLY                 45 (to 4872)
        4782    LOAD_NAME                     59: iLog
        4784    LOAD_CONST                    283: ' get_instrument_by_symbol: Exception='
        4788    LOAD_NAME                     343: str
        4792    LOAD_NAME                     358: ex
        4796    CALL_FUNCTION                 1
        4798    BINARY_ADD                    
        4800    LOAD_CONST                    271: 3
        4804    LOAD_CONST                    20: True
        4806    LOAD_CONST                    43: ('sendTeleMsg',)
        4808    CALL_FUNCTION_KW              3
        4810    POP_TOP                       
        4812    LOAD_NAME                     59: iLog
        4814    LOAD_CONST                    284: ' Exiting Algo'
        4818    LOAD_CONST                    42: 4
        4820    LOAD_CONST                    20: True
        4822    LOAD_CONST                    43: ('sendTeleMsg',)
        4824    CALL_FUNCTION_KW              3
        4826    POP_TOP                       
        4828    LOAD_NAME                     61: set_config_value
        4830    LOAD_CONST                    48: 'status'
        4832    LOAD_CONST                    49: 'algo_running_status'
        4834    LOAD_CONST                    122: '0'
        4836    CALL_FUNCTION                 3
        4838    POP_TOP                       
        4840    LOAD_NAME                     62: savedata
        4842    CALL_FUNCTION                 0
        4844    POP_TOP                       
        4846    LOAD_NAME                     0: sys
        4848    LOAD_METHOD                   344: exit
        4852    CALL_METHOD                   0
        4854    POP_TOP                       
        4856    POP_BLOCK                     
        4858    POP_EXCEPT                    
        4860    LOAD_CONST                    1: None
        4862    STORE_NAME                    358: ex
        4866    DELETE_NAME                   358: ex
        4870    JUMP_FORWARD                  7 (to 4886)
        4872    LOAD_CONST                    1: None
        4874    STORE_NAME                    358: ex
        4878    DELETE_NAME                   358: ex
        4882    RERAISE                       1
        4884    RERAISE                       0
        4886    LOAD_GLOBAL                   356: PE_SL_Triggered
        4890    STORE_GLOBAL                  359: instrument
        4894    LOAD_GLOBAL                   356: PE_SL_Triggered
        4898    STORE_GLOBAL                  360: ins_Index_ce
        4902    LOAD_GLOBAL                   356: PE_SL_Triggered
        4906    STORE_GLOBAL                  361: ins_Index_pe
        4910    LOAD_GLOBAL                   356: PE_SL_Triggered
        4914    STORE_NAME                    362: ins_Index_opt
        4918    LOAD_GLOBAL                   356: PE_SL_Triggered
        4922    STORE_GLOBAL                  363: ins_Index_ce_hedge
        4926    LOAD_GLOBAL                   356: PE_SL_Triggered
        4930    STORE_GLOBAL                  364: ins_Index_pe_hedge
        4934    LOAD_CONST                    285: ' Starting Websocket.'
        4938    STORE_NAME                    65: strMsg
        4940    LOAD_NAME                     59: iLog
        4942    LOAD_NAME                     65: strMsg
        4944    LOAD_CONST                    20: True
        4946    LOAD_CONST                    43: ('sendTeleMsg',)
        4948    CALL_FUNCTION_KW              2
        4950    POP_TOP                       
        4952    LOAD_GLOBAL                   31: NULL + dropna
        4954    LOAD_ATTR                     365: start_websocket
        4958    LOAD_NAME                     335: event_handler_order_update
        4962    LOAD_NAME                     336: event_handler_quote_update
        4966    LOAD_NAME                     337: open_callback
        4970    LOAD_CONST                    286: ('order_update_callback', 'subscribe_callback', 'socket_open_callback')
        4974    CALL_FUNCTION_KW              3
        4976    POP_TOP                       
        4978    LOAD_GLOBAL                   169: NULL + King_Candle_Min_SL
        4980    LOAD_CONST                    30: False
        4982    COMPARE_OP                    2 (==)
        4984    POP_JUMP_IF_FALSE             2500 (to 5000)
        4988    NOP                           
        4990    LOAD_GLOBAL                   169: NULL + King_Candle_Min_SL
        4992    LOAD_CONST                    30: False
        4994    COMPARE_OP                    2 (==)
        4996    POP_JUMP_IF_TRUE              2494 (to 4988)
        5000    LOAD_NAME                     2: time
        5002    LOAD_METHOD                   355: sleep
        5006    LOAD_CONST                    52: 2
        5008    CALL_METHOD                   1
        5010    POP_TOP                       
        5012    LOAD_NAME                     307: get_realtime_config
        5016    CALL_FUNCTION                 0
        5018    POP_TOP                       
        5020    LOAD_GLOBAL                   80: strAdminChatID
        5022    LOAD_CONST                    29: 1
        5024    COMPARE_OP                    2 (==)
        5026    POP_JUMP_IF_FALSE             2525 (to 5050)
        5030    LOAD_NAME                     61: set_config_value
        5032    LOAD_CONST                    55: 'algo'
        5034    LOAD_CONST                    287: 'ExitTradenow'
        5038    LOAD_CONST                    122: '0'
        5040    CALL_FUNCTION                 3
        5042    POP_TOP                       
        5044    LOAD_NAME                     62: savedata
        5046    CALL_FUNCTION                 0
        5048    POP_TOP                       
        5050    SETUP_FINALLY                 7 (to 5066)
        5052    LOAD_NAME                     331: get_option_tokens
        5056    LOAD_CONST                    246: 'ALL'
        5058    CALL_FUNCTION                 1
        5060    POP_TOP                       
        5062    POP_BLOCK                     
        5064    JUMP_FORWARD                  81 (to 5228)
        5066    POP_TOP                       
        5068    POP_TOP                       
        5070    POP_TOP                       
        5072    LOAD_NAME                     2: time
        5074    LOAD_METHOD                   355: sleep
        5078    LOAD_CONST                    288: 5
        5082    CALL_METHOD                   1
        5084    POP_TOP                       
        5086    SETUP_FINALLY                 7 (to 5102)
        5088    LOAD_NAME                     331: get_option_tokens
        5092    LOAD_CONST                    246: 'ALL'
        5094    CALL_FUNCTION                 1
        5096    POP_TOP                       
        5098    POP_BLOCK                     
        5100    JUMP_FORWARD                  62 (to 5226)
        5102    DUP_TOP                       
        5104    LOAD_NAME                     357: Exception
        5108    JUMP_IF_NOT_EXC_MATCH         2612 (to 5224)
        5112    POP_TOP                       
        5114    STORE_NAME                    358: ex
        5118    POP_TOP                       
        5120    SETUP_FINALLY                 45 (to 5212)
        5122    LOAD_NAME                     59: iLog
        5124    LOAD_CONST                    289: ' get_option_tokens(): Exception='
        5128    LOAD_NAME                     343: str
        5132    LOAD_NAME                     358: ex
        5136    CALL_FUNCTION                 1
        5138    BINARY_ADD                    
        5140    LOAD_CONST                    271: 3
        5144    LOAD_CONST                    20: True
        5146    LOAD_CONST                    43: ('sendTeleMsg',)
        5148    CALL_FUNCTION_KW              3
        5150    POP_TOP                       
        5152    LOAD_NAME                     59: iLog
        5154    LOAD_CONST                    284: ' Exiting Algo'
        5158    LOAD_CONST                    42: 4
        5160    LOAD_CONST                    20: True
        5162    LOAD_CONST                    43: ('sendTeleMsg',)
        5164    CALL_FUNCTION_KW              3
        5166    POP_TOP                       
        5168    LOAD_NAME                     61: set_config_value
        5170    LOAD_CONST                    48: 'status'
        5172    LOAD_CONST                    49: 'algo_running_status'
        5174    LOAD_CONST                    122: '0'
        5176    CALL_FUNCTION                 3
        5178    POP_TOP                       
        5180    LOAD_NAME                     62: savedata
        5182    CALL_FUNCTION                 0
        5184    POP_TOP                       
        5186    LOAD_NAME                     0: sys
        5188    LOAD_METHOD                   344: exit
        5192    CALL_METHOD                   0
        5194    POP_TOP                       
        5196    POP_BLOCK                     
        5198    POP_EXCEPT                    
        5200    LOAD_CONST                    1: None
        5202    STORE_NAME                    358: ex
        5206    DELETE_NAME                   358: ex
        5210    JUMP_FORWARD                  7 (to 5226)
        5212    LOAD_CONST                    1: None
        5214    STORE_NAME                    358: ex
        5218    DELETE_NAME                   358: ex
        5222    RERAISE                       1
        5224    RERAISE                       0
        5226    POP_EXCEPT                    
        5228    LOAD_NAME                     21: datetime
        5230    LOAD_ATTR                     347: date
        5234    LOAD_METHOD                   348: today
        5238    CALL_METHOD                   0
        5240    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        5244    COMPARE_OP                    3 (!=)
        5246    POP_JUMP_IF_FALSE             2627 (to 5254)
        5250    LOAD_GLOBAL                   96: strLogText
        5252    STORE_GLOBAL                  239: Perlot_MTM_SL
        5254    LOAD_NAME                     21: datetime
        5256    LOAD_ATTR                     347: date
        5260    LOAD_METHOD                   348: today
        5264    CALL_METHOD                   0
        5266    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        5270    COMPARE_OP                    2 (==)
        5272    POP_JUMP_IF_FALSE             2640 (to 5280)
        5276    LOAD_GLOBAL                   94: login_token
        5278    STORE_GLOBAL                  239: Perlot_MTM_SL
        5280    LOAD_NAME                     44: int
        5282    LOAD_GLOBAL                   366: CE_LTP_Update_Count
        5286    LOAD_GLOBAL                   79: NULL + get
        5288    BINARY_MULTIPLY               
        5290    CALL_FUNCTION                 1
        5292    STORE_GLOBAL                  367: Index_qty
        5296    LOAD_CONST                    290: ' Waiting for First Short Straddle time'
        5300    STORE_NAME                    65: strMsg
        5302    LOAD_NAME                     59: iLog
        5304    LOAD_NAME                     65: strMsg
        5306    LOAD_CONST                    29: 1
        5308    LOAD_CONST                    20: True
        5310    LOAD_CONST                    43: ('sendTeleMsg',)
        5312    CALL_FUNCTION_KW              3
        5314    POP_TOP                       
        5316    NOP                           
        5318    LOAD_NAME                     307: get_realtime_config
        5322    CALL_FUNCTION                 0
        5324    POP_TOP                       
        5326    LOAD_GLOBAL                   78: get
        5328    LOAD_CONST                    29: 1
        5330    COMPARE_OP                    2 (==)
        5332    POP_JUMP_IF_FALSE             2670 (to 5340)
        5336    LOAD_CONST                    30: False
        5338    STORE_GLOBAL                  73: place_orders
        5340    LOAD_NAME                     21: datetime
        5342    LOAD_ATTR                     347: date
        5346    LOAD_METHOD                   348: today
        5350    CALL_METHOD                   0
        5352    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        5356    COMPARE_OP                    3 (!=)
        5358    POP_JUMP_IF_FALSE             2699 (to 5398)
        5362    LOAD_GLOBAL                   97: NULL + strLogText
        5364    STORE_GLOBAL                  240: Perlot_MTM_Target
        5366    LOAD_GLOBAL                   100: format
        5368    STORE_GLOBAL                  241: StikeAdj_SLPer
        5370    LOAD_GLOBAL                   101: NULL + format
        5372    STORE_GLOBAL                  242: StikeAdj_TgtPer
        5374    LOAD_GLOBAL                   115: NULL + stdout
        5376    STORE_GLOBAL                  244: Perlot_MTM_lock_profit
        5378    LOAD_GLOBAL                   116: stderr
        5380    STORE_GLOBAL                  245: Perlot_MTM_Trailing
        5382    LOAD_GLOBAL                   114: stdout
        5384    STORE_GLOBAL                  243: Perlot_MTM_lock_profit_threshold
        5386    LOAD_GLOBAL                   128: __file__
        5388    STORE_GLOBAL                  247: Synthetic_Fut
        5390    LOAD_GLOBAL                   129: NULL + __file__
        5392    STORE_GLOBAL                  248: Single_Leg_Adj
        5394    LOAD_GLOBAL                   130: strMsg
        5396    STORE_GLOBAL                  249: Single_Leg_Adj_Delta_PCT
        5398    LOAD_NAME                     21: datetime
        5400    LOAD_ATTR                     347: date
        5404    LOAD_METHOD                   348: today
        5408    CALL_METHOD                   0
        5410    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        5414    COMPARE_OP                    2 (==)
        5416    POP_JUMP_IF_FALSE             2728 (to 5456)
        5420    LOAD_GLOBAL                   95: NULL + login_token
        5422    STORE_GLOBAL                  240: Perlot_MTM_Target
        5424    LOAD_GLOBAL                   98: print
        5426    STORE_GLOBAL                  241: StikeAdj_SLPer
        5428    LOAD_GLOBAL                   99: NULL + print
        5430    STORE_GLOBAL                  242: StikeAdj_TgtPer
        5432    LOAD_GLOBAL                   118: iLog
        5434    STORE_GLOBAL                  244: Perlot_MTM_lock_profit
        5436    LOAD_GLOBAL                   119: NULL + iLog
        5438    STORE_GLOBAL                  245: Perlot_MTM_Trailing
        5440    LOAD_GLOBAL                   117: NULL + stderr
        5442    STORE_GLOBAL                  243: Perlot_MTM_lock_profit_threshold
        5444    LOAD_GLOBAL                   131: NULL + strMsg
        5446    STORE_GLOBAL                  247: Synthetic_Fut
        5448    LOAD_GLOBAL                   132: f
        5450    STORE_GLOBAL                  248: Single_Leg_Adj
        5452    LOAD_GLOBAL                   133: NULL + f
        5454    STORE_GLOBAL                  249: Single_Leg_Adj_Delta_PCT
        5456    LOAD_NAME                     21: datetime
        5458    LOAD_ATTR                     347: date
        5462    LOAD_METHOD                   348: today
        5466    CALL_METHOD                   0
        5468    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        5472    COMPARE_OP                    3 (!=)
        5474    POP_JUMP_IF_FALSE             2746 (to 5492)
        5478    LOAD_GLOBAL                   113: NULL + open
        5480    LOAD_CONST                    0: 0
        5482    COMPARE_OP                    2 (==)
        5484    POP_JUMP_IF_FALSE             2746 (to 5492)
        5488    LOAD_GLOBAL                   96: strLogText
        5490    STORE_GLOBAL                  239: Perlot_MTM_SL
        5492    LOAD_NAME                     21: datetime
        5494    LOAD_ATTR                     347: date
        5498    LOAD_METHOD                   348: today
        5502    CALL_METHOD                   0
        5504    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        5508    COMPARE_OP                    2 (==)
        5510    POP_JUMP_IF_FALSE             2764 (to 5528)
        5514    LOAD_GLOBAL                   113: NULL + open
        5516    LOAD_CONST                    0: 0
        5518    COMPARE_OP                    2 (==)
        5520    POP_JUMP_IF_FALSE             2764 (to 5528)
        5524    LOAD_GLOBAL                   94: login_token
        5526    STORE_GLOBAL                  239: Perlot_MTM_SL
        5528    LOAD_NAME                     44: int
        5530    LOAD_NAME                     21: datetime
        5532    LOAD_ATTR                     21: datetime
        5534    LOAD_METHOD                   51: now
        5536    CALL_METHOD                   0
        5538    LOAD_METHOD                   52: strftime
        5540    LOAD_CONST                    50: '%H%M'
        5542    CALL_METHOD                   1
        5544    CALL_FUNCTION                 1
        5546    STORE_GLOBAL                  76: cur_HHMM
        5548    LOAD_NAME                     44: int
        5550    LOAD_NAME                     21: datetime
        5552    LOAD_ATTR                     21: datetime
        5554    LOAD_METHOD                   51: now
        5556    CALL_METHOD                   0
        5558    LOAD_METHOD                   52: strftime
        5560    LOAD_CONST                    291: '%H%M%S'
        5564    CALL_METHOD                   1
        5566    CALL_FUNCTION                 1
        5568    STORE_GLOBAL                  368: cur_HHMMSS
        5572    LOAD_GLOBAL                   368: PE_LTP_Update_Count
        5576    LOAD_GLOBAL                   87: NULL + strBotTokenWObot
        5578    COMPARE_OP                    5 (>=)
        5580    POP_JUMP_IF_FALSE             4820 (to 9640)
        5584    LOAD_GLOBAL                   170: King_Candle_Max_SL
        5586    LOAD_CONST                    30: False
        5588    COMPARE_OP                    2 (==)
        5590    POP_JUMP_IF_FALSE             4820 (to 9640)
        5594    LOAD_GLOBAL                   139: NULL + cred
        5596    LOAD_CONST                    29: 1
        5598    COMPARE_OP                    2 (==)
        5600    POP_JUMP_IF_FALSE             3128 (to 6256)
        5604    LOAD_NAME                     369: len
        5608    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        5610    CALL_FUNCTION                 1
        5612    LOAD_CONST                    0: 0
        5614    COMPARE_OP                    4 (>)
        5616    POP_JUMP_IF_FALSE             3128 (to 6256)
        5620    LOAD_NAME                     44: int
        5622    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        5624    LOAD_CONST                    292: -1
        5628    BINARY_SUBSCR                 
        5630    CALL_FUNCTION                 1
        5632    STORE_NAME                    187: Starting_LTP
        5634    LOAD_CONST                    293: ' Wait_for_movement enabled. Short straddle will be triggered when LTP '
        5638    LOAD_NAME                     44: int
        5640    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        5642    LOAD_CONST                    292: -1
        5646    BINARY_SUBSCR                 
        5648    CALL_FUNCTION                 1
        5650    FORMAT_VALUE                  0
        5652    LOAD_CONST                    294: ' move '
        5656    LOAD_GLOBAL                   140: susr
        5658    FORMAT_VALUE                  0
        5660    LOAD_CONST                    295: ' UP or '
        5664    LOAD_GLOBAL                   141: NULL + susr
        5666    FORMAT_VALUE                  0
        5668    LOAD_CONST                    296: ' down points before '
        5672    LOAD_GLOBAL                   142: spassword
        5674    FORMAT_VALUE                  0
        5676    LOAD_CONST                    297: ' Hrs'
        5680    BUILD_STRING                  9
        5682    STORE_NAME                    65: strMsg
        5684    LOAD_NAME                     59: iLog
        5686    LOAD_NAME                     65: strMsg
        5688    LOAD_CONST                    59: 6
        5690    LOAD_CONST                    20: True
        5692    LOAD_CONST                    43: ('sendTeleMsg',)
        5694    CALL_FUNCTION_KW              3
        5696    POP_TOP                       
        5698    LOAD_CONST                    30: False
        5700    STORE_NAME                    370: Wait_Entry_triggered
        5704    LOAD_NAME                     370: Wait_Entry_triggered
        5708    LOAD_CONST                    30: False
        5710    COMPARE_OP                    2 (==)
        5712    POP_JUMP_IF_FALSE             3128 (to 6256)
        5716    LOAD_NAME                     44: int
        5718    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        5720    LOAD_CONST                    292: -1
        5724    BINARY_SUBSCR                 
        5726    CALL_FUNCTION                 1
        5728    LOAD_NAME                     187: Starting_LTP
        5730    BINARY_SUBTRACT               
        5732    LOAD_GLOBAL                   140: susr
        5734    COMPARE_OP                    0 (<)
        5736    POP_JUMP_IF_FALSE             3128 (to 6256)
        5740    LOAD_NAME                     187: Starting_LTP
        5742    LOAD_NAME                     44: int
        5744    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        5746    LOAD_CONST                    292: -1
        5750    BINARY_SUBSCR                 
        5752    CALL_FUNCTION                 1
        5754    BINARY_SUBTRACT               
        5756    LOAD_GLOBAL                   141: NULL + susr
        5758    COMPARE_OP                    0 (<)
        5760    POP_JUMP_IF_FALSE             3128 (to 6256)
        5764    LOAD_GLOBAL                   139: NULL + cred
        5766    LOAD_CONST                    29: 1
        5768    COMPARE_OP                    2 (==)
        5770    POP_JUMP_IF_FALSE             3128 (to 6256)
        5774    LOAD_NAME                     307: get_realtime_config
        5778    CALL_FUNCTION                 0
        5780    POP_TOP                       
        5782    LOAD_NAME                     44: int
        5784    LOAD_NAME                     21: datetime
        5786    LOAD_ATTR                     21: datetime
        5788    LOAD_METHOD                   51: now
        5790    CALL_METHOD                   0
        5792    LOAD_METHOD                   52: strftime
        5794    LOAD_CONST                    50: '%H%M'
        5796    CALL_METHOD                   1
        5798    CALL_FUNCTION                 1
        5800    STORE_GLOBAL                  76: cur_HHMM
        5802    LOAD_GLOBAL                   76: read
        5804    LOAD_GLOBAL                   142: spassword
        5806    COMPARE_OP                    5 (>=)
        5808    POP_JUMP_IF_FALSE             2938 (to 5876)
        5812    LOAD_GLOBAL                   170: King_Candle_Max_SL
        5814    LOAD_CONST                    30: False
        5816    COMPARE_OP                    2 (==)
        5818    POP_JUMP_IF_FALSE             2938 (to 5876)
        5822    LOAD_GLOBAL                   143: NULL + spassword
        5824    LOAD_CONST                    29: 1
        5826    COMPARE_OP                    2 (==)
        5828    POP_JUMP_IF_FALSE             2938 (to 5876)
        5832    LOAD_NAME                     59: iLog
        5834    LOAD_CONST                    298: ' Max Entry time exceeded. Exiting Algo'
        5838    LOAD_CONST                    42: 4
        5840    LOAD_CONST                    20: True
        5842    LOAD_CONST                    43: ('sendTeleMsg',)
        5844    CALL_FUNCTION_KW              3
        5846    POP_TOP                       
        5848    LOAD_NAME                     61: set_config_value
        5850    LOAD_CONST                    48: 'status'
        5852    LOAD_CONST                    49: 'algo_running_status'
        5854    LOAD_CONST                    122: '0'
        5856    CALL_FUNCTION                 3
        5858    POP_TOP                       
        5860    LOAD_NAME                     62: savedata
        5862    CALL_FUNCTION                 0
        5864    POP_TOP                       
        5866    LOAD_NAME                     0: sys
        5868    LOAD_METHOD                   344: exit
        5872    CALL_METHOD                   0
        5874    POP_TOP                       
        5876    LOAD_GLOBAL                   76: read
        5878    LOAD_GLOBAL                   142: spassword
        5880    COMPARE_OP                    5 (>=)
        5882    POP_JUMP_IF_FALSE             2964 (to 5928)
        5886    LOAD_GLOBAL                   170: King_Candle_Max_SL
        5888    LOAD_CONST                    30: False
        5890    COMPARE_OP                    2 (==)
        5892    POP_JUMP_IF_FALSE             2964 (to 5928)
        5896    LOAD_GLOBAL                   143: NULL + spassword
        5898    LOAD_CONST                    0: 0
        5900    COMPARE_OP                    2 (==)
        5902    POP_JUMP_IF_FALSE             2964 (to 5928)
        5906    LOAD_NAME                     59: iLog
        5908    LOAD_CONST                    299: ' Max Entry time Reached. Skipping wait for movement'
        5912    LOAD_CONST                    52: 2
        5914    LOAD_CONST                    20: True
        5916    LOAD_CONST                    43: ('sendTeleMsg',)
        5918    CALL_FUNCTION_KW              3
        5920    POP_TOP                       
        5922    LOAD_CONST                    20: True
        5924    STORE_NAME                    370: Wait_Entry_triggered
        5928    LOAD_NAME                     307: get_realtime_config
        5932    CALL_FUNCTION                 0
        5934    POP_TOP                       
        5936    LOAD_NAME                     44: int
        5938    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        5940    LOAD_CONST                    292: -1
        5944    BINARY_SUBSCR                 
        5946    CALL_FUNCTION                 1
        5948    STORE_NAME                    371: IndexLTP
        5952    LOAD_NAME                     21: datetime
        5954    LOAD_ATTR                     21: datetime
        5956    LOAD_METHOD                   51: now
        5958    CALL_METHOD                   0
        5960    LOAD_ATTR                     372: minute
        5964    STORE_NAME                    207: cur_min
        5966    LOAD_NAME                     207: cur_min
        5968    LOAD_GLOBAL                   159: NULL + no_of_lots
        5970    BINARY_MODULO                 
        5972    LOAD_CONST                    0: 0
        5974    COMPARE_OP                    2 (==)
        5976    POP_JUMP_IF_FALSE             3056 (to 6112)
        5980    LOAD_NAME                     210: log_min
        5982    LOAD_NAME                     207: cur_min
        5984    COMPARE_OP                    3 (!=)
        5986    POP_JUMP_IF_FALSE             3056 (to 6112)
        5990    LOAD_GLOBAL                   160: ExitTradenow
        5992    LOAD_CONST                    0: 0
        5994    COMPARE_OP                    2 (==)
        5996    POP_JUMP_IF_FALSE             3056 (to 6112)
        6000    LOAD_NAME                     207: cur_min
        6002    STORE_NAME                    210: log_min
        6004    LOAD_NAME                     2: time
        6006    LOAD_METHOD                   2: time
        6008    CALL_METHOD                   0
        6010    STORE_NAME                    373: t1
        6014    LOAD_CONST                    300: ' Current LTP : '
        6018    LOAD_NAME                     371: IndexLTP
        6022    FORMAT_VALUE                  0
        6024    LOAD_CONST                    301: ', Starting LTP : '
        6028    LOAD_NAME                     187: Starting_LTP
        6030    FORMAT_VALUE                  0
        6032    LOAD_CONST                    302: ', Pos Difference (Cur,Req) : ('
        6036    LOAD_NAME                     44: int
        6038    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6040    LOAD_CONST                    292: -1
        6044    BINARY_SUBSCR                 
        6046    CALL_FUNCTION                 1
        6048    LOAD_NAME                     187: Starting_LTP
        6050    BINARY_SUBTRACT               
        6052    FORMAT_VALUE                  0
        6054    LOAD_CONST                    303: ','
        6058    LOAD_GLOBAL                   140: susr
        6060    FORMAT_VALUE                  0
        6062    LOAD_CONST                    304: '), Neg Difference (Cur,Req) : ('
        6066    LOAD_NAME                     187: Starting_LTP
        6068    LOAD_NAME                     44: int
        6070    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6072    LOAD_CONST                    292: -1
        6076    BINARY_SUBSCR                 
        6078    CALL_FUNCTION                 1
        6080    BINARY_SUBTRACT               
        6082    FORMAT_VALUE                  0
        6084    LOAD_CONST                    303: ','
        6088    LOAD_GLOBAL                   141: NULL + susr
        6090    FORMAT_VALUE                  0
        6092    LOAD_CONST                    305: ')'
        6096    BUILD_STRING                  13
        6098    STORE_NAME                    65: strMsg
        6100    LOAD_NAME                     59: iLog
        6102    LOAD_NAME                     65: strMsg
        6104    LOAD_CONST                    30: False
        6106    LOAD_CONST                    43: ('sendTeleMsg',)
        6108    CALL_FUNCTION_KW              2
        6110    POP_TOP                       
        6112    LOAD_NAME                     370: Wait_Entry_triggered
        6116    LOAD_CONST                    30: False
        6118    COMPARE_OP                    2 (==)
        6120    POP_JUMP_IF_FALSE             3093 (to 6186)
        6124    LOAD_NAME                     44: int
        6126    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6128    LOAD_CONST                    292: -1
        6132    BINARY_SUBSCR                 
        6134    CALL_FUNCTION                 1
        6136    LOAD_NAME                     187: Starting_LTP
        6138    BINARY_SUBTRACT               
        6140    LOAD_GLOBAL                   140: susr
        6142    COMPARE_OP                    0 (<)
        6144    POP_JUMP_IF_FALSE             3093 (to 6186)
        6148    LOAD_NAME                     187: Starting_LTP
        6150    LOAD_NAME                     44: int
        6152    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6154    LOAD_CONST                    292: -1
        6158    BINARY_SUBSCR                 
        6160    CALL_FUNCTION                 1
        6162    BINARY_SUBTRACT               
        6164    LOAD_GLOBAL                   141: NULL + susr
        6166    COMPARE_OP                    0 (<)
        6168    POP_JUMP_IF_FALSE             3093 (to 6186)
        6172    LOAD_NAME                     2: time
        6174    LOAD_METHOD                   355: sleep
        6178    LOAD_CONST                    288: 5
        6182    CALL_METHOD                   1
        6184    POP_TOP                       
        6186    LOAD_NAME                     370: Wait_Entry_triggered
        6190    LOAD_CONST                    30: False
        6192    COMPARE_OP                    2 (==)
        6194    POP_JUMP_IF_FALSE             3128 (to 6256)
        6198    LOAD_NAME                     44: int
        6200    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6202    LOAD_CONST                    292: -1
        6206    BINARY_SUBSCR                 
        6208    CALL_FUNCTION                 1
        6210    LOAD_NAME                     187: Starting_LTP
        6212    BINARY_SUBTRACT               
        6214    LOAD_GLOBAL                   140: susr
        6216    COMPARE_OP                    0 (<)
        6218    POP_JUMP_IF_FALSE             3128 (to 6256)
        6222    LOAD_NAME                     187: Starting_LTP
        6224    LOAD_NAME                     44: int
        6226    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6228    LOAD_CONST                    292: -1
        6232    BINARY_SUBSCR                 
        6234    CALL_FUNCTION                 1
        6236    BINARY_SUBTRACT               
        6238    LOAD_GLOBAL                   141: NULL + susr
        6240    COMPARE_OP                    0 (<)
        6242    POP_JUMP_IF_FALSE             3128 (to 6256)
        6246    LOAD_GLOBAL                   139: NULL + cred
        6248    LOAD_CONST                    29: 1
        6250    COMPARE_OP                    2 (==)
        6252    POP_JUMP_IF_TRUE              2887 (to 5774)
        6256    LOAD_GLOBAL                   137: NULL + FullLoader
        6258    LOAD_CONST                    29: 1
        6260    COMPARE_OP                    2 (==)
        6262    POP_JUMP_IF_FALSE             3280 (to 6560)
        6266    LOAD_NAME                     369: len
        6270    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6272    CALL_FUNCTION                 1
        6274    LOAD_CONST                    0: 0
        6276    COMPARE_OP                    4 (>)
        6278    POP_JUMP_IF_FALSE             3280 (to 6560)
        6282    LOAD_CONST                    306: ' Wait for premium enabled. Short straddle will be triggered when LTP current difference '
        6286    LOAD_NAME                     44: int
        6288    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6290    LOAD_CONST                    292: -1
        6294    BINARY_SUBSCR                 
        6296    CALL_FUNCTION                 1
        6298    FORMAT_VALUE                  0
        6300    LOAD_CONST                    307: ' is close to ATM strike by '
        6304    LOAD_GLOBAL                   138: cred
        6306    FORMAT_VALUE                  0
        6308    BUILD_STRING                  4
        6310    STORE_NAME                    65: strMsg
        6312    LOAD_NAME                     59: iLog
        6314    LOAD_NAME                     65: strMsg
        6316    LOAD_CONST                    59: 6
        6318    LOAD_CONST                    20: True
        6320    LOAD_CONST                    43: ('sendTeleMsg',)
        6322    CALL_FUNCTION_KW              3
        6324    POP_TOP                       
        6326    LOAD_GLOBAL                   188: expiry_Perlot_MTM_SL
        6328    LOAD_GLOBAL                   138: cred
        6330    COMPARE_OP                    4 (>)
        6332    POP_JUMP_IF_FALSE             3280 (to 6560)
        6336    LOAD_GLOBAL                   137: NULL + FullLoader
        6338    LOAD_CONST                    29: 1
        6340    COMPARE_OP                    2 (==)
        6342    POP_JUMP_IF_FALSE             3280 (to 6560)
        6346    LOAD_NAME                     307: get_realtime_config
        6350    CALL_FUNCTION                 0
        6352    POP_TOP                       
        6354    LOAD_NAME                     44: int
        6356    LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        6358    LOAD_CONST                    292: -1
        6362    BINARY_SUBSCR                 
        6364    CALL_FUNCTION                 1
        6366    STORE_NAME                    371: IndexLTP
        6370    LOAD_CONST                    300: ' Current LTP : '
        6374    LOAD_NAME                     371: IndexLTP
        6378    FORMAT_VALUE                  0
        6380    LOAD_CONST                    308: ' Required Premium difference : '
        6384    LOAD_GLOBAL                   138: cred
        6386    FORMAT_VALUE                  0
        6388    BUILD_STRING                  4
        6390    STORE_NAME                    65: strMsg
        6392    LOAD_NAME                     59: iLog
        6394    LOAD_NAME                     65: strMsg
        6396    LOAD_CONST                    30: False
        6398    LOAD_CONST                    43: ('sendTeleMsg',)
        6400    CALL_FUNCTION_KW              2
        6402    POP_TOP                       
        6404    LOAD_GLOBAL                   81: NULL + strAdminChatID
        6406    LOAD_CONST                    29: 1
        6408    COMPARE_OP                    2 (==)
        6410    POP_JUMP_IF_TRUE              3212 (to 6424)
        6414    LOAD_GLOBAL                   83: NULL + strChatID
        6416    LOAD_CONST                    29: 1
        6418    COMPARE_OP                    2 (==)
        6420    POP_JUMP_IF_FALSE             3228 (to 6456)
        6424    LOAD_NAME                     44: int
        6426    LOAD_CONST                    169: 50
        6428    LOAD_NAME                     374: round
        6432    LOAD_NAME                     44: int
        6434    LOAD_NAME                     371: IndexLTP
        6438    CALL_FUNCTION                 1
        6440    LOAD_CONST                    169: 50
        6442    BINARY_TRUE_DIVIDE            
        6444    LOAD_CONST                    0: 0
        6446    CALL_FUNCTION                 2
        6448    BINARY_MULTIPLY               
        6450    CALL_FUNCTION                 1
        6452    STORE_GLOBAL                  260: Index_CE_atm
        6456    LOAD_GLOBAL                   82: strChatID
        6458    LOAD_CONST                    29: 1
        6460    COMPARE_OP                    2 (==)
        6462    POP_JUMP_IF_FALSE             3249 (to 6498)
        6466    LOAD_NAME                     44: int
        6468    LOAD_CONST                    73: 100
        6470    LOAD_NAME                     374: round
        6474    LOAD_NAME                     44: int
        6476    LOAD_NAME                     371: IndexLTP
        6480    CALL_FUNCTION                 1
        6482    LOAD_CONST                    73: 100
        6484    BINARY_TRUE_DIVIDE            
        6486    LOAD_CONST                    0: 0
        6488    CALL_FUNCTION                 2
        6490    BINARY_MULTIPLY               
        6492    CALL_FUNCTION                 1
        6494    STORE_GLOBAL                  260: Index_CE_atm
        6498    LOAD_NAME                     375: abs
        6502    LOAD_NAME                     371: IndexLTP
        6506    LOAD_GLOBAL                   260: normal_Single_Leg_Adj_Delta_PCT
        6510    BINARY_SUBTRACT               
        6512    CALL_FUNCTION                 1
        6514    STORE_GLOBAL                  188: current_premium_delta
        6516    LOAD_GLOBAL                   188: expiry_Perlot_MTM_SL
        6518    LOAD_GLOBAL                   138: cred
        6520    COMPARE_OP                    4 (>)
        6522    POP_JUMP_IF_FALSE             3270 (to 6540)
        6526    LOAD_NAME                     2: time
        6528    LOAD_METHOD                   355: sleep
        6532    LOAD_CONST                    288: 5
        6536    CALL_METHOD                   1
        6538    POP_TOP                       
        6540    LOAD_GLOBAL                   188: expiry_Perlot_MTM_SL
        6542    LOAD_GLOBAL                   138: cred
        6544    COMPARE_OP                    4 (>)
        6546    POP_JUMP_IF_FALSE             3280 (to 6560)
        6550    LOAD_GLOBAL                   137: NULL + FullLoader
        6552    LOAD_CONST                    29: 1
        6554    COMPARE_OP                    2 (==)
        6556    POP_JUMP_IF_TRUE              3173 (to 6346)
        6560    SETUP_FINALLY                 7 (to 6576)
        6562    LOAD_NAME                     331: get_option_tokens
        6566    LOAD_CONST                    246: 'ALL'
        6568    CALL_FUNCTION                 1
        6570    POP_TOP                       
        6572    POP_BLOCK                     
        6574    JUMP_FORWARD                  72 (to 6720)
        6576    POP_TOP                       
        6578    POP_TOP                       
        6580    POP_TOP                       
        6582    LOAD_NAME                     2: time
        6584    LOAD_METHOD                   355: sleep
        6588    LOAD_CONST                    288: 5
        6592    CALL_METHOD                   1
        6594    POP_TOP                       
        6596    SETUP_FINALLY                 7 (to 6612)
        6598    LOAD_NAME                     331: get_option_tokens
        6602    LOAD_CONST                    246: 'ALL'
        6604    CALL_FUNCTION                 1
        6606    POP_TOP                       
        6608    POP_BLOCK                     
        6610    JUMP_FORWARD                  53 (to 6718)
        6612    DUP_TOP                       
        6614    LOAD_NAME                     357: Exception
        6618    JUMP_IF_NOT_EXC_MATCH         3358 (to 6716)
        6622    POP_TOP                       
        6624    STORE_NAME                    358: ex
        6628    POP_TOP                       
        6630    SETUP_FINALLY                 36 (to 6704)
        6632    LOAD_NAME                     59: iLog
        6634    LOAD_CONST                    289: ' get_option_tokens(): Exception='
        6638    LOAD_NAME                     343: str
        6642    LOAD_NAME                     358: ex
        6646    CALL_FUNCTION                 1
        6648    BINARY_ADD                    
        6650    LOAD_CONST                    271: 3
        6654    LOAD_CONST                    20: True
        6656    LOAD_CONST                    43: ('sendTeleMsg',)
        6658    CALL_FUNCTION_KW              3
        6660    POP_TOP                       
        6662    LOAD_NAME                     59: iLog
        6664    LOAD_CONST                    284: ' Exiting Algo'
        6668    LOAD_CONST                    42: 4
        6670    LOAD_CONST                    20: True
        6672    LOAD_CONST                    43: ('sendTeleMsg',)
        6674    CALL_FUNCTION_KW              3
        6676    POP_TOP                       
        6678    LOAD_NAME                     0: sys
        6680    LOAD_METHOD                   344: exit
        6684    CALL_METHOD                   0
        6686    POP_TOP                       
        6688    POP_BLOCK                     
        6690    POP_EXCEPT                    
        6692    LOAD_CONST                    1: None
        6694    STORE_NAME                    358: ex
        6698    DELETE_NAME                   358: ex
        6702    JUMP_FORWARD                  7 (to 6718)
        6704    LOAD_CONST                    1: None
        6706    STORE_NAME                    358: ex
        6710    DELETE_NAME                   358: ex
        6714    RERAISE                       1
        6716    RERAISE                       0
        6718    POP_EXCEPT                    
        6720    LOAD_CONST                    309: ' Starting tick processing.'
        6724    STORE_NAME                    65: strMsg
        6726    LOAD_NAME                     59: iLog
        6728    LOAD_NAME                     65: strMsg
        6730    LOAD_CONST                    20: True
        6732    LOAD_CONST                    43: ('sendTeleMsg',)
        6734    CALL_FUNCTION_KW              2
        6736    POP_TOP                       
        6738    LOAD_GLOBAL                   78: get
        6740    LOAD_CONST                    29: 1
        6742    COMPARE_OP                    2 (==)
        6744    POP_JUMP_IF_FALSE             3693 (to 7386)
        6748    LOAD_CONST                    310: 'BANK'
        6752    STORE_NAME                    376: Symbol
        6756    LOAD_GLOBAL                   144: tl
        6758    LOAD_CONST                    29: 1
        6760    COMPARE_OP                    2 (==)
        6762    POP_JUMP_IF_FALSE             3539 (to 7078)
        6766    LOAD_GLOBAL                   266: expiry_Single_Leg_Adj_Delta_PCT
        6770    STORE_GLOBAL                  224: Last_Traded_CE_Price_hedge
        6772    LOAD_GLOBAL                   267: NULL + expiry_Single_Leg_Adj_Delta_PCT
        6776    STORE_GLOBAL                  223: Last_Traded_PE_Price_hedge
        6778    LOAD_CONST                    311: ' Place Hedge order for Short Straddle for CE/PE Strike=('
        6782    LOAD_GLOBAL                   377: NULL + current_premium_delta
        6786    FORMAT_VALUE                  0
        6788    LOAD_CONST                    303: ','
        6792    LOAD_GLOBAL                   378: Usr_Lic
        6796    FORMAT_VALUE                  0
        6798    LOAD_CONST                    312: '), ATM(CE,PE)=('
        6802    LOAD_GLOBAL                   224: entry_price_buffer
        6804    FORMAT_VALUE                  0
        6806    LOAD_CONST                    313: ', '
        6810    LOAD_GLOBAL                   223: NULL + entry_price
        6812    FORMAT_VALUE                  0
        6814    LOAD_CONST                    314: ') '
        6818    BUILD_STRING                  9
        6820    STORE_NAME                    65: strMsg
        6822    LOAD_GLOBAL                   74: cfg
        6824    LOAD_CONST                    52: 2
        6826    BINARY_ADD                    
        6828    STORE_GLOBAL                  74: order_count
        6830    LOAD_NAME                     59: iLog
        6832    LOAD_NAME                     65: strMsg
        6834    LOAD_CONST                    288: 5
        6838    LOAD_CONST                    20: True
        6840    LOAD_CONST                    43: ('sendTeleMsg',)
        6842    CALL_FUNCTION_KW              3
        6844    POP_TOP                       
        6846    LOAD_GLOBAL                   76: read
        6848    LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        6852    LOAD_CONST                    0: 0
        6854    BINARY_SUBSCR                 
        6856    LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        6860    LOAD_CONST                    29: 1
        6862    BINARY_SUBSCR                 
        6864    LOAD_CONST                    29: 1
        6866    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        6870    BINARY_MULTIPLY               
        6872    BUILD_LIST                    4
        6874    LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        6876    LOAD_ATTR                     379: loc
        6880    LOAD_CONST                    0: 0
        6882    LOAD_NAME                     197: leg_cols
        6884    BUILD_TUPLE                   2
        6886    STORE_SUBSCR                  
        6888    LOAD_GLOBAL                   76: read
        6890    LOAD_GLOBAL                   364: partial_profit_booked
        6894    LOAD_CONST                    0: 0
        6896    BINARY_SUBSCR                 
        6898    LOAD_GLOBAL                   364: partial_profit_booked
        6902    LOAD_CONST                    29: 1
        6904    BINARY_SUBSCR                 
        6906    LOAD_CONST                    29: 1
        6908    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        6912    BINARY_MULTIPLY               
        6914    BUILD_LIST                    4
        6916    LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        6918    LOAD_ATTR                     379: loc
        6922    LOAD_CONST                    0: 0
        6924    LOAD_NAME                     197: leg_cols
        6926    BUILD_TUPLE                   2
        6928    STORE_SUBSCR                  
        6930    LOAD_NAME                     24: pd
        6932    LOAD_METHOD                   380: concat
        6936    LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        6938    LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        6940    BUILD_LIST                    2
        6942    CALL_METHOD                   1
        6944    STORE_GLOBAL                  203: Current_legs_hedge
        6946    LOAD_GLOBAL                   76: read
        6948    LOAD_NAME                     376: Symbol
        6952    LOAD_GLOBAL                   377: NULL + current_premium_delta
        6956    LOAD_CONST                    315: 'CE'
        6960    LOAD_CONST                    29: 1
        6962    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        6966    LOAD_GLOBAL                   224: entry_price_buffer
        6968    LOAD_CONST                    292: -1
        6972    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        6976    BINARY_MULTIPLY               
        6978    LOAD_GLOBAL                   224: entry_price_buffer
        6980    BINARY_MULTIPLY               
        6982    BUILD_LIST                    8
        6984    LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        6986    LOAD_ATTR                     379: loc
        6990    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        6992    LOAD_NAME                     191: df_cols
        6994    BUILD_TUPLE                   2
        6996    STORE_SUBSCR                  
        6998    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7000    LOAD_CONST                    29: 1
        7002    BINARY_ADD                    
        7004    STORE_GLOBAL                  190: df_king_cnt
        7006    LOAD_GLOBAL                   76: read
        7008    LOAD_NAME                     376: Symbol
        7012    LOAD_GLOBAL                   378: Usr_Lic
        7016    LOAD_CONST                    316: 'PE'
        7020    LOAD_CONST                    29: 1
        7022    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7026    LOAD_GLOBAL                   223: NULL + entry_price
        7028    LOAD_CONST                    292: -1
        7032    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7036    BINARY_MULTIPLY               
        7038    LOAD_GLOBAL                   223: NULL + entry_price
        7040    BINARY_MULTIPLY               
        7042    BUILD_LIST                    8
        7044    LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        7046    LOAD_ATTR                     379: loc
        7050    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7052    LOAD_NAME                     191: df_cols
        7054    BUILD_TUPLE                   2
        7056    STORE_SUBSCR                  
        7058    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7060    LOAD_CONST                    29: 1
        7062    BINARY_ADD                    
        7064    STORE_GLOBAL                  190: df_king_cnt
        7066    LOAD_NAME                     2: time
        7068    LOAD_METHOD                   355: sleep
        7072    LOAD_CONST                    52: 2
        7074    CALL_METHOD                   1
        7076    POP_TOP                       
        7078    LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        7082    STORE_GLOBAL                  222: Last_Traded_CE_Price
        7084    LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        7088    STORE_GLOBAL                  221: Last_Traded_PE_Price
        7090    LOAD_CONST                    317: ' Place First Short Straddle order for CE/PE ATM Strike=('
        7094    LOAD_GLOBAL                   381: NULL + df_king_cnt
        7098    FORMAT_VALUE                  0
        7100    LOAD_CONST                    303: ','
        7104    LOAD_GLOBAL                   382: df_cols
        7108    FORMAT_VALUE                  0
        7110    LOAD_CONST                    312: '), ATM(CE,PE)=('
        7114    LOAD_GLOBAL                   222: entry_price
        7116    FORMAT_VALUE                  0
        7118    LOAD_CONST                    313: ', '
        7122    LOAD_GLOBAL                   221: NULL + strike_offset
        7124    FORMAT_VALUE                  0
        7126    LOAD_CONST                    314: ') '
        7130    BUILD_STRING                  9
        7132    STORE_NAME                    65: strMsg
        7134    LOAD_GLOBAL                   74: cfg
        7136    LOAD_CONST                    52: 2
        7138    BINARY_ADD                    
        7140    STORE_GLOBAL                  74: order_count
        7142    LOAD_NAME                     59: iLog
        7144    LOAD_NAME                     65: strMsg
        7146    LOAD_CONST                    288: 5
        7150    LOAD_CONST                    20: True
        7152    LOAD_CONST                    43: ('sendTeleMsg',)
        7154    CALL_FUNCTION_KW              3
        7156    POP_TOP                       
        7158    LOAD_GLOBAL                   76: read
        7160    LOAD_GLOBAL                   360: PE_TGT_Triggered
        7164    LOAD_CONST                    0: 0
        7166    BINARY_SUBSCR                 
        7168    LOAD_GLOBAL                   360: PE_TGT_Triggered
        7172    LOAD_CONST                    29: 1
        7174    BINARY_SUBSCR                 
        7176    LOAD_CONST                    292: -1
        7180    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7184    BINARY_MULTIPLY               
        7186    BUILD_LIST                    4
        7188    LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        7190    LOAD_ATTR                     379: loc
        7194    LOAD_CONST                    0: 0
        7196    LOAD_NAME                     197: leg_cols
        7198    BUILD_TUPLE                   2
        7200    STORE_SUBSCR                  
        7202    LOAD_GLOBAL                   76: read
        7204    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        7208    LOAD_CONST                    0: 0
        7210    BINARY_SUBSCR                 
        7212    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        7216    LOAD_CONST                    29: 1
        7218    BINARY_SUBSCR                 
        7220    LOAD_CONST                    292: -1
        7224    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7228    BINARY_MULTIPLY               
        7230    BUILD_LIST                    4
        7232    LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        7234    LOAD_ATTR                     379: loc
        7238    LOAD_CONST                    0: 0
        7240    LOAD_NAME                     197: leg_cols
        7242    BUILD_TUPLE                   2
        7244    STORE_SUBSCR                  
        7246    LOAD_NAME                     24: pd
        7248    LOAD_METHOD                   380: concat
        7252    LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        7254    LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        7256    BUILD_LIST                    2
        7258    CALL_METHOD                   1
        7260    STORE_GLOBAL                  200: Current_legs
        7262    LOAD_GLOBAL                   76: read
        7264    LOAD_NAME                     376: Symbol
        7268    LOAD_GLOBAL                   381: NULL + df_king_cnt
        7272    LOAD_CONST                    315: 'CE'
        7276    LOAD_CONST                    292: -1
        7280    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7284    LOAD_GLOBAL                   222: entry_price
        7286    LOAD_CONST                    29: 1
        7288    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7292    BINARY_MULTIPLY               
        7294    LOAD_GLOBAL                   222: entry_price
        7296    BINARY_MULTIPLY               
        7298    BUILD_LIST                    8
        7300    LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        7302    LOAD_ATTR                     379: loc
        7306    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7308    LOAD_NAME                     191: df_cols
        7310    BUILD_TUPLE                   2
        7312    STORE_SUBSCR                  
        7314    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7316    LOAD_CONST                    29: 1
        7318    BINARY_ADD                    
        7320    STORE_GLOBAL                  190: df_king_cnt
        7322    LOAD_GLOBAL                   76: read
        7324    LOAD_NAME                     376: Symbol
        7328    LOAD_GLOBAL                   382: df_cols
        7332    LOAD_CONST                    316: 'PE'
        7336    LOAD_CONST                    292: -1
        7340    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7344    LOAD_GLOBAL                   221: NULL + strike_offset
        7346    LOAD_CONST                    29: 1
        7348    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7352    BINARY_MULTIPLY               
        7354    LOAD_GLOBAL                   221: NULL + strike_offset
        7356    BINARY_MULTIPLY               
        7358    BUILD_LIST                    8
        7360    LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        7362    LOAD_ATTR                     379: loc
        7366    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7368    LOAD_NAME                     191: df_cols
        7370    BUILD_TUPLE                   2
        7372    STORE_SUBSCR                  
        7374    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7376    LOAD_CONST                    29: 1
        7378    BINARY_ADD                    
        7380    STORE_GLOBAL                  190: df_king_cnt
        7382    LOAD_CONST                    20: True
        7384    STORE_GLOBAL                  170: First_Straddle
        7386    LOAD_GLOBAL                   78: get
        7388    LOAD_CONST                    0: 0
        7390    COMPARE_OP                    2 (==)
        7392    POP_JUMP_IF_FALSE             4820 (to 9640)
        7396    LOAD_GLOBAL                   144: tl
        7398    LOAD_CONST                    29: 1
        7400    COMPARE_OP                    2 (==)
        7402    POP_JUMP_IF_FALSE             4216 (to 8432)
        7406    LOAD_NAME                     308: place_order
        7410    LOAD_CONST                    318: 'B'
        7414    LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        7418    LOAD_CONST                    52: 2
        7420    BINARY_SUBSCR                 
        7422    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7426    CALL_FUNCTION                 3
        7428    STORE_GLOBAL                  383: order_id_CE
        7432    LOAD_GLOBAL                   74: cfg
        7434    LOAD_CONST                    29: 1
        7436    BINARY_ADD                    
        7438    STORE_GLOBAL                  74: order_count
        7440    LOAD_GLOBAL                   266: expiry_Single_Leg_Adj_Delta_PCT
        7444    STORE_GLOBAL                  224: Last_Traded_CE_Price_hedge
        7446    LOAD_GLOBAL                   383: NULL + df_cols
        7450    LOAD_CONST                    319: 'norenordno'
        7454    BINARY_SUBSCR                 
        7456    STORE_NAME                    384: order_id
        7460    LOAD_NAME                     311: get_order_symbol
        7464    LOAD_NAME                     384: order_id
        7468    CALL_FUNCTION                 1
        7470    STORE_NAME                    376: Symbol
        7474    LOAD_GLOBAL                   383: NULL + df_cols
        7478    LOAD_CONST                    320: 'stat'
        7482    BINARY_SUBSCR                 
        7484    STORE_NAME                    385: Placed_Status
        7488    LOAD_NAME                     309: get_order_status
        7492    LOAD_NAME                     384: order_id
        7496    CALL_FUNCTION                 1
        7498    STORE_NAME                    386: Return_Status
        7502    LOAD_NAME                     310: get_order_price
        7506    LOAD_NAME                     384: order_id
        7510    CALL_FUNCTION                 1
        7512    STORE_NAME                    387: average_price
        7516    LOAD_NAME                     386: Return_Status
        7520    LOAD_METHOD                   352: upper
        7524    CALL_METHOD                   0
        7526    LOAD_CONST                    321: 'REJECTED'
        7530    COMPARE_OP                    2 (==)
        7532    POP_JUMP_IF_FALSE             3814 (to 7628)
        7536    LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        7540    LOAD_NAME                     384: order_id
        7544    FORMAT_VALUE                  0
        7546    LOAD_CONST                    323: ', Ord_STS = '
        7550    LOAD_NAME                     385: Placed_Status
        7554    FORMAT_VALUE                  0
        7556    LOAD_CONST                    324: ', Ret_STS = '
        7560    LOAD_NAME                     386: Return_Status
        7564    FORMAT_VALUE                  0
        7566    LOAD_CONST                    325: '.Exiting Algo'
        7570    BUILD_STRING                  7
        7572    STORE_NAME                    65: strMsg
        7574    LOAD_NAME                     59: iLog
        7576    LOAD_NAME                     65: strMsg
        7578    LOAD_CONST                    42: 4
        7580    LOAD_CONST                    20: True
        7582    LOAD_CONST                    43: ('sendTeleMsg',)
        7584    CALL_FUNCTION_KW              3
        7586    POP_TOP                       
        7588    LOAD_GLOBAL                   144: tl
        7590    LOAD_CONST                    29: 1
        7592    COMPARE_OP                    2 (==)
        7594    POP_JUMP_IF_FALSE             3809 (to 7618)
        7598    LOAD_CONST                    326: ' Exiting Algo.Cross Check for any Open positions'
        7602    STORE_NAME                    65: strMsg
        7604    LOAD_NAME                     59: iLog
        7606    LOAD_NAME                     65: strMsg
        7608    LOAD_CONST                    42: 4
        7610    LOAD_CONST                    20: True
        7612    LOAD_CONST                    43: ('sendTeleMsg',)
        7614    CALL_FUNCTION_KW              3
        7616    POP_TOP                       
        7618    LOAD_NAME                     0: sys
        7620    LOAD_METHOD                   344: exit
        7624    CALL_METHOD                   0
        7626    POP_TOP                       
        7628    LOAD_NAME                     387: average_price
        7632    LOAD_CONST                    0: 0
        7634    COMPARE_OP                    4 (>)
        7636    POP_JUMP_IF_FALSE             3833 (to 7666)
        7640    LOAD_NAME                     386: Return_Status
        7644    LOAD_METHOD                   352: upper
        7648    CALL_METHOD                   0
        7650    LOAD_CONST                    327: 'COMPLETE'
        7654    COMPARE_OP                    2 (==)
        7656    POP_JUMP_IF_FALSE             3833 (to 7666)
        7660    LOAD_NAME                     387: average_price
        7664    STORE_GLOBAL                  224: Last_Traded_CE_Price_hedge
        7666    LOAD_GLOBAL                   76: read
        7668    LOAD_NAME                     376: Symbol
        7672    LOAD_GLOBAL                   377: NULL + current_premium_delta
        7676    LOAD_CONST                    315: 'CE'
        7680    LOAD_CONST                    29: 1
        7682    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7686    LOAD_GLOBAL                   224: entry_price_buffer
        7688    LOAD_CONST                    292: -1
        7692    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7696    BINARY_MULTIPLY               
        7698    LOAD_GLOBAL                   224: entry_price_buffer
        7700    BINARY_MULTIPLY               
        7702    BUILD_LIST                    8
        7704    LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        7706    LOAD_ATTR                     379: loc
        7710    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7712    LOAD_NAME                     191: df_cols
        7714    BUILD_TUPLE                   2
        7716    STORE_SUBSCR                  
        7718    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        7720    LOAD_CONST                    29: 1
        7722    BINARY_ADD                    
        7724    STORE_GLOBAL                  190: df_king_cnt
        7726    LOAD_CONST                    328: ' Placed First Hedge CE Buy Market order Stike: '
        7730    LOAD_GLOBAL                   377: NULL + current_premium_delta
        7734    FORMAT_VALUE                  0
        7736    LOAD_CONST                    329: ' ATM CE='
        7740    LOAD_NAME                     387: average_price
        7744    FORMAT_VALUE                  0
        7746    LOAD_CONST                    330: ', Qty ='
        7750    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7754    FORMAT_VALUE                  0
        7756    LOAD_CONST                    331: ', Ord_ID = '
        7760    LOAD_NAME                     384: order_id
        7764    FORMAT_VALUE                  0
        7766    LOAD_CONST                    323: ', Ord_STS = '
        7770    LOAD_NAME                     385: Placed_Status
        7774    FORMAT_VALUE                  0
        7776    LOAD_CONST                    324: ', Ret_STS = '
        7780    LOAD_NAME                     386: Return_Status
        7784    FORMAT_VALUE                  0
        7786    BUILD_STRING                  12
        7788    STORE_NAME                    65: strMsg
        7790    LOAD_NAME                     59: iLog
        7792    LOAD_NAME                     65: strMsg
        7794    LOAD_CONST                    288: 5
        7798    LOAD_CONST                    20: True
        7800    LOAD_CONST                    43: ('sendTeleMsg',)
        7802    CALL_FUNCTION_KW              3
        7804    POP_TOP                       
        7806    LOAD_NAME                     72: tl
        7808    LOAD_METHOD                   388: update_csv
        7812    LOAD_NAME                     376: Symbol
        7816    LOAD_CONST                    332: 'Buy'
        7820    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7824    LOAD_GLOBAL                   224: entry_price_buffer
        7826    LOAD_NAME                     384: order_id
        7830    LOAD_NAME                     385: Placed_Status
        7834    LOAD_NAME                     386: Return_Status
        7838    CALL_METHOD                   7
        7840    POP_TOP                       
        7842    LOAD_GLOBAL                   76: read
        7844    LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        7848    LOAD_CONST                    0: 0
        7850    BINARY_SUBSCR                 
        7852    LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        7856    LOAD_CONST                    29: 1
        7858    BINARY_SUBSCR                 
        7860    LOAD_CONST                    29: 1
        7862    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7866    BINARY_MULTIPLY               
        7868    BUILD_LIST                    4
        7870    LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        7872    LOAD_ATTR                     379: loc
        7876    LOAD_CONST                    0: 0
        7878    LOAD_NAME                     197: leg_cols
        7880    BUILD_TUPLE                   2
        7882    STORE_SUBSCR                  
        7884    LOAD_GLOBAL                   76: read
        7886    LOAD_GLOBAL                   364: partial_profit_booked
        7890    LOAD_CONST                    0: 0
        7892    BINARY_SUBSCR                 
        7894    LOAD_GLOBAL                   364: partial_profit_booked
        7898    LOAD_CONST                    29: 1
        7900    BINARY_SUBSCR                 
        7902    LOAD_CONST                    0: 0
        7904    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7908    BINARY_MULTIPLY               
        7910    BUILD_LIST                    4
        7912    LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        7914    LOAD_ATTR                     379: loc
        7918    LOAD_CONST                    0: 0
        7920    LOAD_NAME                     197: leg_cols
        7922    BUILD_TUPLE                   2
        7924    STORE_SUBSCR                  
        7926    LOAD_NAME                     308: place_order
        7930    LOAD_CONST                    318: 'B'
        7934    LOAD_GLOBAL                   364: partial_profit_booked
        7938    LOAD_CONST                    52: 2
        7940    BINARY_SUBSCR                 
        7942    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        7946    CALL_FUNCTION                 3
        7948    STORE_GLOBAL                  389: order_id_PE
        7952    LOAD_GLOBAL                   74: cfg
        7954    LOAD_CONST                    29: 1
        7956    BINARY_ADD                    
        7958    STORE_GLOBAL                  74: order_count
        7960    LOAD_GLOBAL                   267: NULL + expiry_Single_Leg_Adj_Delta_PCT
        7964    STORE_GLOBAL                  223: Last_Traded_PE_Price_hedge
        7966    LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        7970    LOAD_CONST                    319: 'norenordno'
        7974    BINARY_SUBSCR                 
        7976    STORE_NAME                    384: order_id
        7980    LOAD_NAME                     311: get_order_symbol
        7984    LOAD_NAME                     384: order_id
        7988    CALL_FUNCTION                 1
        7990    STORE_NAME                    376: Symbol
        7994    LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        7998    LOAD_CONST                    320: 'stat'
        8002    BINARY_SUBSCR                 
        8004    STORE_NAME                    385: Placed_Status
        8008    LOAD_NAME                     309: get_order_status
        8012    LOAD_NAME                     384: order_id
        8016    CALL_FUNCTION                 1
        8018    STORE_NAME                    386: Return_Status
        8022    LOAD_NAME                     310: get_order_price
        8026    LOAD_NAME                     384: order_id
        8030    CALL_FUNCTION                 1
        8032    STORE_NAME                    387: average_price
        8036    LOAD_NAME                     386: Return_Status
        8040    LOAD_METHOD                   352: upper
        8044    CALL_METHOD                   0
        8046    LOAD_CONST                    321: 'REJECTED'
        8050    COMPARE_OP                    2 (==)
        8052    POP_JUMP_IF_FALSE             4074 (to 8148)
        8056    LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        8060    LOAD_NAME                     384: order_id
        8064    FORMAT_VALUE                  0
        8066    LOAD_CONST                    323: ', Ord_STS = '
        8070    LOAD_NAME                     385: Placed_Status
        8074    FORMAT_VALUE                  0
        8076    LOAD_CONST                    324: ', Ret_STS = '
        8080    LOAD_NAME                     386: Return_Status
        8084    FORMAT_VALUE                  0
        8086    LOAD_CONST                    333: '.'
        8090    BUILD_STRING                  7
        8092    STORE_NAME                    65: strMsg
        8094    LOAD_NAME                     59: iLog
        8096    LOAD_NAME                     65: strMsg
        8098    LOAD_CONST                    288: 5
        8102    LOAD_CONST                    20: True
        8104    LOAD_CONST                    43: ('sendTeleMsg',)
        8106    CALL_FUNCTION_KW              3
        8108    POP_TOP                       
        8110    LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        8114    STORE_NAME                    65: strMsg
        8116    LOAD_NAME                     59: iLog
        8118    LOAD_NAME                     65: strMsg
        8120    LOAD_CONST                    42: 4
        8122    LOAD_CONST                    20: True
        8124    LOAD_CONST                    43: ('sendTeleMsg',)
        8126    CALL_FUNCTION_KW              3
        8128    POP_TOP                       
        8130    LOAD_NAME                     322: close_all_orders
        8134    CALL_FUNCTION                 0
        8136    POP_TOP                       
        8138    LOAD_NAME                     0: sys
        8140    LOAD_METHOD                   344: exit
        8144    CALL_METHOD                   0
        8146    POP_TOP                       
        8148    LOAD_NAME                     387: average_price
        8152    LOAD_CONST                    0: 0
        8154    COMPARE_OP                    4 (>)
        8156    POP_JUMP_IF_FALSE             4093 (to 8186)
        8160    LOAD_NAME                     386: Return_Status
        8164    LOAD_METHOD                   352: upper
        8168    CALL_METHOD                   0
        8170    LOAD_CONST                    327: 'COMPLETE'
        8174    COMPARE_OP                    2 (==)
        8176    POP_JUMP_IF_FALSE             4093 (to 8186)
        8180    LOAD_NAME                     387: average_price
        8184    STORE_GLOBAL                  223: Last_Traded_PE_Price_hedge
        8186    LOAD_GLOBAL                   76: read
        8188    LOAD_NAME                     376: Symbol
        8192    LOAD_GLOBAL                   378: Usr_Lic
        8196    LOAD_CONST                    316: 'PE'
        8200    LOAD_CONST                    29: 1
        8202    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8206    LOAD_GLOBAL                   221: NULL + strike_offset
        8208    LOAD_CONST                    292: -1
        8212    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8216    BINARY_MULTIPLY               
        8218    LOAD_GLOBAL                   223: NULL + entry_price
        8220    BINARY_MULTIPLY               
        8222    BUILD_LIST                    8
        8224    LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        8226    LOAD_ATTR                     379: loc
        8230    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        8232    LOAD_NAME                     191: df_cols
        8234    BUILD_TUPLE                   2
        8236    STORE_SUBSCR                  
        8238    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        8240    LOAD_CONST                    29: 1
        8242    BINARY_ADD                    
        8244    STORE_GLOBAL                  190: df_king_cnt
        8246    LOAD_CONST                    335: ' Placed First Hedge PE Buy Market order Stike: '
        8250    LOAD_GLOBAL                   378: Usr_Lic
        8254    FORMAT_VALUE                  0
        8256    LOAD_CONST                    336: ' ATM PE='
        8260    LOAD_NAME                     387: average_price
        8264    FORMAT_VALUE                  0
        8266    LOAD_CONST                    330: ', Qty ='
        8270    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8274    FORMAT_VALUE                  0
        8276    LOAD_CONST                    331: ', Ord_ID = '
        8280    LOAD_NAME                     384: order_id
        8284    FORMAT_VALUE                  0
        8286    LOAD_CONST                    323: ', Ord_STS = '
        8290    LOAD_NAME                     385: Placed_Status
        8294    FORMAT_VALUE                  0
        8296    LOAD_CONST                    324: ', Ret_STS = '
        8300    LOAD_NAME                     386: Return_Status
        8304    FORMAT_VALUE                  0
        8306    BUILD_STRING                  12
        8308    STORE_NAME                    65: strMsg
        8310    LOAD_NAME                     59: iLog
        8312    LOAD_NAME                     65: strMsg
        8314    LOAD_CONST                    288: 5
        8318    LOAD_CONST                    20: True
        8320    LOAD_CONST                    43: ('sendTeleMsg',)
        8322    CALL_FUNCTION_KW              3
        8324    POP_TOP                       
        8326    LOAD_NAME                     72: tl
        8328    LOAD_METHOD                   388: update_csv
        8332    LOAD_NAME                     376: Symbol
        8336    LOAD_CONST                    332: 'Buy'
        8340    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8344    LOAD_GLOBAL                   223: NULL + entry_price
        8346    LOAD_NAME                     384: order_id
        8350    LOAD_NAME                     385: Placed_Status
        8354    LOAD_NAME                     386: Return_Status
        8358    CALL_METHOD                   7
        8360    POP_TOP                       
        8362    LOAD_GLOBAL                   76: read
        8364    LOAD_GLOBAL                   364: partial_profit_booked
        8368    LOAD_CONST                    0: 0
        8370    BINARY_SUBSCR                 
        8372    LOAD_GLOBAL                   364: partial_profit_booked
        8376    LOAD_CONST                    29: 1
        8378    BINARY_SUBSCR                 
        8380    LOAD_CONST                    29: 1
        8382    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8386    BINARY_MULTIPLY               
        8388    BUILD_LIST                    4
        8390    LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        8392    LOAD_ATTR                     379: loc
        8396    LOAD_CONST                    0: 0
        8398    LOAD_NAME                     197: leg_cols
        8400    BUILD_TUPLE                   2
        8402    STORE_SUBSCR                  
        8404    LOAD_NAME                     24: pd
        8406    LOAD_METHOD                   380: concat
        8410    LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        8412    LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        8414    BUILD_LIST                    2
        8416    CALL_METHOD                   1
        8418    STORE_GLOBAL                  203: Current_legs_hedge
        8420    LOAD_NAME                     2: time
        8422    LOAD_METHOD                   355: sleep
        8426    LOAD_CONST                    52: 2
        8428    CALL_METHOD                   1
        8430    POP_TOP                       
        8432    LOAD_NAME                     308: place_order
        8436    LOAD_CONST                    337: 'S'
        8440    LOAD_GLOBAL                   360: PE_TGT_Triggered
        8444    LOAD_CONST                    52: 2
        8446    BINARY_SUBSCR                 
        8448    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8452    CALL_FUNCTION                 3
        8454    STORE_GLOBAL                  383: order_id_CE
        8458    LOAD_GLOBAL                   74: cfg
        8460    LOAD_CONST                    29: 1
        8462    BINARY_ADD                    
        8464    STORE_GLOBAL                  74: order_count
        8466    LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        8470    STORE_GLOBAL                  222: Last_Traded_CE_Price
        8472    LOAD_GLOBAL                   383: NULL + df_cols
        8476    LOAD_CONST                    319: 'norenordno'
        8480    BINARY_SUBSCR                 
        8482    STORE_NAME                    384: order_id
        8486    LOAD_NAME                     311: get_order_symbol
        8490    LOAD_NAME                     384: order_id
        8494    CALL_FUNCTION                 1
        8496    STORE_NAME                    376: Symbol
        8500    LOAD_GLOBAL                   383: NULL + df_cols
        8504    LOAD_CONST                    320: 'stat'
        8508    BINARY_SUBSCR                 
        8510    STORE_NAME                    385: Placed_Status
        8514    LOAD_NAME                     309: get_order_status
        8518    LOAD_NAME                     384: order_id
        8522    CALL_FUNCTION                 1
        8524    STORE_NAME                    386: Return_Status
        8528    LOAD_NAME                     310: get_order_price
        8532    LOAD_NAME                     384: order_id
        8536    CALL_FUNCTION                 1
        8538    STORE_NAME                    387: average_price
        8542    LOAD_NAME                     386: Return_Status
        8546    LOAD_METHOD                   352: upper
        8550    CALL_METHOD                   0
        8552    LOAD_CONST                    321: 'REJECTED'
        8556    COMPARE_OP                    2 (==)
        8558    POP_JUMP_IF_FALSE             4317 (to 8634)
        8562    LOAD_GLOBAL                   144: tl
        8564    LOAD_CONST                    0: 0
        8566    COMPARE_OP                    2 (==)
        8568    POP_JUMP_IF_FALSE             4317 (to 8634)
        8572    LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        8576    LOAD_NAME                     384: order_id
        8580    FORMAT_VALUE                  0
        8582    LOAD_CONST                    323: ', Ord_STS = '
        8586    LOAD_NAME                     385: Placed_Status
        8590    FORMAT_VALUE                  0
        8592    LOAD_CONST                    324: ', Ret_STS = '
        8596    LOAD_NAME                     386: Return_Status
        8600    FORMAT_VALUE                  0
        8602    LOAD_CONST                    325: '.Exiting Algo'
        8606    BUILD_STRING                  7
        8608    STORE_NAME                    65: strMsg
        8610    LOAD_NAME                     59: iLog
        8612    LOAD_NAME                     65: strMsg
        8614    LOAD_CONST                    42: 4
        8616    LOAD_CONST                    20: True
        8618    LOAD_CONST                    43: ('sendTeleMsg',)
        8620    CALL_FUNCTION_KW              3
        8622    POP_TOP                       
        8624    LOAD_NAME                     0: sys
        8626    LOAD_METHOD                   344: exit
        8630    CALL_METHOD                   0
        8632    POP_TOP                       
        8634    LOAD_NAME                     386: Return_Status
        8638    LOAD_METHOD                   352: upper
        8642    CALL_METHOD                   0
        8644    LOAD_CONST                    321: 'REJECTED'
        8648    COMPARE_OP                    2 (==)
        8650    POP_JUMP_IF_FALSE             4420 (to 8840)
        8654    LOAD_GLOBAL                   144: tl
        8656    LOAD_CONST                    29: 1
        8658    COMPARE_OP                    2 (==)
        8660    POP_JUMP_IF_FALSE             4420 (to 8840)
        8664    LOAD_GLOBAL                   76: read
        8666    LOAD_GLOBAL                   360: PE_TGT_Triggered
        8670    LOAD_CONST                    0: 0
        8672    BINARY_SUBSCR                 
        8674    LOAD_GLOBAL                   360: PE_TGT_Triggered
        8678    LOAD_CONST                    29: 1
        8680    BINARY_SUBSCR                 
        8682    LOAD_CONST                    0: 0
        8684    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8688    BINARY_MULTIPLY               
        8690    BUILD_LIST                    4
        8692    LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        8694    LOAD_ATTR                     379: loc
        8698    LOAD_CONST                    0: 0
        8700    LOAD_NAME                     197: leg_cols
        8702    BUILD_TUPLE                   2
        8704    STORE_SUBSCR                  
        8706    LOAD_GLOBAL                   76: read
        8708    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        8712    LOAD_CONST                    0: 0
        8714    BINARY_SUBSCR                 
        8716    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        8720    LOAD_CONST                    29: 1
        8722    BINARY_SUBSCR                 
        8724    LOAD_CONST                    0: 0
        8726    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8730    BINARY_MULTIPLY               
        8732    BUILD_LIST                    4
        8734    LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        8736    LOAD_ATTR                     379: loc
        8740    LOAD_CONST                    0: 0
        8742    LOAD_NAME                     197: leg_cols
        8744    BUILD_TUPLE                   2
        8746    STORE_SUBSCR                  
        8748    LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        8752    LOAD_NAME                     384: order_id
        8756    FORMAT_VALUE                  0
        8758    LOAD_CONST                    323: ', Ord_STS = '
        8762    LOAD_NAME                     385: Placed_Status
        8766    FORMAT_VALUE                  0
        8768    LOAD_CONST                    324: ', Ret_STS = '
        8772    LOAD_NAME                     386: Return_Status
        8776    FORMAT_VALUE                  0
        8778    LOAD_CONST                    333: '.'
        8782    BUILD_STRING                  7
        8784    STORE_NAME                    65: strMsg
        8786    LOAD_NAME                     59: iLog
        8788    LOAD_NAME                     65: strMsg
        8790    LOAD_CONST                    288: 5
        8794    LOAD_CONST                    20: True
        8796    LOAD_CONST                    43: ('sendTeleMsg',)
        8798    CALL_FUNCTION_KW              3
        8800    POP_TOP                       
        8802    LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        8806    STORE_NAME                    65: strMsg
        8808    LOAD_NAME                     59: iLog
        8810    LOAD_NAME                     65: strMsg
        8812    LOAD_CONST                    42: 4
        8814    LOAD_CONST                    20: True
        8816    LOAD_CONST                    43: ('sendTeleMsg',)
        8818    CALL_FUNCTION_KW              3
        8820    POP_TOP                       
        8822    LOAD_NAME                     322: close_all_orders
        8826    CALL_FUNCTION                 0
        8828    POP_TOP                       
        8830    LOAD_NAME                     0: sys
        8832    LOAD_METHOD                   344: exit
        8836    CALL_METHOD                   0
        8838    POP_TOP                       
        8840    LOAD_NAME                     387: average_price
        8844    LOAD_CONST                    0: 0
        8846    COMPARE_OP                    4 (>)
        8848    POP_JUMP_IF_FALSE             4439 (to 8878)
        8852    LOAD_NAME                     386: Return_Status
        8856    LOAD_METHOD                   352: upper
        8860    CALL_METHOD                   0
        8862    LOAD_CONST                    327: 'COMPLETE'
        8866    COMPARE_OP                    2 (==)
        8868    POP_JUMP_IF_FALSE             4439 (to 8878)
        8872    LOAD_NAME                     387: average_price
        8876    STORE_GLOBAL                  222: Last_Traded_CE_Price
        8878    LOAD_GLOBAL                   76: read
        8880    LOAD_NAME                     376: Symbol
        8884    LOAD_GLOBAL                   381: NULL + df_king_cnt
        8888    LOAD_CONST                    315: 'CE'
        8892    LOAD_CONST                    292: -1
        8896    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8900    LOAD_GLOBAL                   222: entry_price
        8902    LOAD_CONST                    29: 1
        8904    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8908    BINARY_MULTIPLY               
        8910    LOAD_GLOBAL                   222: entry_price
        8912    BINARY_MULTIPLY               
        8914    BUILD_LIST                    8
        8916    LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        8918    LOAD_ATTR                     379: loc
        8922    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        8924    LOAD_NAME                     191: df_cols
        8926    BUILD_TUPLE                   2
        8928    STORE_SUBSCR                  
        8930    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        8932    LOAD_CONST                    29: 1
        8934    BINARY_ADD                    
        8936    STORE_GLOBAL                  190: df_king_cnt
        8938    LOAD_CONST                    338: ' Placed First ATM SS CE Sell Market order Stike: '
        8942    LOAD_GLOBAL                   381: NULL + df_king_cnt
        8946    FORMAT_VALUE                  0
        8948    LOAD_CONST                    329: ' ATM CE='
        8952    LOAD_NAME                     387: average_price
        8956    FORMAT_VALUE                  0
        8958    LOAD_CONST                    330: ', Qty ='
        8962    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        8966    FORMAT_VALUE                  0
        8968    LOAD_CONST                    331: ', Ord_ID = '
        8972    LOAD_NAME                     384: order_id
        8976    FORMAT_VALUE                  0
        8978    LOAD_CONST                    323: ', Ord_STS = '
        8982    LOAD_NAME                     385: Placed_Status
        8986    FORMAT_VALUE                  0
        8988    LOAD_CONST                    324: ', Ret_STS = '
        8992    LOAD_NAME                     386: Return_Status
        8996    FORMAT_VALUE                  0
        8998    BUILD_STRING                  12
        9000    STORE_NAME                    65: strMsg
        9002    LOAD_NAME                     59: iLog
        9004    LOAD_NAME                     65: strMsg
        9006    LOAD_CONST                    288: 5
        9010    LOAD_CONST                    20: True
        9012    LOAD_CONST                    43: ('sendTeleMsg',)
        9014    CALL_FUNCTION_KW              3
        9016    POP_TOP                       
        9018    LOAD_NAME                     72: tl
        9020    LOAD_METHOD                   388: update_csv
        9024    LOAD_NAME                     376: Symbol
        9028    LOAD_CONST                    339: 'Sell'
        9032    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9036    LOAD_GLOBAL                   222: entry_price
        9038    LOAD_NAME                     384: order_id
        9042    LOAD_NAME                     385: Placed_Status
        9046    LOAD_NAME                     386: Return_Status
        9050    CALL_METHOD                   7
        9052    POP_TOP                       
        9054    LOAD_GLOBAL                   76: read
        9056    LOAD_GLOBAL                   360: PE_TGT_Triggered
        9060    LOAD_CONST                    0: 0
        9062    BINARY_SUBSCR                 
        9064    LOAD_GLOBAL                   360: PE_TGT_Triggered
        9068    LOAD_CONST                    29: 1
        9070    BINARY_SUBSCR                 
        9072    LOAD_CONST                    292: -1
        9076    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9080    BINARY_MULTIPLY               
        9082    BUILD_LIST                    4
        9084    LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        9086    LOAD_ATTR                     379: loc
        9090    LOAD_CONST                    0: 0
        9092    LOAD_NAME                     197: leg_cols
        9094    BUILD_TUPLE                   2
        9096    STORE_SUBSCR                  
        9098    LOAD_GLOBAL                   76: read
        9100    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        9104    LOAD_CONST                    0: 0
        9106    BINARY_SUBSCR                 
        9108    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        9112    LOAD_CONST                    29: 1
        9114    BINARY_SUBSCR                 
        9116    LOAD_CONST                    0: 0
        9118    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9122    BINARY_MULTIPLY               
        9124    BUILD_LIST                    4
        9126    LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        9128    LOAD_ATTR                     379: loc
        9132    LOAD_CONST                    0: 0
        9134    LOAD_NAME                     197: leg_cols
        9136    BUILD_TUPLE                   2
        9138    STORE_SUBSCR                  
        9140    LOAD_NAME                     308: place_order
        9144    LOAD_CONST                    337: 'S'
        9148    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        9152    LOAD_CONST                    52: 2
        9154    BINARY_SUBSCR                 
        9156    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9160    CALL_FUNCTION                 3
        9162    STORE_GLOBAL                  389: order_id_PE
        9166    LOAD_GLOBAL                   74: cfg
        9168    LOAD_CONST                    29: 1
        9170    BINARY_ADD                    
        9172    STORE_GLOBAL                  74: order_count
        9174    LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        9178    STORE_GLOBAL                  221: Last_Traded_PE_Price
        9180    LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        9184    LOAD_CONST                    319: 'norenordno'
        9188    BINARY_SUBSCR                 
        9190    STORE_NAME                    384: order_id
        9194    LOAD_NAME                     311: get_order_symbol
        9198    LOAD_NAME                     384: order_id
        9202    CALL_FUNCTION                 1
        9204    STORE_NAME                    376: Symbol
        9208    LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        9212    LOAD_CONST                    320: 'stat'
        9216    BINARY_SUBSCR                 
        9218    STORE_NAME                    385: Placed_Status
        9222    LOAD_NAME                     309: get_order_status
        9226    LOAD_NAME                     384: order_id
        9230    CALL_FUNCTION                 1
        9232    STORE_NAME                    386: Return_Status
        9236    LOAD_NAME                     310: get_order_price
        9240    LOAD_NAME                     384: order_id
        9244    CALL_FUNCTION                 1
        9246    STORE_NAME                    387: average_price
        9250    LOAD_NAME                     386: Return_Status
        9254    LOAD_METHOD                   352: upper
        9258    CALL_METHOD                   0
        9260    LOAD_CONST                    321: 'REJECTED'
        9264    COMPARE_OP                    2 (==)
        9266    POP_JUMP_IF_FALSE             4681 (to 9362)
        9270    LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        9274    LOAD_NAME                     384: order_id
        9278    FORMAT_VALUE                  0
        9280    LOAD_CONST                    323: ', Ord_STS = '
        9284    LOAD_NAME                     385: Placed_Status
        9288    FORMAT_VALUE                  0
        9290    LOAD_CONST                    324: ', Ret_STS = '
        9294    LOAD_NAME                     386: Return_Status
        9298    FORMAT_VALUE                  0
        9300    LOAD_CONST                    333: '.'
        9304    BUILD_STRING                  7
        9306    STORE_NAME                    65: strMsg
        9308    LOAD_NAME                     59: iLog
        9310    LOAD_NAME                     65: strMsg
        9312    LOAD_CONST                    288: 5
        9316    LOAD_CONST                    20: True
        9318    LOAD_CONST                    43: ('sendTeleMsg',)
        9320    CALL_FUNCTION_KW              3
        9322    POP_TOP                       
        9324    LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        9328    STORE_NAME                    65: strMsg
        9330    LOAD_NAME                     59: iLog
        9332    LOAD_NAME                     65: strMsg
        9334    LOAD_CONST                    42: 4
        9336    LOAD_CONST                    20: True
        9338    LOAD_CONST                    43: ('sendTeleMsg',)
        9340    CALL_FUNCTION_KW              3
        9342    POP_TOP                       
        9344    LOAD_NAME                     322: close_all_orders
        9348    CALL_FUNCTION                 0
        9350    POP_TOP                       
        9352    LOAD_NAME                     0: sys
        9354    LOAD_METHOD                   344: exit
        9358    CALL_METHOD                   0
        9360    POP_TOP                       
        9362    LOAD_NAME                     387: average_price
        9366    LOAD_CONST                    0: 0
        9368    COMPARE_OP                    4 (>)
        9370    POP_JUMP_IF_FALSE             4700 (to 9400)
        9374    LOAD_NAME                     386: Return_Status
        9378    LOAD_METHOD                   352: upper
        9382    CALL_METHOD                   0
        9384    LOAD_CONST                    327: 'COMPLETE'
        9388    COMPARE_OP                    2 (==)
        9390    POP_JUMP_IF_FALSE             4700 (to 9400)
        9394    LOAD_NAME                     387: average_price
        9398    STORE_GLOBAL                  221: Last_Traded_PE_Price
        9400    LOAD_GLOBAL                   76: read
        9402    LOAD_NAME                     376: Symbol
        9406    LOAD_GLOBAL                   382: df_cols
        9410    LOAD_CONST                    316: 'PE'
        9414    LOAD_CONST                    292: -1
        9418    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9422    LOAD_GLOBAL                   221: NULL + strike_offset
        9424    LOAD_CONST                    29: 1
        9426    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9430    BINARY_MULTIPLY               
        9432    LOAD_GLOBAL                   221: NULL + strike_offset
        9434    BINARY_MULTIPLY               
        9436    BUILD_LIST                    8
        9438    LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        9440    LOAD_ATTR                     379: loc
        9444    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        9446    LOAD_NAME                     191: df_cols
        9448    BUILD_TUPLE                   2
        9450    STORE_SUBSCR                  
        9452    LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        9454    LOAD_CONST                    29: 1
        9456    BINARY_ADD                    
        9458    STORE_GLOBAL                  190: df_king_cnt
        9460    LOAD_CONST                    340: ' Placed First ATM SS PE Sell Market order Stike: '
        9464    LOAD_GLOBAL                   382: df_cols
        9468    FORMAT_VALUE                  0
        9470    LOAD_CONST                    336: ' ATM PE='
        9474    LOAD_NAME                     387: average_price
        9478    FORMAT_VALUE                  0
        9480    LOAD_CONST                    330: ', Qty ='
        9484    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9488    FORMAT_VALUE                  0
        9490    LOAD_CONST                    331: ', Ord_ID = '
        9494    LOAD_NAME                     384: order_id
        9498    FORMAT_VALUE                  0
        9500    LOAD_CONST                    323: ', Ord_STS = '
        9504    LOAD_NAME                     385: Placed_Status
        9508    FORMAT_VALUE                  0
        9510    LOAD_CONST                    324: ', Ret_STS = '
        9514    LOAD_NAME                     386: Return_Status
        9518    FORMAT_VALUE                  0
        9520    BUILD_STRING                  12
        9522    STORE_NAME                    65: strMsg
        9524    LOAD_NAME                     59: iLog
        9526    LOAD_NAME                     65: strMsg
        9528    LOAD_CONST                    288: 5
        9532    LOAD_CONST                    20: True
        9534    LOAD_CONST                    43: ('sendTeleMsg',)
        9536    CALL_FUNCTION_KW              3
        9538    POP_TOP                       
        9540    LOAD_NAME                     72: tl
        9542    LOAD_METHOD                   388: update_csv
        9546    LOAD_NAME                     376: Symbol
        9550    LOAD_CONST                    339: 'Sell'
        9554    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9558    LOAD_GLOBAL                   221: NULL + strike_offset
        9560    LOAD_NAME                     384: order_id
        9564    LOAD_NAME                     385: Placed_Status
        9568    LOAD_NAME                     386: Return_Status
        9572    CALL_METHOD                   7
        9574    POP_TOP                       
        9576    LOAD_GLOBAL                   76: read
        9578    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        9582    LOAD_CONST                    0: 0
        9584    BINARY_SUBSCR                 
        9586    LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        9590    LOAD_CONST                    29: 1
        9592    BINARY_SUBSCR                 
        9594    LOAD_CONST                    292: -1
        9598    LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        9602    BINARY_MULTIPLY               
        9604    BUILD_LIST                    4
        9606    LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        9608    LOAD_ATTR                     379: loc
        9612    LOAD_CONST                    0: 0
        9614    LOAD_NAME                     197: leg_cols
        9616    BUILD_TUPLE                   2
        9618    STORE_SUBSCR                  
        9620    LOAD_NAME                     24: pd
        9622    LOAD_METHOD                   380: concat
        9626    LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        9628    LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        9630    BUILD_LIST                    2
        9632    CALL_METHOD                   1
        9634    STORE_GLOBAL                  200: Current_legs
        9636    LOAD_CONST                    20: True
        9638    STORE_GLOBAL                  170: First_Straddle
        9640    LOAD_GLOBAL                   151: NULL + Algo_Running_Status
        9642    LOAD_CONST                    0: 0
        9644    COMPARE_OP                    2 (==)
        9646    POP_JUMP_IF_TRUE              4837 (to 9674)
        9650    LOAD_GLOBAL                   151: NULL + Algo_Running_Status
        9652    LOAD_CONST                    29: 1
        9654    COMPARE_OP                    2 (==)
        9656    POP_JUMP_IF_FALSE             10114 (to 20228)
        9660    LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        9662    LOAD_GLOBAL                   79: NULL + get
        9664    BINARY_TRUE_DIVIDE            
        9666    LOAD_GLOBAL                   152: cur_HHMM
        9668    COMPARE_OP                    0 (<)
        9670    POP_JUMP_IF_FALSE             10114 (to 20228)
        9674    LOAD_NAME                     21: datetime
        9676    LOAD_ATTR                     21: datetime
        9678    LOAD_METHOD                   51: now
        9680    CALL_METHOD                   0
        9682    LOAD_ATTR                     372: minute
        9686    STORE_NAME                    207: cur_min
        9688    LOAD_NAME                     44: int
        9690    LOAD_NAME                     21: datetime
        9692    LOAD_ATTR                     21: datetime
        9694    LOAD_METHOD                   51: now
        9696    CALL_METHOD                   0
        9698    LOAD_METHOD                   52: strftime
        9700    LOAD_CONST                    291: '%H%M%S'
        9704    CALL_METHOD                   1
        9706    CALL_FUNCTION                 1
        9708    STORE_GLOBAL                  368: cur_HHMMSS
        9712    LOAD_GLOBAL                   150: Algo_Running_Status
        9714    LOAD_CONST                    29: 1
        9716    COMPARE_OP                    2 (==)
        9718    POP_JUMP_IF_FALSE             4901 (to 9802)
        9722    LOAD_NAME                     207: cur_min
        9724    LOAD_CONST                    29: 1
        9726    BINARY_MODULO                 
        9728    LOAD_CONST                    0: 0
        9730    COMPARE_OP                    2 (==)
        9732    POP_JUMP_IF_FALSE             4901 (to 9802)
        9736    LOAD_NAME                     211: log1_min
        9738    LOAD_NAME                     207: cur_min
        9740    COMPARE_OP                    3 (!=)
        9742    POP_JUMP_IF_FALSE             4901 (to 9802)
        9746    LOAD_GLOBAL                   368: PE_LTP_Update_Count
        9750    LOAD_GLOBAL                   87: NULL + strBotTokenWObot
        9752    COMPARE_OP                    5 (>=)
        9754    POP_JUMP_IF_FALSE             4901 (to 9802)
        9758    LOAD_GLOBAL                   170: King_Candle_Max_SL
        9760    LOAD_CONST                    20: True
        9762    COMPARE_OP                    2 (==)
        9764    POP_JUMP_IF_FALSE             4901 (to 9802)
        9768    LOAD_GLOBAL                   296: hedge_buy_price_buffer
        9772    LOAD_CONST                    0: 0
        9774    COMPARE_OP                    2 (==)
        9776    POP_JUMP_IF_TRUE              4956 (to 9912)
        9780    LOAD_GLOBAL                   296: hedge_buy_price_buffer
        9784    LOAD_CONST                    0: 0
        9786    COMPARE_OP                    3 (!=)
        9788    POP_JUMP_IF_FALSE             4901 (to 9802)
        9792    LOAD_GLOBAL                   247: NULL + ADX_Period
        9794    LOAD_CONST                    0: 0
        9796    COMPARE_OP                    2 (==)
        9798    POP_JUMP_IF_TRUE              4956 (to 9912)
        9802    LOAD_GLOBAL                   150: Algo_Running_Status
        9804    LOAD_CONST                    0: 0
        9806    COMPARE_OP                    2 (==)
        9808    POP_JUMP_IF_TRUE              4928 (to 9856)
        9812    LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        9814    LOAD_CONST                    341: 'NQ'
        9818    BINARY_SUBSCR                 
        9820    LOAD_METHOD                   390: sum
        9824    CALL_METHOD                   0
        9826    LOAD_CONST                    0: 0
        9828    COMPARE_OP                    2 (==)
        9830    POP_JUMP_IF_TRUE              4928 (to 9856)
        9834    LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        9836    LOAD_CONST                    341: 'NQ'
        9840    BINARY_SUBSCR                 
        9842    LOAD_METHOD                   390: sum
        9846    CALL_METHOD                   0
        9848    LOAD_CONST                    0: 0
        9850    COMPARE_OP                    2 (==)
        9852    POP_JUMP_IF_FALSE             10114 (to 20228)
        9856    LOAD_GLOBAL                   368: PE_LTP_Update_Count
        9860    LOAD_GLOBAL                   87: NULL + strBotTokenWObot
        9862    COMPARE_OP                    5 (>=)
        9864    POP_JUMP_IF_FALSE             10114 (to 20228)
        9868    LOAD_GLOBAL                   170: King_Candle_Max_SL
        9870    LOAD_CONST                    20: True
        9872    COMPARE_OP                    2 (==)
        9874    POP_JUMP_IF_FALSE             10114 (to 20228)
        9878    LOAD_GLOBAL                   296: hedge_buy_price_buffer
        9882    LOAD_CONST                    0: 0
        9884    COMPARE_OP                    2 (==)
        9886    POP_JUMP_IF_TRUE              4956 (to 9912)
        9890    LOAD_GLOBAL                   296: hedge_buy_price_buffer
        9894    LOAD_CONST                    0: 0
        9896    COMPARE_OP                    3 (!=)
        9898    POP_JUMP_IF_FALSE             10114 (to 20228)
        9902    LOAD_GLOBAL                   247: NULL + ADX_Period
        9904    LOAD_CONST                    0: 0
        9906    COMPARE_OP                    2 (==)
        9908    POP_JUMP_IF_FALSE             10114 (to 20228)
        9912    LOAD_NAME                     207: cur_min
        9914    STORE_NAME                    211: log1_min
        9916    LOAD_NAME                     21: datetime
        9918    LOAD_ATTR                     347: date
        9922    LOAD_METHOD                   348: today
        9926    CALL_METHOD                   0
        9928    LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        9932    COMPARE_OP                    3 (!=)
        9934    POP_JUMP_IF_FALSE             5009 (to 10018)
        9938    LOAD_NAME                     374: round
        9942    LOAD_NAME                     391: max
        9946    LOAD_GLOBAL                   222: entry_price
        9948    LOAD_NAME                     391: max
        9952    LOAD_GLOBAL                   222: entry_price
        9954    LOAD_GLOBAL                   242: RSI_High
        9956    BINARY_MULTIPLY               
        9958    LOAD_CONST                    73: 100
        9960    BINARY_TRUE_DIVIDE            
        9962    LOAD_GLOBAL                   107: NULL + windll
        9964    CALL_FUNCTION                 2
        9966    BINARY_SUBTRACT               
        9968    LOAD_GLOBAL                   103: NULL + now
        9970    CALL_FUNCTION                 2
        9972    LOAD_CONST                    29: 1
        9974    CALL_FUNCTION                 2
        9976    STORE_GLOBAL                  252: CE_Leg_Target
        9978    LOAD_NAME                     374: round
        9982    LOAD_NAME                     391: max
        9986    LOAD_GLOBAL                   221: NULL + strike_offset
        9988    LOAD_NAME                     391: max
        9992    LOAD_GLOBAL                   221: NULL + strike_offset
        9994    LOAD_GLOBAL                   242: RSI_High
        9996    BINARY_MULTIPLY               
        9998    LOAD_CONST                    73: 100
        10000   BINARY_TRUE_DIVIDE            
        10002   LOAD_GLOBAL                   107: NULL + windll
        10004   CALL_FUNCTION                 2
        10006   BINARY_SUBTRACT               
        10008   LOAD_GLOBAL                   103: NULL + now
        10010   CALL_FUNCTION                 2
        10012   LOAD_CONST                    29: 1
        10014   CALL_FUNCTION                 2
        10016   STORE_GLOBAL                  253: PE_Leg_Target
        10018   LOAD_NAME                     21: datetime
        10020   LOAD_ATTR                     347: date
        10024   LOAD_METHOD                   348: today
        10028   CALL_METHOD                   0
        10030   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        10034   COMPARE_OP                    2 (==)
        10036   POP_JUMP_IF_FALSE             5060 (to 10120)
        10040   LOAD_NAME                     374: round
        10044   LOAD_NAME                     391: max
        10048   LOAD_GLOBAL                   222: entry_price
        10050   LOAD_NAME                     391: max
        10054   LOAD_GLOBAL                   222: entry_price
        10056   LOAD_GLOBAL                   242: RSI_High
        10058   BINARY_MULTIPLY               
        10060   LOAD_CONST                    73: 100
        10062   BINARY_TRUE_DIVIDE            
        10064   LOAD_GLOBAL                   106: windll
        10066   CALL_FUNCTION                 2
        10068   BINARY_SUBTRACT               
        10070   LOAD_GLOBAL                   102: now
        10072   CALL_FUNCTION                 2
        10074   LOAD_CONST                    29: 1
        10076   CALL_FUNCTION                 2
        10078   STORE_GLOBAL                  252: CE_Leg_Target
        10080   LOAD_NAME                     374: round
        10084   LOAD_NAME                     391: max
        10088   LOAD_GLOBAL                   221: NULL + strike_offset
        10090   LOAD_NAME                     391: max
        10094   LOAD_GLOBAL                   221: NULL + strike_offset
        10096   LOAD_GLOBAL                   242: RSI_High
        10098   BINARY_MULTIPLY               
        10100   LOAD_CONST                    73: 100
        10102   BINARY_TRUE_DIVIDE            
        10104   LOAD_GLOBAL                   106: windll
        10106   CALL_FUNCTION                 2
        10108   BINARY_SUBTRACT               
        10110   LOAD_GLOBAL                   102: now
        10112   CALL_FUNCTION                 2
        10114   LOAD_CONST                    29: 1
        10116   CALL_FUNCTION                 2
        10118   STORE_GLOBAL                  253: PE_Leg_Target
        10120   LOAD_NAME                     21: datetime
        10122   LOAD_ATTR                     347: date
        10126   LOAD_METHOD                   348: today
        10130   CALL_METHOD                   0
        10132   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        10136   COMPARE_OP                    3 (!=)
        10138   POP_JUMP_IF_FALSE             5103 (to 10206)
        10142   LOAD_NAME                     374: round
        10146   LOAD_GLOBAL                   222: entry_price
        10148   LOAD_NAME                     391: max
        10152   LOAD_GLOBAL                   222: entry_price
        10154   LOAD_GLOBAL                   241: NULL + RSI_Low
        10156   BINARY_MULTIPLY               
        10158   LOAD_CONST                    73: 100
        10160   BINARY_TRUE_DIVIDE            
        10162   LOAD_GLOBAL                   105: NULL + strftime
        10164   CALL_FUNCTION                 2
        10166   BINARY_ADD                    
        10168   LOAD_CONST                    29: 1
        10170   CALL_FUNCTION                 2
        10172   STORE_GLOBAL                  250: CE_Leg_SL
        10174   LOAD_NAME                     374: round
        10178   LOAD_GLOBAL                   221: NULL + strike_offset
        10180   LOAD_NAME                     391: max
        10184   LOAD_GLOBAL                   221: NULL + strike_offset
        10186   LOAD_GLOBAL                   241: NULL + RSI_Low
        10188   BINARY_MULTIPLY               
        10190   LOAD_CONST                    73: 100
        10192   BINARY_TRUE_DIVIDE            
        10194   LOAD_GLOBAL                   105: NULL + strftime
        10196   CALL_FUNCTION                 2
        10198   BINARY_ADD                    
        10200   LOAD_CONST                    29: 1
        10202   CALL_FUNCTION                 2
        10204   STORE_GLOBAL                  251: PE_Leg_SL
        10206   LOAD_NAME                     21: datetime
        10208   LOAD_ATTR                     347: date
        10212   LOAD_METHOD                   348: today
        10216   CALL_METHOD                   0
        10218   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        10222   COMPARE_OP                    2 (==)
        10224   POP_JUMP_IF_FALSE             5146 (to 10292)
        10228   LOAD_NAME                     374: round
        10232   LOAD_GLOBAL                   222: entry_price
        10234   LOAD_NAME                     391: max
        10238   LOAD_GLOBAL                   222: entry_price
        10240   LOAD_GLOBAL                   241: NULL + RSI_Low
        10242   BINARY_MULTIPLY               
        10244   LOAD_CONST                    73: 100
        10246   BINARY_TRUE_DIVIDE            
        10248   LOAD_GLOBAL                   104: strftime
        10250   CALL_FUNCTION                 2
        10252   BINARY_ADD                    
        10254   LOAD_CONST                    29: 1
        10256   CALL_FUNCTION                 2
        10258   STORE_GLOBAL                  250: CE_Leg_SL
        10260   LOAD_NAME                     374: round
        10264   LOAD_GLOBAL                   221: NULL + strike_offset
        10266   LOAD_NAME                     391: max
        10270   LOAD_GLOBAL                   221: NULL + strike_offset
        10272   LOAD_GLOBAL                   241: NULL + RSI_Low
        10274   BINARY_MULTIPLY               
        10276   LOAD_CONST                    73: 100
        10278   BINARY_TRUE_DIVIDE            
        10280   LOAD_GLOBAL                   104: strftime
        10282   CALL_FUNCTION                 2
        10284   BINARY_ADD                    
        10286   LOAD_CONST                    29: 1
        10288   CALL_FUNCTION                 2
        10290   STORE_GLOBAL                  251: PE_Leg_SL
        10292   LOAD_NAME                     369: len
        10296   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10298   CALL_FUNCTION                 1
        10300   LOAD_CONST                    0: 0
        10302   COMPARE_OP                    4 (>)
        10304   POP_JUMP_IF_FALSE             5409 (to 10818)
        10308   LOAD_GLOBAL                   81: NULL + strAdminChatID
        10310   LOAD_CONST                    29: 1
        10312   COMPARE_OP                    2 (==)
        10314   POP_JUMP_IF_TRUE              5164 (to 10328)
        10318   LOAD_GLOBAL                   83: NULL + strChatID
        10320   LOAD_CONST                    29: 1
        10322   COMPARE_OP                    2 (==)
        10324   POP_JUMP_IF_FALSE             5284 (to 10568)
        10328   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        10330   LOAD_CONST                    341: 'NQ'
        10334   BINARY_SUBSCR                 
        10336   LOAD_METHOD                   390: sum
        10340   CALL_METHOD                   0
        10342   LOAD_CONST                    0: 0
        10344   COMPARE_OP                    2 (==)
        10346   POP_JUMP_IF_FALSE             5200 (to 10400)
        10350   LOAD_NAME                     44: int
        10352   LOAD_NAME                     44: int
        10354   LOAD_CONST                    169: 50
        10356   LOAD_NAME                     4: math
        10358   LOAD_METHOD                   392: ceil
        10362   LOAD_NAME                     44: int
        10364   LOAD_NAME                     91: float
        10366   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10368   LOAD_CONST                    292: -1
        10372   BINARY_SUBSCR                 
        10374   CALL_FUNCTION                 1
        10376   CALL_FUNCTION                 1
        10378   LOAD_CONST                    169: 50
        10380   BINARY_TRUE_DIVIDE            
        10382   CALL_METHOD                   1
        10384   BINARY_MULTIPLY               
        10386   CALL_FUNCTION                 1
        10388   LOAD_GLOBAL                   108: kernel32
        10390   BINARY_ADD                    
        10392   CALL_FUNCTION                 1
        10394   STORE_NAME                    262: current_strike_ce
        10398   JUMP_FORWARD                  24 (to 10448)
        10400   LOAD_NAME                     44: int
        10402   LOAD_NAME                     44: int
        10404   LOAD_CONST                    169: 50
        10406   LOAD_NAME                     374: round
        10410   LOAD_NAME                     44: int
        10412   LOAD_NAME                     91: float
        10414   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10416   LOAD_CONST                    292: -1
        10420   BINARY_SUBSCR                 
        10422   CALL_FUNCTION                 1
        10424   CALL_FUNCTION                 1
        10426   LOAD_CONST                    169: 50
        10428   BINARY_TRUE_DIVIDE            
        10430   LOAD_CONST                    0: 0
        10432   CALL_FUNCTION                 2
        10434   BINARY_MULTIPLY               
        10436   CALL_FUNCTION                 1
        10438   LOAD_GLOBAL                   108: kernel32
        10440   BINARY_ADD                    
        10442   CALL_FUNCTION                 1
        10444   STORE_NAME                    262: current_strike_ce
        10448   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        10450   LOAD_CONST                    341: 'NQ'
        10454   BINARY_SUBSCR                 
        10456   LOAD_METHOD                   390: sum
        10460   CALL_METHOD                   0
        10462   LOAD_CONST                    0: 0
        10464   COMPARE_OP                    2 (==)
        10466   POP_JUMP_IF_FALSE             5260 (to 10520)
        10470   LOAD_NAME                     44: int
        10472   LOAD_NAME                     44: int
        10474   LOAD_CONST                    169: 50
        10476   LOAD_NAME                     4: math
        10478   LOAD_METHOD                   393: floor
        10482   LOAD_NAME                     44: int
        10484   LOAD_NAME                     91: float
        10486   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10488   LOAD_CONST                    292: -1
        10492   BINARY_SUBSCR                 
        10494   CALL_FUNCTION                 1
        10496   CALL_FUNCTION                 1
        10498   LOAD_CONST                    169: 50
        10500   BINARY_TRUE_DIVIDE            
        10502   CALL_METHOD                   1
        10504   BINARY_MULTIPLY               
        10506   CALL_FUNCTION                 1
        10508   LOAD_GLOBAL                   109: NULL + kernel32
        10510   BINARY_SUBTRACT               
        10512   CALL_FUNCTION                 1
        10514   STORE_NAME                    263: current_strike_pe
        10518   JUMP_FORWARD                  24 (to 10568)
        10520   LOAD_NAME                     44: int
        10522   LOAD_NAME                     44: int
        10524   LOAD_CONST                    169: 50
        10526   LOAD_NAME                     374: round
        10530   LOAD_NAME                     44: int
        10532   LOAD_NAME                     91: float
        10534   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10536   LOAD_CONST                    292: -1
        10540   BINARY_SUBSCR                 
        10542   CALL_FUNCTION                 1
        10544   CALL_FUNCTION                 1
        10546   LOAD_CONST                    169: 50
        10548   BINARY_TRUE_DIVIDE            
        10550   LOAD_CONST                    0: 0
        10552   CALL_FUNCTION                 2
        10554   BINARY_MULTIPLY               
        10556   CALL_FUNCTION                 1
        10558   LOAD_GLOBAL                   109: NULL + kernel32
        10560   BINARY_SUBTRACT               
        10562   CALL_FUNCTION                 1
        10564   STORE_NAME                    263: current_strike_pe
        10568   LOAD_GLOBAL                   82: strChatID
        10570   LOAD_CONST                    29: 1
        10572   COMPARE_OP                    2 (==)
        10574   POP_JUMP_IF_FALSE             5409 (to 10818)
        10578   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        10580   LOAD_CONST                    341: 'NQ'
        10584   BINARY_SUBSCR                 
        10586   LOAD_METHOD                   390: sum
        10590   CALL_METHOD                   0
        10592   LOAD_CONST                    0: 0
        10594   COMPARE_OP                    2 (==)
        10596   POP_JUMP_IF_FALSE             5325 (to 10650)
        10600   LOAD_NAME                     44: int
        10602   LOAD_NAME                     44: int
        10604   LOAD_CONST                    73: 100
        10606   LOAD_NAME                     4: math
        10608   LOAD_METHOD                   392: ceil
        10612   LOAD_NAME                     44: int
        10614   LOAD_NAME                     91: float
        10616   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10618   LOAD_CONST                    292: -1
        10622   BINARY_SUBSCR                 
        10624   CALL_FUNCTION                 1
        10626   CALL_FUNCTION                 1
        10628   LOAD_CONST                    73: 100
        10630   BINARY_TRUE_DIVIDE            
        10632   CALL_METHOD                   1
        10634   BINARY_MULTIPLY               
        10636   CALL_FUNCTION                 1
        10638   LOAD_GLOBAL                   108: kernel32
        10640   BINARY_ADD                    
        10642   CALL_FUNCTION                 1
        10644   STORE_NAME                    262: current_strike_ce
        10648   JUMP_FORWARD                  24 (to 10698)
        10650   LOAD_NAME                     44: int
        10652   LOAD_NAME                     44: int
        10654   LOAD_CONST                    73: 100
        10656   LOAD_NAME                     374: round
        10660   LOAD_NAME                     44: int
        10662   LOAD_NAME                     91: float
        10664   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10666   LOAD_CONST                    292: -1
        10670   BINARY_SUBSCR                 
        10672   CALL_FUNCTION                 1
        10674   CALL_FUNCTION                 1
        10676   LOAD_CONST                    73: 100
        10678   BINARY_TRUE_DIVIDE            
        10680   LOAD_CONST                    0: 0
        10682   CALL_FUNCTION                 2
        10684   BINARY_MULTIPLY               
        10686   CALL_FUNCTION                 1
        10688   LOAD_GLOBAL                   108: kernel32
        10690   BINARY_ADD                    
        10692   CALL_FUNCTION                 1
        10694   STORE_NAME                    262: current_strike_ce
        10698   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        10700   LOAD_CONST                    341: 'NQ'
        10704   BINARY_SUBSCR                 
        10706   LOAD_METHOD                   390: sum
        10710   CALL_METHOD                   0
        10712   LOAD_CONST                    0: 0
        10714   COMPARE_OP                    2 (==)
        10716   POP_JUMP_IF_FALSE             5385 (to 10770)
        10720   LOAD_NAME                     44: int
        10722   LOAD_NAME                     44: int
        10724   LOAD_CONST                    73: 100
        10726   LOAD_NAME                     4: math
        10728   LOAD_METHOD                   393: floor
        10732   LOAD_NAME                     44: int
        10734   LOAD_NAME                     91: float
        10736   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10738   LOAD_CONST                    292: -1
        10742   BINARY_SUBSCR                 
        10744   CALL_FUNCTION                 1
        10746   CALL_FUNCTION                 1
        10748   LOAD_CONST                    73: 100
        10750   BINARY_TRUE_DIVIDE            
        10752   CALL_METHOD                   1
        10754   BINARY_MULTIPLY               
        10756   CALL_FUNCTION                 1
        10758   LOAD_GLOBAL                   109: NULL + kernel32
        10760   BINARY_SUBTRACT               
        10762   CALL_FUNCTION                 1
        10764   STORE_NAME                    263: current_strike_pe
        10768   JUMP_FORWARD                  24 (to 10818)
        10770   LOAD_NAME                     44: int
        10772   LOAD_NAME                     44: int
        10774   LOAD_CONST                    73: 100
        10776   LOAD_NAME                     374: round
        10780   LOAD_NAME                     44: int
        10782   LOAD_NAME                     91: float
        10784   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        10786   LOAD_CONST                    292: -1
        10790   BINARY_SUBSCR                 
        10792   CALL_FUNCTION                 1
        10794   CALL_FUNCTION                 1
        10796   LOAD_CONST                    73: 100
        10798   BINARY_TRUE_DIVIDE            
        10800   LOAD_CONST                    0: 0
        10802   CALL_FUNCTION                 2
        10804   BINARY_MULTIPLY               
        10806   CALL_FUNCTION                 1
        10808   LOAD_GLOBAL                   109: NULL + kernel32
        10810   BINARY_SUBTRACT               
        10812   CALL_FUNCTION                 1
        10814   STORE_NAME                    263: current_strike_pe
        10818   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        10822   LOAD_GLOBAL                   252: ST_Close
        10824   COMPARE_OP                    0 (<)
        10826   POP_JUMP_IF_FALSE             5422 (to 10844)
        10830   LOAD_GLOBAL                   381: NULL + df_king_cnt
        10834   LOAD_NAME                     262: current_strike_ce
        10838   COMPARE_OP                    4 (>)
        10840   POP_JUMP_IF_TRUE              5428 (to 10856)
        10844   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        10848   LOAD_GLOBAL                   250: ST_Mult
        10850   COMPARE_OP                    4 (>)
        10852   POP_JUMP_IF_FALSE             5456 (to 10912)
        10856   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        10858   LOAD_CONST                    341: 'NQ'
        10862   BINARY_SUBSCR                 
        10864   LOAD_METHOD                   390: sum
        10868   CALL_METHOD                   0
        10870   LOAD_CONST                    0: 0
        10872   COMPARE_OP                    3 (!=)
        10874   POP_JUMP_IF_FALSE             5456 (to 10912)
        10878   LOAD_GLOBAL                   74: cfg
        10880   LOAD_GLOBAL                   162: Trade_Nifty
        10882   COMPARE_OP                    5 (>=)
        10884   POP_JUMP_IF_FALSE             5456 (to 10912)
        10888   LOAD_CONST                    342: ' CE Leg Stoploss/Target reached : Max order_limit_per_day Reached. Exiting trade for the day '
        10892   STORE_NAME                    65: strMsg
        10894   LOAD_NAME                     59: iLog
        10896   LOAD_NAME                     65: strMsg
        10898   LOAD_CONST                    42: 4
        10900   LOAD_CONST                    20: True
        10902   LOAD_CONST                    43: ('sendTeleMsg',)
        10904   CALL_FUNCTION_KW              3
        10906   POP_TOP                       
        10908   LOAD_CONST                    29: 1
        10910   STORE_GLOBAL                  80: ExitTradenow
        10912   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        10916   LOAD_GLOBAL                   252: ST_Close
        10918   COMPARE_OP                    0 (<)
        10920   POP_JUMP_IF_FALSE             5469 (to 10938)
        10924   LOAD_GLOBAL                   381: NULL + df_king_cnt
        10928   LOAD_NAME                     262: current_strike_ce
        10932   COMPARE_OP                    4 (>)
        10934   POP_JUMP_IF_TRUE              5475 (to 10950)
        10938   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        10942   LOAD_GLOBAL                   250: ST_Mult
        10944   COMPARE_OP                    4 (>)
        10946   POP_JUMP_IF_FALSE             5503 (to 11006)
        10950   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        10952   LOAD_CONST                    341: 'NQ'
        10956   BINARY_SUBSCR                 
        10958   LOAD_METHOD                   390: sum
        10962   CALL_METHOD                   0
        10964   LOAD_CONST                    0: 0
        10966   COMPARE_OP                    3 (!=)
        10968   POP_JUMP_IF_FALSE             5503 (to 11006)
        10972   LOAD_GLOBAL                   76: read
        10974   LOAD_GLOBAL                   90: Send_Telegram
        10976   COMPARE_OP                    5 (>=)
        10978   POP_JUMP_IF_FALSE             5503 (to 11006)
        10982   LOAD_CONST                    343: ' CE Leg Stoploss/Target reached : Position change after MaxPositionChangeTime. Exiting trade for the day '
        10986   STORE_NAME                    65: strMsg
        10988   LOAD_NAME                     59: iLog
        10990   LOAD_NAME                     65: strMsg
        10992   LOAD_CONST                    42: 4
        10994   LOAD_CONST                    20: True
        10996   LOAD_CONST                    43: ('sendTeleMsg',)
        10998   CALL_FUNCTION_KW              3
        11000   POP_TOP                       
        11002   LOAD_CONST                    29: 1
        11004   STORE_GLOBAL                  80: ExitTradenow
        11006   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11010   LOAD_GLOBAL                   252: ST_Close
        11012   COMPARE_OP                    0 (<)
        11014   POP_JUMP_IF_FALSE             5516 (to 11032)
        11018   LOAD_GLOBAL                   381: NULL + df_king_cnt
        11022   LOAD_NAME                     262: current_strike_ce
        11026   COMPARE_OP                    4 (>)
        11028   POP_JUMP_IF_TRUE              5522 (to 11044)
        11032   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11036   LOAD_GLOBAL                   250: ST_Mult
        11038   COMPARE_OP                    4 (>)
        11040   POP_JUMP_IF_FALSE             6636 (to 13272)
        11044   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        11046   LOAD_CONST                    341: 'NQ'
        11050   BINARY_SUBSCR                 
        11052   LOAD_METHOD                   390: sum
        11056   CALL_METHOD                   0
        11058   LOAD_CONST                    0: 0
        11060   COMPARE_OP                    3 (!=)
        11062   POP_JUMP_IF_FALSE             6636 (to 13272)
        11066   LOAD_GLOBAL                   76: read
        11068   LOAD_GLOBAL                   90: Send_Telegram
        11070   COMPARE_OP                    0 (<)
        11072   POP_JUMP_IF_FALSE             6636 (to 13272)
        11076   LOAD_GLOBAL                   74: cfg
        11078   LOAD_GLOBAL                   162: Trade_Nifty
        11080   COMPARE_OP                    0 (<)
        11082   POP_JUMP_IF_FALSE             6636 (to 13272)
        11086   LOAD_NAME                     375: abs
        11090   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11094   LOAD_GLOBAL                   252: ST_Close
        11096   BINARY_SUBTRACT               
        11098   CALL_FUNCTION                 1
        11100   LOAD_NAME                     375: abs
        11104   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11108   LOAD_GLOBAL                   250: ST_Mult
        11110   BINARY_SUBTRACT               
        11112   CALL_FUNCTION                 1
        11114   COMPARE_OP                    0 (<)
        11116   POP_JUMP_IF_FALSE             5602 (to 11204)
        11120   LOAD_GLOBAL                   381: NULL + df_king_cnt
        11124   LOAD_NAME                     262: current_strike_ce
        11128   COMPARE_OP                    4 (>)
        11130   POP_JUMP_IF_FALSE             5602 (to 11204)
        11134   LOAD_CONST                    344: ' CE Leg Target Reached: (Current,Target) = ('
        11138   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11142   FORMAT_VALUE                  0
        11144   LOAD_CONST                    303: ','
        11148   LOAD_GLOBAL                   252: ST_Close
        11150   FORMAT_VALUE                  0
        11152   LOAD_CONST                    345: ') Strike (Old,New) = ('
        11156   LOAD_GLOBAL                   381: NULL + df_king_cnt
        11160   FORMAT_VALUE                  0
        11162   LOAD_CONST                    303: ','
        11166   LOAD_NAME                     262: current_strike_ce
        11170   FORMAT_VALUE                  0
        11172   LOAD_CONST                    346: ') Starting New ATM CE Tick processing.'
        11176   BUILD_STRING                  9
        11178   STORE_NAME                    65: strMsg
        11180   LOAD_NAME                     59: iLog
        11182   LOAD_NAME                     65: strMsg
        11184   LOAD_CONST                    52: 2
        11186   LOAD_CONST                    20: True
        11188   LOAD_CONST                    43: ('sendTeleMsg',)
        11190   CALL_FUNCTION_KW              3
        11192   POP_TOP                       
        11194   LOAD_CONST                    20: True
        11196   STORE_NAME                    179: CE_TGT_Triggered
        11198   LOAD_CONST                    30: False
        11200   STORE_NAME                    177: CE_SL_Triggered
        11202   JUMP_FORWARD                  30 (to 11264)
        11204   LOAD_CONST                    347: ' CE Leg Stop Loss Reached: (Current,SL) = ('
        11208   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11212   FORMAT_VALUE                  0
        11214   LOAD_CONST                    303: ','
        11218   LOAD_GLOBAL                   250: ST_Mult
        11220   FORMAT_VALUE                  0
        11222   LOAD_CONST                    346: ') Starting New ATM CE Tick processing.'
        11226   BUILD_STRING                  5
        11228   STORE_NAME                    65: strMsg
        11230   LOAD_NAME                     59: iLog
        11232   LOAD_NAME                     65: strMsg
        11234   LOAD_CONST                    52: 2
        11236   LOAD_CONST                    20: True
        11238   LOAD_CONST                    43: ('sendTeleMsg',)
        11240   CALL_FUNCTION_KW              3
        11242   POP_TOP                       
        11244   LOAD_CONST                    20: True
        11246   STORE_NAME                    177: CE_SL_Triggered
        11248   LOAD_CONST                    30: False
        11250   STORE_NAME                    179: CE_TGT_Triggered
        11252   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        11254   LOAD_CONST                    292: -1
        11258   BINARY_SUBSCR                 
        11260   STORE_NAME                    298: Single_Leg_Triggered_LTP
        11264   LOAD_GLOBAL                   78: get
        11266   LOAD_CONST                    29: 1
        11268   COMPARE_OP                    2 (==)
        11270   POP_JUMP_IF_FALSE             5972 (to 11944)
        11274   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11278   STORE_GLOBAL                  222: Last_Traded_CE_Price
        11280   LOAD_CONST                    348: '  Place Buy order for Closing Existing '
        11284   LOAD_GLOBAL                   381: NULL + df_king_cnt
        11288   FORMAT_VALUE                  0
        11290   LOAD_CONST                    349: ' CE at '
        11294   LOAD_GLOBAL                   222: entry_price
        11296   FORMAT_VALUE                  0
        11298   BUILD_STRING                  4
        11300   STORE_NAME                    65: strMsg
        11302   LOAD_NAME                     59: iLog
        11304   LOAD_NAME                     65: strMsg
        11306   LOAD_CONST                    288: 5
        11310   LOAD_CONST                    20: True
        11312   LOAD_CONST                    43: ('sendTeleMsg',)
        11314   CALL_FUNCTION_KW              3
        11316   POP_TOP                       
        11318   LOAD_GLOBAL                   74: cfg
        11320   LOAD_CONST                    29: 1
        11322   BINARY_ADD                    
        11324   STORE_GLOBAL                  74: order_count
        11326   LOAD_GLOBAL                   76: read
        11328   LOAD_NAME                     376: Symbol
        11332   LOAD_GLOBAL                   381: NULL + df_king_cnt
        11336   LOAD_CONST                    315: 'CE'
        11340   LOAD_CONST                    29: 1
        11342   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        11346   LOAD_GLOBAL                   222: entry_price
        11348   LOAD_CONST                    292: -1
        11352   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        11356   BINARY_MULTIPLY               
        11358   LOAD_GLOBAL                   222: entry_price
        11360   BINARY_MULTIPLY               
        11362   BUILD_LIST                    8
        11364   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        11366   LOAD_ATTR                     379: loc
        11370   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        11372   LOAD_NAME                     191: df_cols
        11374   BUILD_TUPLE                   2
        11376   STORE_SUBSCR                  
        11378   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        11380   LOAD_CONST                    29: 1
        11382   BINARY_ADD                    
        11384   STORE_GLOBAL                  190: df_king_cnt
        11386   LOAD_GLOBAL                   76: read
        11388   LOAD_GLOBAL                   360: PE_TGT_Triggered
        11392   LOAD_CONST                    0: 0
        11394   BINARY_SUBSCR                 
        11396   LOAD_GLOBAL                   360: PE_TGT_Triggered
        11400   LOAD_CONST                    29: 1
        11402   BINARY_SUBSCR                 
        11404   LOAD_CONST                    0: 0
        11406   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        11410   BINARY_MULTIPLY               
        11412   BUILD_LIST                    4
        11414   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        11416   LOAD_ATTR                     379: loc
        11420   LOAD_CONST                    0: 0
        11422   LOAD_NAME                     197: leg_cols
        11424   BUILD_TUPLE                   2
        11426   STORE_SUBSCR                  
        11428   LOAD_NAME                     24: pd
        11430   LOAD_METHOD                   380: concat
        11434   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        11436   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        11438   BUILD_LIST                    2
        11440   CALL_METHOD                   1
        11442   STORE_GLOBAL                  200: Current_legs
        11444   LOAD_GLOBAL                   248: ST_Period
        11446   LOAD_CONST                    0: 0
        11448   COMPARE_OP                    2 (==)
        11450   POP_JUMP_IF_FALSE             5730 (to 11460)
        11454   LOAD_NAME                     177: CE_SL_Triggered
        11456   POP_JUMP_IF_TRUE              5733 (to 11466)
        11460   LOAD_NAME                     179: CE_TGT_Triggered
        11462   POP_JUMP_IF_FALSE             5972 (to 11944)
        11466   LOAD_NAME                     179: CE_TGT_Triggered
        11468   POP_JUMP_IF_FALSE             5817 (to 11634)
        11472   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        11474   LOAD_CONST                    341: 'NQ'
        11478   BINARY_SUBSCR                 
        11480   LOAD_METHOD                   390: sum
        11484   CALL_METHOD                   0
        11486   LOAD_CONST                    0: 0
        11488   COMPARE_OP                    2 (==)
        11490   POP_JUMP_IF_FALSE             5817 (to 11634)
        11494   SETUP_FINALLY                 8 (to 11512)
        11496   LOAD_NAME                     331: get_option_tokens
        11500   LOAD_CONST                    350: 'CEC'
        11504   CALL_FUNCTION                 1
        11506   POP_TOP                       
        11508   POP_BLOCK                     
        11510   JUMP_FORWARD                  130 (to 11772)
        11512   POP_TOP                       
        11514   POP_TOP                       
        11516   POP_TOP                       
        11518   LOAD_NAME                     2: time
        11520   LOAD_METHOD                   355: sleep
        11524   LOAD_CONST                    288: 5
        11528   CALL_METHOD                   1
        11530   POP_TOP                       
        11532   SETUP_FINALLY                 8 (to 11550)
        11534   LOAD_NAME                     331: get_option_tokens
        11538   LOAD_CONST                    350: 'CEC'
        11542   CALL_FUNCTION                 1
        11544   POP_TOP                       
        11546   POP_BLOCK                     
        11548   JUMP_FORWARD                  40 (to 11630)
        11550   DUP_TOP                       
        11552   LOAD_NAME                     357: Exception
        11556   JUMP_IF_NOT_EXC_MATCH         5814 (to 11628)
        11560   POP_TOP                       
        11562   STORE_NAME                    358: ex
        11566   POP_TOP                       
        11568   SETUP_FINALLY                 23 (to 11616)
        11570   LOAD_NAME                     59: iLog
        11572   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        11576   LOAD_NAME                     343: str
        11580   LOAD_NAME                     358: ex
        11584   CALL_FUNCTION                 1
        11586   BINARY_ADD                    
        11588   LOAD_CONST                    271: 3
        11592   LOAD_CONST                    20: True
        11594   LOAD_CONST                    43: ('sendTeleMsg',)
        11596   CALL_FUNCTION_KW              3
        11598   POP_TOP                       
        11600   POP_BLOCK                     
        11602   POP_EXCEPT                    
        11604   LOAD_CONST                    1: None
        11606   STORE_NAME                    358: ex
        11610   DELETE_NAME                   358: ex
        11614   JUMP_FORWARD                  7 (to 11630)
        11616   LOAD_CONST                    1: None
        11618   STORE_NAME                    358: ex
        11622   DELETE_NAME                   358: ex
        11626   RERAISE                       1
        11628   RERAISE                       0
        11630   POP_EXCEPT                    
        11632   JUMP_FORWARD                  69 (to 11772)
        11634   SETUP_FINALLY                 8 (to 11652)
        11636   LOAD_NAME                     331: get_option_tokens
        11640   LOAD_CONST                    315: 'CE'
        11644   CALL_FUNCTION                 1
        11646   POP_TOP                       
        11648   POP_BLOCK                     
        11650   JUMP_FORWARD                  60 (to 11772)
        11652   POP_TOP                       
        11654   POP_TOP                       
        11656   POP_TOP                       
        11658   LOAD_NAME                     2: time
        11660   LOAD_METHOD                   355: sleep
        11664   LOAD_CONST                    288: 5
        11668   CALL_METHOD                   1
        11670   POP_TOP                       
        11672   SETUP_FINALLY                 8 (to 11690)
        11674   LOAD_NAME                     331: get_option_tokens
        11678   LOAD_CONST                    315: 'CE'
        11682   CALL_FUNCTION                 1
        11684   POP_TOP                       
        11686   POP_BLOCK                     
        11688   JUMP_FORWARD                  40 (to 11770)
        11690   DUP_TOP                       
        11692   LOAD_NAME                     357: Exception
        11696   JUMP_IF_NOT_EXC_MATCH         5884 (to 11768)
        11700   POP_TOP                       
        11702   STORE_NAME                    358: ex
        11706   POP_TOP                       
        11708   SETUP_FINALLY                 23 (to 11756)
        11710   LOAD_NAME                     59: iLog
        11712   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        11716   LOAD_NAME                     343: str
        11720   LOAD_NAME                     358: ex
        11724   CALL_FUNCTION                 1
        11726   BINARY_ADD                    
        11728   LOAD_CONST                    271: 3
        11732   LOAD_CONST                    20: True
        11734   LOAD_CONST                    43: ('sendTeleMsg',)
        11736   CALL_FUNCTION_KW              3
        11738   POP_TOP                       
        11740   POP_BLOCK                     
        11742   POP_EXCEPT                    
        11744   LOAD_CONST                    1: None
        11746   STORE_NAME                    358: ex
        11750   DELETE_NAME                   358: ex
        11754   JUMP_FORWARD                  7 (to 11770)
        11756   LOAD_CONST                    1: None
        11758   STORE_NAME                    358: ex
        11762   DELETE_NAME                   358: ex
        11766   RERAISE                       1
        11768   RERAISE                       0
        11770   POP_EXCEPT                    
        11772   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11776   STORE_GLOBAL                  222: Last_Traded_CE_Price
        11778   LOAD_CONST                    351: '  Place SELL order for new  '
        11782   LOAD_GLOBAL                   381: NULL + df_king_cnt
        11786   FORMAT_VALUE                  0
        11788   LOAD_CONST                    349: ' CE at '
        11792   LOAD_GLOBAL                   222: entry_price
        11794   FORMAT_VALUE                  0
        11796   BUILD_STRING                  4
        11798   STORE_NAME                    65: strMsg
        11800   LOAD_NAME                     59: iLog
        11802   LOAD_NAME                     65: strMsg
        11804   LOAD_CONST                    288: 5
        11808   LOAD_CONST                    20: True
        11810   LOAD_CONST                    43: ('sendTeleMsg',)
        11812   CALL_FUNCTION_KW              3
        11814   POP_TOP                       
        11816   LOAD_GLOBAL                   74: cfg
        11818   LOAD_CONST                    29: 1
        11820   BINARY_ADD                    
        11822   STORE_GLOBAL                  74: order_count
        11824   LOAD_GLOBAL                   76: read
        11826   LOAD_NAME                     376: Symbol
        11830   LOAD_GLOBAL                   381: NULL + df_king_cnt
        11834   LOAD_CONST                    315: 'CE'
        11838   LOAD_CONST                    292: -1
        11842   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        11846   LOAD_GLOBAL                   222: entry_price
        11848   LOAD_CONST                    29: 1
        11850   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        11854   BINARY_MULTIPLY               
        11856   LOAD_GLOBAL                   222: entry_price
        11858   BINARY_MULTIPLY               
        11860   BUILD_LIST                    8
        11862   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        11864   LOAD_ATTR                     379: loc
        11868   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        11870   LOAD_NAME                     191: df_cols
        11872   BUILD_TUPLE                   2
        11874   STORE_SUBSCR                  
        11876   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        11878   LOAD_CONST                    29: 1
        11880   BINARY_ADD                    
        11882   STORE_GLOBAL                  190: df_king_cnt
        11884   LOAD_GLOBAL                   76: read
        11886   LOAD_GLOBAL                   360: PE_TGT_Triggered
        11890   LOAD_CONST                    0: 0
        11892   BINARY_SUBSCR                 
        11894   LOAD_GLOBAL                   360: PE_TGT_Triggered
        11898   LOAD_CONST                    29: 1
        11900   BINARY_SUBSCR                 
        11902   LOAD_CONST                    292: -1
        11906   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        11910   BINARY_MULTIPLY               
        11912   BUILD_LIST                    4
        11914   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        11916   LOAD_ATTR                     379: loc
        11920   LOAD_CONST                    0: 0
        11922   LOAD_NAME                     197: leg_cols
        11924   BUILD_TUPLE                   2
        11926   STORE_SUBSCR                  
        11928   LOAD_NAME                     24: pd
        11930   LOAD_METHOD                   380: concat
        11934   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        11936   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        11938   BUILD_LIST                    2
        11940   CALL_METHOD                   1
        11942   STORE_GLOBAL                  200: Current_legs
        11944   LOAD_GLOBAL                   78: get
        11946   LOAD_CONST                    0: 0
        11948   COMPARE_OP                    2 (==)
        11950   POP_JUMP_IF_FALSE             6636 (to 13272)
        11954   LOAD_NAME                     308: place_order
        11958   LOAD_CONST                    318: 'B'
        11962   LOAD_GLOBAL                   360: PE_TGT_Triggered
        11966   LOAD_CONST                    52: 2
        11968   BINARY_SUBSCR                 
        11970   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        11974   CALL_FUNCTION                 3
        11976   STORE_GLOBAL                  383: order_id_CE
        11980   LOAD_GLOBAL                   74: cfg
        11982   LOAD_CONST                    29: 1
        11984   BINARY_ADD                    
        11986   STORE_GLOBAL                  74: order_count
        11988   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        11992   STORE_GLOBAL                  222: Last_Traded_CE_Price
        11994   LOAD_GLOBAL                   383: NULL + df_cols
        11998   LOAD_CONST                    319: 'norenordno'
        12002   BINARY_SUBSCR                 
        12004   STORE_NAME                    384: order_id
        12008   LOAD_NAME                     311: get_order_symbol
        12012   LOAD_NAME                     384: order_id
        12016   CALL_FUNCTION                 1
        12018   STORE_NAME                    376: Symbol
        12022   LOAD_GLOBAL                   383: NULL + df_cols
        12026   LOAD_CONST                    320: 'stat'
        12030   BINARY_SUBSCR                 
        12032   STORE_NAME                    385: Placed_Status
        12036   LOAD_NAME                     309: get_order_status
        12040   LOAD_NAME                     384: order_id
        12044   CALL_FUNCTION                 1
        12046   STORE_NAME                    386: Return_Status
        12050   LOAD_NAME                     310: get_order_price
        12054   LOAD_NAME                     384: order_id
        12058   CALL_FUNCTION                 1
        12060   STORE_NAME                    387: average_price
        12064   LOAD_NAME                     386: Return_Status
        12068   LOAD_METHOD                   352: upper
        12072   CALL_METHOD                   0
        12074   LOAD_CONST                    321: 'REJECTED'
        12078   COMPARE_OP                    2 (==)
        12080   POP_JUMP_IF_FALSE             6088 (to 12176)
        12084   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        12088   LOAD_NAME                     384: order_id
        12092   FORMAT_VALUE                  0
        12094   LOAD_CONST                    323: ', Ord_STS = '
        12098   LOAD_NAME                     385: Placed_Status
        12102   FORMAT_VALUE                  0
        12104   LOAD_CONST                    324: ', Ret_STS = '
        12108   LOAD_NAME                     386: Return_Status
        12112   FORMAT_VALUE                  0
        12114   LOAD_CONST                    333: '.'
        12118   BUILD_STRING                  7
        12120   STORE_NAME                    65: strMsg
        12122   LOAD_NAME                     59: iLog
        12124   LOAD_NAME                     65: strMsg
        12126   LOAD_CONST                    288: 5
        12130   LOAD_CONST                    20: True
        12132   LOAD_CONST                    43: ('sendTeleMsg',)
        12134   CALL_FUNCTION_KW              3
        12136   POP_TOP                       
        12138   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        12142   STORE_NAME                    65: strMsg
        12144   LOAD_NAME                     59: iLog
        12146   LOAD_NAME                     65: strMsg
        12148   LOAD_CONST                    42: 4
        12150   LOAD_CONST                    20: True
        12152   LOAD_CONST                    43: ('sendTeleMsg',)
        12154   CALL_FUNCTION_KW              3
        12156   POP_TOP                       
        12158   LOAD_NAME                     322: close_all_orders
        12162   CALL_FUNCTION                 0
        12164   POP_TOP                       
        12166   LOAD_NAME                     0: sys
        12168   LOAD_METHOD                   344: exit
        12172   CALL_METHOD                   0
        12174   POP_TOP                       
        12176   LOAD_NAME                     387: average_price
        12180   LOAD_CONST                    0: 0
        12182   COMPARE_OP                    4 (>)
        12184   POP_JUMP_IF_FALSE             6107 (to 12214)
        12188   LOAD_NAME                     386: Return_Status
        12192   LOAD_METHOD                   352: upper
        12196   CALL_METHOD                   0
        12198   LOAD_CONST                    327: 'COMPLETE'
        12202   COMPARE_OP                    2 (==)
        12204   POP_JUMP_IF_FALSE             6107 (to 12214)
        12208   LOAD_NAME                     387: average_price
        12212   STORE_GLOBAL                  222: Last_Traded_CE_Price
        12214   LOAD_GLOBAL                   76: read
        12216   LOAD_NAME                     376: Symbol
        12220   LOAD_GLOBAL                   381: NULL + df_king_cnt
        12224   LOAD_CONST                    315: 'CE'
        12228   LOAD_CONST                    29: 1
        12230   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        12234   LOAD_GLOBAL                   222: entry_price
        12236   LOAD_CONST                    292: -1
        12240   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        12244   BINARY_MULTIPLY               
        12246   LOAD_GLOBAL                   222: entry_price
        12248   BINARY_MULTIPLY               
        12250   BUILD_LIST                    8
        12252   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        12254   LOAD_ATTR                     379: loc
        12258   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        12260   LOAD_NAME                     191: df_cols
        12262   BUILD_TUPLE                   2
        12264   STORE_SUBSCR                  
        12266   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        12268   LOAD_CONST                    29: 1
        12270   BINARY_ADD                    
        12272   STORE_GLOBAL                  190: df_king_cnt
        12274   LOAD_CONST                    352: ' Placed CE Buy Market order for ATM Strike='
        12278   LOAD_GLOBAL                   381: NULL + df_king_cnt
        12282   FORMAT_VALUE                  0
        12284   LOAD_CONST                    353: ', ATM CE='
        12288   LOAD_NAME                     387: average_price
        12292   FORMAT_VALUE                  0
        12294   LOAD_CONST                    330: ', Qty ='
        12298   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        12302   FORMAT_VALUE                  0
        12304   LOAD_CONST                    331: ', Ord_ID = '
        12308   LOAD_NAME                     384: order_id
        12312   FORMAT_VALUE                  0
        12314   LOAD_CONST                    323: ', Ord_STS = '
        12318   LOAD_NAME                     385: Placed_Status
        12322   FORMAT_VALUE                  0
        12324   LOAD_CONST                    324: ', Ret_STS = '
        12328   LOAD_NAME                     386: Return_Status
        12332   FORMAT_VALUE                  0
        12334   BUILD_STRING                  12
        12336   STORE_NAME                    65: strMsg
        12338   LOAD_NAME                     59: iLog
        12340   LOAD_NAME                     65: strMsg
        12342   LOAD_CONST                    288: 5
        12346   LOAD_CONST                    20: True
        12348   LOAD_CONST                    43: ('sendTeleMsg',)
        12350   CALL_FUNCTION_KW              3
        12352   POP_TOP                       
        12354   LOAD_GLOBAL                   76: read
        12356   LOAD_GLOBAL                   360: PE_TGT_Triggered
        12360   LOAD_CONST                    0: 0
        12362   BINARY_SUBSCR                 
        12364   LOAD_GLOBAL                   360: PE_TGT_Triggered
        12368   LOAD_CONST                    29: 1
        12370   BINARY_SUBSCR                 
        12372   LOAD_CONST                    0: 0
        12374   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        12378   BINARY_MULTIPLY               
        12380   BUILD_LIST                    4
        12382   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        12384   LOAD_ATTR                     379: loc
        12388   LOAD_CONST                    0: 0
        12390   LOAD_NAME                     197: leg_cols
        12392   BUILD_TUPLE                   2
        12394   STORE_SUBSCR                  
        12396   LOAD_NAME                     24: pd
        12398   LOAD_METHOD                   380: concat
        12402   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        12404   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        12406   BUILD_LIST                    2
        12408   CALL_METHOD                   1
        12410   STORE_GLOBAL                  200: Current_legs
        12412   LOAD_NAME                     72: tl
        12414   LOAD_METHOD                   388: update_csv
        12418   LOAD_NAME                     376: Symbol
        12422   LOAD_CONST                    332: 'Buy'
        12426   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        12430   LOAD_GLOBAL                   222: entry_price
        12432   LOAD_NAME                     384: order_id
        12436   LOAD_NAME                     385: Placed_Status
        12440   LOAD_NAME                     386: Return_Status
        12444   CALL_METHOD                   7
        12446   POP_TOP                       
        12448   LOAD_GLOBAL                   248: ST_Period
        12450   LOAD_CONST                    0: 0
        12452   COMPARE_OP                    2 (==)
        12454   POP_JUMP_IF_FALSE             6232 (to 12464)
        12458   LOAD_NAME                     177: CE_SL_Triggered
        12460   POP_JUMP_IF_TRUE              6235 (to 12470)
        12464   LOAD_NAME                     179: CE_TGT_Triggered
        12466   POP_JUMP_IF_FALSE             6636 (to 13272)
        12470   LOAD_NAME                     179: CE_TGT_Triggered
        12472   POP_JUMP_IF_FALSE             6319 (to 12638)
        12476   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        12478   LOAD_CONST                    341: 'NQ'
        12482   BINARY_SUBSCR                 
        12484   LOAD_METHOD                   390: sum
        12488   CALL_METHOD                   0
        12490   LOAD_CONST                    0: 0
        12492   COMPARE_OP                    2 (==)
        12494   POP_JUMP_IF_FALSE             6319 (to 12638)
        12498   SETUP_FINALLY                 8 (to 12516)
        12500   LOAD_NAME                     331: get_option_tokens
        12504   LOAD_CONST                    350: 'CEC'
        12508   CALL_FUNCTION                 1
        12510   POP_TOP                       
        12512   POP_BLOCK                     
        12514   JUMP_FORWARD                  130 (to 12776)
        12516   POP_TOP                       
        12518   POP_TOP                       
        12520   POP_TOP                       
        12522   LOAD_NAME                     2: time
        12524   LOAD_METHOD                   355: sleep
        12528   LOAD_CONST                    288: 5
        12532   CALL_METHOD                   1
        12534   POP_TOP                       
        12536   SETUP_FINALLY                 8 (to 12554)
        12538   LOAD_NAME                     331: get_option_tokens
        12542   LOAD_CONST                    350: 'CEC'
        12546   CALL_FUNCTION                 1
        12548   POP_TOP                       
        12550   POP_BLOCK                     
        12552   JUMP_FORWARD                  40 (to 12634)
        12554   DUP_TOP                       
        12556   LOAD_NAME                     357: Exception
        12560   JUMP_IF_NOT_EXC_MATCH         6316 (to 12632)
        12564   POP_TOP                       
        12566   STORE_NAME                    358: ex
        12570   POP_TOP                       
        12572   SETUP_FINALLY                 23 (to 12620)
        12574   LOAD_NAME                     59: iLog
        12576   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        12580   LOAD_NAME                     343: str
        12584   LOAD_NAME                     358: ex
        12588   CALL_FUNCTION                 1
        12590   BINARY_ADD                    
        12592   LOAD_CONST                    271: 3
        12596   LOAD_CONST                    20: True
        12598   LOAD_CONST                    43: ('sendTeleMsg',)
        12600   CALL_FUNCTION_KW              3
        12602   POP_TOP                       
        12604   POP_BLOCK                     
        12606   POP_EXCEPT                    
        12608   LOAD_CONST                    1: None
        12610   STORE_NAME                    358: ex
        12614   DELETE_NAME                   358: ex
        12618   JUMP_FORWARD                  7 (to 12634)
        12620   LOAD_CONST                    1: None
        12622   STORE_NAME                    358: ex
        12626   DELETE_NAME                   358: ex
        12630   RERAISE                       1
        12632   RERAISE                       0
        12634   POP_EXCEPT                    
        12636   JUMP_FORWARD                  69 (to 12776)
        12638   SETUP_FINALLY                 8 (to 12656)
        12640   LOAD_NAME                     331: get_option_tokens
        12644   LOAD_CONST                    315: 'CE'
        12648   CALL_FUNCTION                 1
        12650   POP_TOP                       
        12652   POP_BLOCK                     
        12654   JUMP_FORWARD                  60 (to 12776)
        12656   POP_TOP                       
        12658   POP_TOP                       
        12660   POP_TOP                       
        12662   LOAD_NAME                     2: time
        12664   LOAD_METHOD                   355: sleep
        12668   LOAD_CONST                    288: 5
        12672   CALL_METHOD                   1
        12674   POP_TOP                       
        12676   SETUP_FINALLY                 8 (to 12694)
        12678   LOAD_NAME                     331: get_option_tokens
        12682   LOAD_CONST                    315: 'CE'
        12686   CALL_FUNCTION                 1
        12688   POP_TOP                       
        12690   POP_BLOCK                     
        12692   JUMP_FORWARD                  40 (to 12774)
        12694   DUP_TOP                       
        12696   LOAD_NAME                     357: Exception
        12700   JUMP_IF_NOT_EXC_MATCH         6386 (to 12772)
        12704   POP_TOP                       
        12706   STORE_NAME                    358: ex
        12710   POP_TOP                       
        12712   SETUP_FINALLY                 23 (to 12760)
        12714   LOAD_NAME                     59: iLog
        12716   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        12720   LOAD_NAME                     343: str
        12724   LOAD_NAME                     358: ex
        12728   CALL_FUNCTION                 1
        12730   BINARY_ADD                    
        12732   LOAD_CONST                    271: 3
        12736   LOAD_CONST                    20: True
        12738   LOAD_CONST                    43: ('sendTeleMsg',)
        12740   CALL_FUNCTION_KW              3
        12742   POP_TOP                       
        12744   POP_BLOCK                     
        12746   POP_EXCEPT                    
        12748   LOAD_CONST                    1: None
        12750   STORE_NAME                    358: ex
        12754   DELETE_NAME                   358: ex
        12758   JUMP_FORWARD                  7 (to 12774)
        12760   LOAD_CONST                    1: None
        12762   STORE_NAME                    358: ex
        12766   DELETE_NAME                   358: ex
        12770   RERAISE                       1
        12772   RERAISE                       0
        12774   POP_EXCEPT                    
        12776   LOAD_NAME                     308: place_order
        12780   LOAD_CONST                    337: 'S'
        12784   LOAD_GLOBAL                   360: PE_TGT_Triggered
        12788   LOAD_CONST                    52: 2
        12790   BINARY_SUBSCR                 
        12792   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        12796   CALL_FUNCTION                 3
        12798   STORE_NAME                    394: order_id_CE1
        12802   LOAD_GLOBAL                   74: cfg
        12804   LOAD_CONST                    29: 1
        12806   BINARY_ADD                    
        12808   STORE_GLOBAL                  74: order_count
        12810   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        12814   STORE_GLOBAL                  222: Last_Traded_CE_Price
        12816   LOAD_NAME                     394: order_id_CE1
        12820   LOAD_CONST                    319: 'norenordno'
        12824   BINARY_SUBSCR                 
        12826   STORE_NAME                    384: order_id
        12830   LOAD_NAME                     311: get_order_symbol
        12834   LOAD_NAME                     384: order_id
        12838   CALL_FUNCTION                 1
        12840   STORE_NAME                    376: Symbol
        12844   LOAD_NAME                     394: order_id_CE1
        12848   LOAD_CONST                    320: 'stat'
        12852   BINARY_SUBSCR                 
        12854   STORE_NAME                    385: Placed_Status
        12858   LOAD_NAME                     309: get_order_status
        12862   LOAD_NAME                     384: order_id
        12866   CALL_FUNCTION                 1
        12868   STORE_NAME                    386: Return_Status
        12872   LOAD_NAME                     310: get_order_price
        12876   LOAD_NAME                     384: order_id
        12880   CALL_FUNCTION                 1
        12882   STORE_NAME                    387: average_price
        12886   LOAD_NAME                     386: Return_Status
        12890   LOAD_METHOD                   352: upper
        12894   CALL_METHOD                   0
        12896   LOAD_CONST                    321: 'REJECTED'
        12900   COMPARE_OP                    2 (==)
        12902   POP_JUMP_IF_FALSE             6499 (to 12998)
        12906   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        12910   LOAD_NAME                     384: order_id
        12914   FORMAT_VALUE                  0
        12916   LOAD_CONST                    323: ', Ord_STS = '
        12920   LOAD_NAME                     385: Placed_Status
        12924   FORMAT_VALUE                  0
        12926   LOAD_CONST                    324: ', Ret_STS = '
        12930   LOAD_NAME                     386: Return_Status
        12934   FORMAT_VALUE                  0
        12936   LOAD_CONST                    333: '.'
        12940   BUILD_STRING                  7
        12942   STORE_NAME                    65: strMsg
        12944   LOAD_NAME                     59: iLog
        12946   LOAD_NAME                     65: strMsg
        12948   LOAD_CONST                    288: 5
        12952   LOAD_CONST                    20: True
        12954   LOAD_CONST                    43: ('sendTeleMsg',)
        12956   CALL_FUNCTION_KW              3
        12958   POP_TOP                       
        12960   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        12964   STORE_NAME                    65: strMsg
        12966   LOAD_NAME                     59: iLog
        12968   LOAD_NAME                     65: strMsg
        12970   LOAD_CONST                    42: 4
        12972   LOAD_CONST                    20: True
        12974   LOAD_CONST                    43: ('sendTeleMsg',)
        12976   CALL_FUNCTION_KW              3
        12978   POP_TOP                       
        12980   LOAD_NAME                     322: close_all_orders
        12984   CALL_FUNCTION                 0
        12986   POP_TOP                       
        12988   LOAD_NAME                     0: sys
        12990   LOAD_METHOD                   344: exit
        12994   CALL_METHOD                   0
        12996   POP_TOP                       
        12998   LOAD_NAME                     387: average_price
        13002   LOAD_CONST                    0: 0
        13004   COMPARE_OP                    4 (>)
        13006   POP_JUMP_IF_FALSE             6518 (to 13036)
        13010   LOAD_NAME                     386: Return_Status
        13014   LOAD_METHOD                   352: upper
        13018   CALL_METHOD                   0
        13020   LOAD_CONST                    327: 'COMPLETE'
        13024   COMPARE_OP                    2 (==)
        13026   POP_JUMP_IF_FALSE             6518 (to 13036)
        13030   LOAD_NAME                     387: average_price
        13034   STORE_GLOBAL                  222: Last_Traded_CE_Price
        13036   LOAD_GLOBAL                   76: read
        13038   LOAD_NAME                     376: Symbol
        13042   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13046   LOAD_CONST                    315: 'CE'
        13050   LOAD_CONST                    292: -1
        13054   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        13058   LOAD_GLOBAL                   222: entry_price
        13060   LOAD_CONST                    29: 1
        13062   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        13066   BINARY_MULTIPLY               
        13068   LOAD_GLOBAL                   222: entry_price
        13070   BINARY_MULTIPLY               
        13072   BUILD_LIST                    8
        13074   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        13076   LOAD_ATTR                     379: loc
        13080   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        13082   LOAD_NAME                     191: df_cols
        13084   BUILD_TUPLE                   2
        13086   STORE_SUBSCR                  
        13088   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        13090   LOAD_CONST                    29: 1
        13092   BINARY_ADD                    
        13094   STORE_GLOBAL                  190: df_king_cnt
        13096   LOAD_CONST                    354: ' Placed CE Sell Market order for ATM Strike='
        13100   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13104   FORMAT_VALUE                  0
        13106   LOAD_CONST                    353: ', ATM CE='
        13110   LOAD_NAME                     387: average_price
        13114   FORMAT_VALUE                  0
        13116   LOAD_CONST                    330: ', Qty ='
        13120   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        13124   FORMAT_VALUE                  0
        13126   LOAD_CONST                    331: ', Ord_ID = '
        13130   LOAD_NAME                     384: order_id
        13134   FORMAT_VALUE                  0
        13136   LOAD_CONST                    323: ', Ord_STS = '
        13140   LOAD_NAME                     385: Placed_Status
        13144   FORMAT_VALUE                  0
        13146   LOAD_CONST                    324: ', Ret_STS = '
        13150   LOAD_NAME                     386: Return_Status
        13154   FORMAT_VALUE                  0
        13156   BUILD_STRING                  12
        13158   STORE_NAME                    65: strMsg
        13160   LOAD_NAME                     59: iLog
        13162   LOAD_NAME                     65: strMsg
        13164   LOAD_CONST                    288: 5
        13168   LOAD_CONST                    20: True
        13170   LOAD_CONST                    43: ('sendTeleMsg',)
        13172   CALL_FUNCTION_KW              3
        13174   POP_TOP                       
        13176   LOAD_NAME                     72: tl
        13178   LOAD_METHOD                   388: update_csv
        13182   LOAD_NAME                     376: Symbol
        13186   LOAD_CONST                    339: 'Sell'
        13190   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        13194   LOAD_GLOBAL                   222: entry_price
        13196   LOAD_NAME                     384: order_id
        13200   LOAD_NAME                     385: Placed_Status
        13204   LOAD_NAME                     386: Return_Status
        13208   CALL_METHOD                   7
        13210   POP_TOP                       
        13212   LOAD_GLOBAL                   76: read
        13214   LOAD_GLOBAL                   360: PE_TGT_Triggered
        13218   LOAD_CONST                    0: 0
        13220   BINARY_SUBSCR                 
        13222   LOAD_GLOBAL                   360: PE_TGT_Triggered
        13226   LOAD_CONST                    29: 1
        13228   BINARY_SUBSCR                 
        13230   LOAD_CONST                    292: -1
        13234   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        13238   BINARY_MULTIPLY               
        13240   BUILD_LIST                    4
        13242   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        13244   LOAD_ATTR                     379: loc
        13248   LOAD_CONST                    0: 0
        13250   LOAD_NAME                     197: leg_cols
        13252   BUILD_TUPLE                   2
        13254   STORE_SUBSCR                  
        13256   LOAD_NAME                     24: pd
        13258   LOAD_METHOD                   380: concat
        13262   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        13264   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        13266   BUILD_LIST                    2
        13268   CALL_METHOD                   1
        13270   STORE_GLOBAL                  200: Current_legs
        13272   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        13276   LOAD_CONST                    0: 0
        13278   COMPARE_OP                    2 (==)
        13280   POP_JUMP_IF_FALSE             6734 (to 13468)
        13284   LOAD_GLOBAL                   248: ST_Period
        13286   LOAD_CONST                    29: 1
        13288   COMPARE_OP                    2 (==)
        13290   POP_JUMP_IF_FALSE             6734 (to 13468)
        13294   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        13296   LOAD_CONST                    341: 'NQ'
        13300   BINARY_SUBSCR                 
        13302   LOAD_METHOD                   390: sum
        13306   CALL_METHOD                   0
        13308   LOAD_CONST                    0: 0
        13310   COMPARE_OP                    2 (==)
        13312   POP_JUMP_IF_FALSE             6734 (to 13468)
        13316   LOAD_NAME                     44: int
        13318   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13320   LOAD_CONST                    292: -1
        13324   BINARY_SUBSCR                 
        13326   CALL_FUNCTION                 1
        13328   LOAD_GLOBAL                   108: kernel32
        13330   BINARY_ADD                    
        13332   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13336   LOAD_GLOBAL                   157: NULL + papertrade
        13338   BINARY_SUBTRACT               
        13340   COMPARE_OP                    0 (<)
        13342   POP_JUMP_IF_TRUE              6717 (to 13434)
        13346   LOAD_NAME                     44: int
        13348   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13350   LOAD_CONST                    292: -1
        13354   BINARY_SUBSCR                 
        13356   CALL_FUNCTION                 1
        13358   LOAD_GLOBAL                   109: NULL + kernel32
        13360   BINARY_SUBTRACT               
        13362   LOAD_GLOBAL                   382: df_cols
        13366   LOAD_GLOBAL                   157: NULL + papertrade
        13368   BINARY_SUBTRACT               
        13370   COMPARE_OP                    0 (<)
        13372   POP_JUMP_IF_TRUE              6717 (to 13434)
        13376   LOAD_NAME                     44: int
        13378   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13380   LOAD_CONST                    292: -1
        13384   BINARY_SUBSCR                 
        13386   LOAD_GLOBAL                   108: kernel32
        13388   BINARY_ADD                    
        13390   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13394   BINARY_SUBTRACT               
        13396   CALL_FUNCTION                 1
        13398   LOAD_NAME                     44: int
        13400   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        13404   LOAD_GLOBAL                   108: kernel32
        13406   BINARY_ADD                    
        13408   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13412   BINARY_SUBTRACT               
        13414   CALL_FUNCTION                 1
        13416   LOAD_CONST                    73: 100
        13418   LOAD_GLOBAL                   249: NULL + ST_Period
        13420   BINARY_SUBTRACT               
        13422   BINARY_MULTIPLY               
        13424   LOAD_CONST                    73: 100
        13426   BINARY_TRUE_DIVIDE            
        13428   COMPARE_OP                    0 (<)
        13430   POP_JUMP_IF_FALSE             6734 (to 13468)
        13434   LOAD_GLOBAL                   74: cfg
        13436   LOAD_GLOBAL                   162: Trade_Nifty
        13438   COMPARE_OP                    5 (>=)
        13440   POP_JUMP_IF_FALSE             6734 (to 13468)
        13444   LOAD_CONST                    355: ' CE Leg Re-entry Triggered : Max order_limit_per_day Reached. Exiting trade for the day '
        13448   STORE_NAME                    65: strMsg
        13450   LOAD_NAME                     59: iLog
        13452   LOAD_NAME                     65: strMsg
        13454   LOAD_CONST                    42: 4
        13456   LOAD_CONST                    20: True
        13458   LOAD_CONST                    43: ('sendTeleMsg',)
        13460   CALL_FUNCTION_KW              3
        13462   POP_TOP                       
        13464   LOAD_CONST                    29: 1
        13466   STORE_GLOBAL                  80: ExitTradenow
        13468   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        13472   LOAD_CONST                    0: 0
        13474   COMPARE_OP                    2 (==)
        13476   POP_JUMP_IF_FALSE             6832 (to 13664)
        13480   LOAD_GLOBAL                   248: ST_Period
        13482   LOAD_CONST                    29: 1
        13484   COMPARE_OP                    2 (==)
        13486   POP_JUMP_IF_FALSE             6832 (to 13664)
        13490   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        13492   LOAD_CONST                    341: 'NQ'
        13496   BINARY_SUBSCR                 
        13498   LOAD_METHOD                   390: sum
        13502   CALL_METHOD                   0
        13504   LOAD_CONST                    0: 0
        13506   COMPARE_OP                    2 (==)
        13508   POP_JUMP_IF_FALSE             6832 (to 13664)
        13512   LOAD_NAME                     44: int
        13514   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13516   LOAD_CONST                    292: -1
        13520   BINARY_SUBSCR                 
        13522   CALL_FUNCTION                 1
        13524   LOAD_GLOBAL                   108: kernel32
        13526   BINARY_ADD                    
        13528   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13532   LOAD_GLOBAL                   157: NULL + papertrade
        13534   BINARY_SUBTRACT               
        13536   COMPARE_OP                    0 (<)
        13538   POP_JUMP_IF_TRUE              6815 (to 13630)
        13542   LOAD_NAME                     44: int
        13544   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13546   LOAD_CONST                    292: -1
        13550   BINARY_SUBSCR                 
        13552   CALL_FUNCTION                 1
        13554   LOAD_GLOBAL                   109: NULL + kernel32
        13556   BINARY_SUBTRACT               
        13558   LOAD_GLOBAL                   382: df_cols
        13562   LOAD_GLOBAL                   157: NULL + papertrade
        13564   BINARY_SUBTRACT               
        13566   COMPARE_OP                    0 (<)
        13568   POP_JUMP_IF_TRUE              6815 (to 13630)
        13572   LOAD_NAME                     44: int
        13574   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13576   LOAD_CONST                    292: -1
        13580   BINARY_SUBSCR                 
        13582   LOAD_GLOBAL                   108: kernel32
        13584   BINARY_ADD                    
        13586   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13590   BINARY_SUBTRACT               
        13592   CALL_FUNCTION                 1
        13594   LOAD_NAME                     44: int
        13596   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        13600   LOAD_GLOBAL                   108: kernel32
        13602   BINARY_ADD                    
        13604   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13608   BINARY_SUBTRACT               
        13610   CALL_FUNCTION                 1
        13612   LOAD_CONST                    73: 100
        13614   LOAD_GLOBAL                   249: NULL + ST_Period
        13616   BINARY_SUBTRACT               
        13618   BINARY_MULTIPLY               
        13620   LOAD_CONST                    73: 100
        13622   BINARY_TRUE_DIVIDE            
        13624   COMPARE_OP                    0 (<)
        13626   POP_JUMP_IF_FALSE             6832 (to 13664)
        13630   LOAD_GLOBAL                   76: read
        13632   LOAD_GLOBAL                   90: Send_Telegram
        13634   COMPARE_OP                    5 (>=)
        13636   POP_JUMP_IF_FALSE             6832 (to 13664)
        13640   LOAD_CONST                    356: ' CE Leg Re-entry Triggered : Position change after MaxPositionChangeTime. Exiting trade for the day '
        13644   STORE_NAME                    65: strMsg
        13646   LOAD_NAME                     59: iLog
        13648   LOAD_NAME                     65: strMsg
        13650   LOAD_CONST                    42: 4
        13652   LOAD_CONST                    20: True
        13654   LOAD_CONST                    43: ('sendTeleMsg',)
        13656   CALL_FUNCTION_KW              3
        13658   POP_TOP                       
        13660   LOAD_CONST                    29: 1
        13662   STORE_GLOBAL                  80: ExitTradenow
        13664   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        13668   LOAD_CONST                    0: 0
        13670   COMPARE_OP                    2 (==)
        13672   POP_JUMP_IF_FALSE             7627 (to 15254)
        13676   LOAD_GLOBAL                   248: ST_Period
        13678   LOAD_CONST                    29: 1
        13680   COMPARE_OP                    2 (==)
        13682   POP_JUMP_IF_FALSE             7627 (to 15254)
        13686   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        13688   LOAD_CONST                    341: 'NQ'
        13692   BINARY_SUBSCR                 
        13694   LOAD_METHOD                   390: sum
        13698   CALL_METHOD                   0
        13700   LOAD_CONST                    0: 0
        13702   COMPARE_OP                    2 (==)
        13704   POP_JUMP_IF_FALSE             7627 (to 15254)
        13708   LOAD_NAME                     44: int
        13710   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13712   LOAD_CONST                    292: -1
        13716   BINARY_SUBSCR                 
        13718   CALL_FUNCTION                 1
        13720   LOAD_GLOBAL                   108: kernel32
        13722   BINARY_ADD                    
        13724   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13728   LOAD_GLOBAL                   157: NULL + papertrade
        13730   BINARY_SUBTRACT               
        13732   COMPARE_OP                    0 (<)
        13734   POP_JUMP_IF_TRUE              6913 (to 13826)
        13738   LOAD_NAME                     44: int
        13740   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13742   LOAD_CONST                    292: -1
        13746   BINARY_SUBSCR                 
        13748   CALL_FUNCTION                 1
        13750   LOAD_GLOBAL                   109: NULL + kernel32
        13752   BINARY_SUBTRACT               
        13754   LOAD_GLOBAL                   382: df_cols
        13758   LOAD_GLOBAL                   157: NULL + papertrade
        13760   BINARY_SUBTRACT               
        13762   COMPARE_OP                    0 (<)
        13764   POP_JUMP_IF_TRUE              6913 (to 13826)
        13768   LOAD_NAME                     44: int
        13770   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13772   LOAD_CONST                    292: -1
        13776   BINARY_SUBSCR                 
        13778   LOAD_GLOBAL                   108: kernel32
        13780   BINARY_ADD                    
        13782   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13786   BINARY_SUBTRACT               
        13788   CALL_FUNCTION                 1
        13790   LOAD_NAME                     44: int
        13792   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        13796   LOAD_GLOBAL                   108: kernel32
        13798   BINARY_ADD                    
        13800   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13804   BINARY_SUBTRACT               
        13806   CALL_FUNCTION                 1
        13808   LOAD_CONST                    73: 100
        13810   LOAD_GLOBAL                   249: NULL + ST_Period
        13812   BINARY_SUBTRACT               
        13814   BINARY_MULTIPLY               
        13816   LOAD_CONST                    73: 100
        13818   BINARY_TRUE_DIVIDE            
        13820   COMPARE_OP                    0 (<)
        13822   POP_JUMP_IF_FALSE             7627 (to 15254)
        13826   LOAD_GLOBAL                   76: read
        13828   LOAD_GLOBAL                   90: Send_Telegram
        13830   COMPARE_OP                    0 (<)
        13832   POP_JUMP_IF_FALSE             7627 (to 15254)
        13836   LOAD_GLOBAL                   74: cfg
        13838   LOAD_GLOBAL                   162: Trade_Nifty
        13840   COMPARE_OP                    0 (<)
        13842   POP_JUMP_IF_FALSE             7627 (to 15254)
        13846   LOAD_CONST                    357: ' CE Leg Re-entry triggered (LTP,ATM_CE_Strike,ATM_PE_Strike,Delta_Limit,Actual_Delta): ('
        13850   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13852   LOAD_CONST                    292: -1
        13856   BINARY_SUBSCR                 
        13858   FORMAT_VALUE                  0
        13860   LOAD_CONST                    303: ','
        13864   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13868   FORMAT_VALUE                  0
        13870   LOAD_CONST                    303: ','
        13874   LOAD_GLOBAL                   382: df_cols
        13878   FORMAT_VALUE                  0
        13880   LOAD_CONST                    303: ','
        13884   LOAD_NAME                     44: int
        13886   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        13890   LOAD_GLOBAL                   108: kernel32
        13892   BINARY_ADD                    
        13894   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13898   BINARY_SUBTRACT               
        13900   CALL_FUNCTION                 1
        13902   LOAD_CONST                    73: 100
        13904   LOAD_GLOBAL                   249: NULL + ST_Period
        13906   BINARY_SUBTRACT               
        13908   BINARY_MULTIPLY               
        13910   LOAD_CONST                    73: 100
        13912   BINARY_TRUE_DIVIDE            
        13914   FORMAT_VALUE                  0
        13916   LOAD_CONST                    303: ','
        13920   LOAD_NAME                     44: int
        13922   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        13924   LOAD_CONST                    292: -1
        13928   BINARY_SUBSCR                 
        13930   LOAD_GLOBAL                   108: kernel32
        13932   BINARY_ADD                    
        13934   LOAD_GLOBAL                   381: NULL + df_king_cnt
        13938   BINARY_SUBTRACT               
        13940   CALL_FUNCTION                 1
        13942   FORMAT_VALUE                  0
        13944   LOAD_CONST                    305: ')'
        13948   BUILD_STRING                  11
        13950   STORE_NAME                    65: strMsg
        13952   LOAD_NAME                     59: iLog
        13954   LOAD_NAME                     65: strMsg
        13956   LOAD_CONST                    52: 2
        13958   LOAD_CONST                    20: True
        13960   LOAD_CONST                    43: ('sendTeleMsg',)
        13962   CALL_FUNCTION_KW              3
        13964   POP_TOP                       
        13966   LOAD_GLOBAL                   78: get
        13968   LOAD_CONST                    29: 1
        13970   COMPARE_OP                    2 (==)
        13972   POP_JUMP_IF_FALSE             7224 (to 14448)
        13976   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        13978   LOAD_CONST                    341: 'NQ'
        13982   BINARY_SUBSCR                 
        13984   LOAD_METHOD                   390: sum
        13988   CALL_METHOD                   0
        13990   LOAD_CONST                    0: 0
        13992   COMPARE_OP                    2 (==)
        13994   POP_JUMP_IF_FALSE             7069 (to 14138)
        13998   SETUP_FINALLY                 8 (to 14016)
        14000   LOAD_NAME                     331: get_option_tokens
        14004   LOAD_CONST                    350: 'CEC'
        14008   CALL_FUNCTION                 1
        14010   POP_TOP                       
        14012   POP_BLOCK                     
        14014   JUMP_FORWARD                  130 (to 14276)
        14016   POP_TOP                       
        14018   POP_TOP                       
        14020   POP_TOP                       
        14022   LOAD_NAME                     2: time
        14024   LOAD_METHOD                   355: sleep
        14028   LOAD_CONST                    288: 5
        14032   CALL_METHOD                   1
        14034   POP_TOP                       
        14036   SETUP_FINALLY                 8 (to 14054)
        14038   LOAD_NAME                     331: get_option_tokens
        14042   LOAD_CONST                    350: 'CEC'
        14046   CALL_FUNCTION                 1
        14048   POP_TOP                       
        14050   POP_BLOCK                     
        14052   JUMP_FORWARD                  40 (to 14134)
        14054   DUP_TOP                       
        14056   LOAD_NAME                     357: Exception
        14060   JUMP_IF_NOT_EXC_MATCH         7066 (to 14132)
        14064   POP_TOP                       
        14066   STORE_NAME                    358: ex
        14070   POP_TOP                       
        14072   SETUP_FINALLY                 23 (to 14120)
        14074   LOAD_NAME                     59: iLog
        14076   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        14080   LOAD_NAME                     343: str
        14084   LOAD_NAME                     358: ex
        14088   CALL_FUNCTION                 1
        14090   BINARY_ADD                    
        14092   LOAD_CONST                    271: 3
        14096   LOAD_CONST                    20: True
        14098   LOAD_CONST                    43: ('sendTeleMsg',)
        14100   CALL_FUNCTION_KW              3
        14102   POP_TOP                       
        14104   POP_BLOCK                     
        14106   POP_EXCEPT                    
        14108   LOAD_CONST                    1: None
        14110   STORE_NAME                    358: ex
        14114   DELETE_NAME                   358: ex
        14118   JUMP_FORWARD                  7 (to 14134)
        14120   LOAD_CONST                    1: None
        14122   STORE_NAME                    358: ex
        14126   DELETE_NAME                   358: ex
        14130   RERAISE                       1
        14132   RERAISE                       0
        14134   POP_EXCEPT                    
        14136   JUMP_FORWARD                  69 (to 14276)
        14138   SETUP_FINALLY                 8 (to 14156)
        14140   LOAD_NAME                     331: get_option_tokens
        14144   LOAD_CONST                    315: 'CE'
        14148   CALL_FUNCTION                 1
        14150   POP_TOP                       
        14152   POP_BLOCK                     
        14154   JUMP_FORWARD                  60 (to 14276)
        14156   POP_TOP                       
        14158   POP_TOP                       
        14160   POP_TOP                       
        14162   LOAD_NAME                     2: time
        14164   LOAD_METHOD                   355: sleep
        14168   LOAD_CONST                    288: 5
        14172   CALL_METHOD                   1
        14174   POP_TOP                       
        14176   SETUP_FINALLY                 8 (to 14194)
        14178   LOAD_NAME                     331: get_option_tokens
        14182   LOAD_CONST                    315: 'CE'
        14186   CALL_FUNCTION                 1
        14188   POP_TOP                       
        14190   POP_BLOCK                     
        14192   JUMP_FORWARD                  40 (to 14274)
        14194   DUP_TOP                       
        14196   LOAD_NAME                     357: Exception
        14200   JUMP_IF_NOT_EXC_MATCH         7136 (to 14272)
        14204   POP_TOP                       
        14206   STORE_NAME                    358: ex
        14210   POP_TOP                       
        14212   SETUP_FINALLY                 23 (to 14260)
        14214   LOAD_NAME                     59: iLog
        14216   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        14220   LOAD_NAME                     343: str
        14224   LOAD_NAME                     358: ex
        14228   CALL_FUNCTION                 1
        14230   BINARY_ADD                    
        14232   LOAD_CONST                    271: 3
        14236   LOAD_CONST                    20: True
        14238   LOAD_CONST                    43: ('sendTeleMsg',)
        14240   CALL_FUNCTION_KW              3
        14242   POP_TOP                       
        14244   POP_BLOCK                     
        14246   POP_EXCEPT                    
        14248   LOAD_CONST                    1: None
        14250   STORE_NAME                    358: ex
        14254   DELETE_NAME                   358: ex
        14258   JUMP_FORWARD                  7 (to 14274)
        14260   LOAD_CONST                    1: None
        14262   STORE_NAME                    358: ex
        14266   DELETE_NAME                   358: ex
        14270   RERAISE                       1
        14272   RERAISE                       0
        14274   POP_EXCEPT                    
        14276   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        14280   STORE_GLOBAL                  222: Last_Traded_CE_Price
        14282   LOAD_CONST                    358: '  Place SELL order for  '
        14286   LOAD_GLOBAL                   381: NULL + df_king_cnt
        14290   FORMAT_VALUE                  0
        14292   LOAD_CONST                    349: ' CE at '
        14296   LOAD_GLOBAL                   222: entry_price
        14298   FORMAT_VALUE                  0
        14300   BUILD_STRING                  4
        14302   STORE_NAME                    65: strMsg
        14304   LOAD_NAME                     59: iLog
        14306   LOAD_NAME                     65: strMsg
        14308   LOAD_CONST                    288: 5
        14312   LOAD_CONST                    20: True
        14314   LOAD_CONST                    43: ('sendTeleMsg',)
        14316   CALL_FUNCTION_KW              3
        14318   POP_TOP                       
        14320   LOAD_GLOBAL                   74: cfg
        14322   LOAD_CONST                    29: 1
        14324   BINARY_ADD                    
        14326   STORE_GLOBAL                  74: order_count
        14328   LOAD_GLOBAL                   76: read
        14330   LOAD_NAME                     376: Symbol
        14334   LOAD_GLOBAL                   381: NULL + df_king_cnt
        14338   LOAD_CONST                    315: 'CE'
        14342   LOAD_CONST                    292: -1
        14346   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        14350   LOAD_GLOBAL                   222: entry_price
        14352   LOAD_CONST                    29: 1
        14354   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        14358   BINARY_MULTIPLY               
        14360   LOAD_GLOBAL                   222: entry_price
        14362   BINARY_MULTIPLY               
        14364   BUILD_LIST                    8
        14366   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        14368   LOAD_ATTR                     379: loc
        14372   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        14374   LOAD_NAME                     191: df_cols
        14376   BUILD_TUPLE                   2
        14378   STORE_SUBSCR                  
        14380   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        14382   LOAD_CONST                    29: 1
        14384   BINARY_ADD                    
        14386   STORE_GLOBAL                  190: df_king_cnt
        14388   LOAD_GLOBAL                   76: read
        14390   LOAD_GLOBAL                   360: PE_TGT_Triggered
        14394   LOAD_CONST                    0: 0
        14396   BINARY_SUBSCR                 
        14398   LOAD_GLOBAL                   360: PE_TGT_Triggered
        14402   LOAD_CONST                    29: 1
        14404   BINARY_SUBSCR                 
        14406   LOAD_CONST                    292: -1
        14410   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        14414   BINARY_MULTIPLY               
        14416   BUILD_LIST                    4
        14418   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        14420   LOAD_ATTR                     379: loc
        14424   LOAD_CONST                    0: 0
        14426   LOAD_NAME                     197: leg_cols
        14428   BUILD_TUPLE                   2
        14430   STORE_SUBSCR                  
        14432   LOAD_NAME                     24: pd
        14434   LOAD_METHOD                   380: concat
        14438   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        14440   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        14442   BUILD_LIST                    2
        14444   CALL_METHOD                   1
        14446   STORE_GLOBAL                  200: Current_legs
        14448   LOAD_GLOBAL                   78: get
        14450   LOAD_CONST                    0: 0
        14452   COMPARE_OP                    2 (==)
        14454   POP_JUMP_IF_FALSE             7627 (to 15254)
        14458   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        14460   LOAD_CONST                    341: 'NQ'
        14464   BINARY_SUBSCR                 
        14466   LOAD_METHOD                   390: sum
        14470   CALL_METHOD                   0
        14472   LOAD_CONST                    0: 0
        14474   COMPARE_OP                    2 (==)
        14476   POP_JUMP_IF_FALSE             7310 (to 14620)
        14480   SETUP_FINALLY                 8 (to 14498)
        14482   LOAD_NAME                     331: get_option_tokens
        14486   LOAD_CONST                    350: 'CEC'
        14490   CALL_FUNCTION                 1
        14492   POP_TOP                       
        14494   POP_BLOCK                     
        14496   JUMP_FORWARD                  130 (to 14758)
        14498   POP_TOP                       
        14500   POP_TOP                       
        14502   POP_TOP                       
        14504   LOAD_NAME                     2: time
        14506   LOAD_METHOD                   355: sleep
        14510   LOAD_CONST                    288: 5
        14514   CALL_METHOD                   1
        14516   POP_TOP                       
        14518   SETUP_FINALLY                 8 (to 14536)
        14520   LOAD_NAME                     331: get_option_tokens
        14524   LOAD_CONST                    350: 'CEC'
        14528   CALL_FUNCTION                 1
        14530   POP_TOP                       
        14532   POP_BLOCK                     
        14534   JUMP_FORWARD                  40 (to 14616)
        14536   DUP_TOP                       
        14538   LOAD_NAME                     357: Exception
        14542   JUMP_IF_NOT_EXC_MATCH         7307 (to 14614)
        14546   POP_TOP                       
        14548   STORE_NAME                    358: ex
        14552   POP_TOP                       
        14554   SETUP_FINALLY                 23 (to 14602)
        14556   LOAD_NAME                     59: iLog
        14558   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        14562   LOAD_NAME                     343: str
        14566   LOAD_NAME                     358: ex
        14570   CALL_FUNCTION                 1
        14572   BINARY_ADD                    
        14574   LOAD_CONST                    271: 3
        14578   LOAD_CONST                    20: True
        14580   LOAD_CONST                    43: ('sendTeleMsg',)
        14582   CALL_FUNCTION_KW              3
        14584   POP_TOP                       
        14586   POP_BLOCK                     
        14588   POP_EXCEPT                    
        14590   LOAD_CONST                    1: None
        14592   STORE_NAME                    358: ex
        14596   DELETE_NAME                   358: ex
        14600   JUMP_FORWARD                  7 (to 14616)
        14602   LOAD_CONST                    1: None
        14604   STORE_NAME                    358: ex
        14608   DELETE_NAME                   358: ex
        14612   RERAISE                       1
        14614   RERAISE                       0
        14616   POP_EXCEPT                    
        14618   JUMP_FORWARD                  69 (to 14758)
        14620   SETUP_FINALLY                 8 (to 14638)
        14622   LOAD_NAME                     331: get_option_tokens
        14626   LOAD_CONST                    315: 'CE'
        14630   CALL_FUNCTION                 1
        14632   POP_TOP                       
        14634   POP_BLOCK                     
        14636   JUMP_FORWARD                  60 (to 14758)
        14638   POP_TOP                       
        14640   POP_TOP                       
        14642   POP_TOP                       
        14644   LOAD_NAME                     2: time
        14646   LOAD_METHOD                   355: sleep
        14650   LOAD_CONST                    288: 5
        14654   CALL_METHOD                   1
        14656   POP_TOP                       
        14658   SETUP_FINALLY                 8 (to 14676)
        14660   LOAD_NAME                     331: get_option_tokens
        14664   LOAD_CONST                    315: 'CE'
        14668   CALL_FUNCTION                 1
        14670   POP_TOP                       
        14672   POP_BLOCK                     
        14674   JUMP_FORWARD                  40 (to 14756)
        14676   DUP_TOP                       
        14678   LOAD_NAME                     357: Exception
        14682   JUMP_IF_NOT_EXC_MATCH         7377 (to 14754)
        14686   POP_TOP                       
        14688   STORE_NAME                    358: ex
        14692   POP_TOP                       
        14694   SETUP_FINALLY                 23 (to 14742)
        14696   LOAD_NAME                     59: iLog
        14698   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        14702   LOAD_NAME                     343: str
        14706   LOAD_NAME                     358: ex
        14710   CALL_FUNCTION                 1
        14712   BINARY_ADD                    
        14714   LOAD_CONST                    271: 3
        14718   LOAD_CONST                    20: True
        14720   LOAD_CONST                    43: ('sendTeleMsg',)
        14722   CALL_FUNCTION_KW              3
        14724   POP_TOP                       
        14726   POP_BLOCK                     
        14728   POP_EXCEPT                    
        14730   LOAD_CONST                    1: None
        14732   STORE_NAME                    358: ex
        14736   DELETE_NAME                   358: ex
        14740   JUMP_FORWARD                  7 (to 14756)
        14742   LOAD_CONST                    1: None
        14744   STORE_NAME                    358: ex
        14748   DELETE_NAME                   358: ex
        14752   RERAISE                       1
        14754   RERAISE                       0
        14756   POP_EXCEPT                    
        14758   LOAD_NAME                     308: place_order
        14762   LOAD_CONST                    337: 'S'
        14766   LOAD_GLOBAL                   360: PE_TGT_Triggered
        14770   LOAD_CONST                    52: 2
        14772   BINARY_SUBSCR                 
        14774   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        14778   CALL_FUNCTION                 3
        14780   STORE_NAME                    394: order_id_CE1
        14784   LOAD_GLOBAL                   74: cfg
        14786   LOAD_CONST                    29: 1
        14788   BINARY_ADD                    
        14790   STORE_GLOBAL                  74: order_count
        14792   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        14796   STORE_GLOBAL                  222: Last_Traded_CE_Price
        14798   LOAD_NAME                     394: order_id_CE1
        14802   LOAD_CONST                    319: 'norenordno'
        14806   BINARY_SUBSCR                 
        14808   STORE_NAME                    384: order_id
        14812   LOAD_NAME                     311: get_order_symbol
        14816   LOAD_NAME                     384: order_id
        14820   CALL_FUNCTION                 1
        14822   STORE_NAME                    376: Symbol
        14826   LOAD_NAME                     394: order_id_CE1
        14830   LOAD_CONST                    320: 'stat'
        14834   BINARY_SUBSCR                 
        14836   STORE_NAME                    385: Placed_Status
        14840   LOAD_NAME                     309: get_order_status
        14844   LOAD_NAME                     384: order_id
        14848   CALL_FUNCTION                 1
        14850   STORE_NAME                    386: Return_Status
        14854   LOAD_NAME                     310: get_order_price
        14858   LOAD_NAME                     384: order_id
        14862   CALL_FUNCTION                 1
        14864   STORE_NAME                    387: average_price
        14868   LOAD_NAME                     386: Return_Status
        14872   LOAD_METHOD                   352: upper
        14876   CALL_METHOD                   0
        14878   LOAD_CONST                    321: 'REJECTED'
        14882   COMPARE_OP                    2 (==)
        14884   POP_JUMP_IF_FALSE             7490 (to 14980)
        14888   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        14892   LOAD_NAME                     384: order_id
        14896   FORMAT_VALUE                  0
        14898   LOAD_CONST                    323: ', Ord_STS = '
        14902   LOAD_NAME                     385: Placed_Status
        14906   FORMAT_VALUE                  0
        14908   LOAD_CONST                    324: ', Ret_STS = '
        14912   LOAD_NAME                     386: Return_Status
        14916   FORMAT_VALUE                  0
        14918   LOAD_CONST                    333: '.'
        14922   BUILD_STRING                  7
        14924   STORE_NAME                    65: strMsg
        14926   LOAD_NAME                     59: iLog
        14928   LOAD_NAME                     65: strMsg
        14930   LOAD_CONST                    288: 5
        14934   LOAD_CONST                    20: True
        14936   LOAD_CONST                    43: ('sendTeleMsg',)
        14938   CALL_FUNCTION_KW              3
        14940   POP_TOP                       
        14942   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        14946   STORE_NAME                    65: strMsg
        14948   LOAD_NAME                     59: iLog
        14950   LOAD_NAME                     65: strMsg
        14952   LOAD_CONST                    42: 4
        14954   LOAD_CONST                    20: True
        14956   LOAD_CONST                    43: ('sendTeleMsg',)
        14958   CALL_FUNCTION_KW              3
        14960   POP_TOP                       
        14962   LOAD_NAME                     322: close_all_orders
        14966   CALL_FUNCTION                 0
        14968   POP_TOP                       
        14970   LOAD_NAME                     0: sys
        14972   LOAD_METHOD                   344: exit
        14976   CALL_METHOD                   0
        14978   POP_TOP                       
        14980   LOAD_NAME                     387: average_price
        14984   LOAD_CONST                    0: 0
        14986   COMPARE_OP                    4 (>)
        14988   POP_JUMP_IF_FALSE             7509 (to 15018)
        14992   LOAD_NAME                     386: Return_Status
        14996   LOAD_METHOD                   352: upper
        15000   CALL_METHOD                   0
        15002   LOAD_CONST                    327: 'COMPLETE'
        15006   COMPARE_OP                    2 (==)
        15008   POP_JUMP_IF_FALSE             7509 (to 15018)
        15012   LOAD_NAME                     387: average_price
        15016   STORE_GLOBAL                  222: Last_Traded_CE_Price
        15018   LOAD_GLOBAL                   76: read
        15020   LOAD_NAME                     376: Symbol
        15024   LOAD_GLOBAL                   381: NULL + df_king_cnt
        15028   LOAD_CONST                    315: 'CE'
        15032   LOAD_CONST                    292: -1
        15036   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        15040   LOAD_GLOBAL                   222: entry_price
        15042   LOAD_CONST                    29: 1
        15044   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        15048   BINARY_MULTIPLY               
        15050   LOAD_GLOBAL                   222: entry_price
        15052   BINARY_MULTIPLY               
        15054   BUILD_LIST                    8
        15056   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        15058   LOAD_ATTR                     379: loc
        15062   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        15064   LOAD_NAME                     191: df_cols
        15066   BUILD_TUPLE                   2
        15068   STORE_SUBSCR                  
        15070   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        15072   LOAD_CONST                    29: 1
        15074   BINARY_ADD                    
        15076   STORE_GLOBAL                  190: df_king_cnt
        15078   LOAD_CONST                    354: ' Placed CE Sell Market order for ATM Strike='
        15082   LOAD_GLOBAL                   381: NULL + df_king_cnt
        15086   FORMAT_VALUE                  0
        15088   LOAD_CONST                    353: ', ATM CE='
        15092   LOAD_NAME                     387: average_price
        15096   FORMAT_VALUE                  0
        15098   LOAD_CONST                    330: ', Qty ='
        15102   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        15106   FORMAT_VALUE                  0
        15108   LOAD_CONST                    331: ', Ord_ID = '
        15112   LOAD_NAME                     384: order_id
        15116   FORMAT_VALUE                  0
        15118   LOAD_CONST                    323: ', Ord_STS = '
        15122   LOAD_NAME                     385: Placed_Status
        15126   FORMAT_VALUE                  0
        15128   LOAD_CONST                    324: ', Ret_STS = '
        15132   LOAD_NAME                     386: Return_Status
        15136   FORMAT_VALUE                  0
        15138   BUILD_STRING                  12
        15140   STORE_NAME                    65: strMsg
        15142   LOAD_NAME                     59: iLog
        15144   LOAD_NAME                     65: strMsg
        15146   LOAD_CONST                    288: 5
        15150   LOAD_CONST                    20: True
        15152   LOAD_CONST                    43: ('sendTeleMsg',)
        15154   CALL_FUNCTION_KW              3
        15156   POP_TOP                       
        15158   LOAD_NAME                     72: tl
        15160   LOAD_METHOD                   388: update_csv
        15164   LOAD_NAME                     376: Symbol
        15168   LOAD_CONST                    339: 'Sell'
        15172   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        15176   LOAD_GLOBAL                   222: entry_price
        15178   LOAD_NAME                     384: order_id
        15182   LOAD_NAME                     385: Placed_Status
        15186   LOAD_NAME                     386: Return_Status
        15190   CALL_METHOD                   7
        15192   POP_TOP                       
        15194   LOAD_GLOBAL                   76: read
        15196   LOAD_GLOBAL                   360: PE_TGT_Triggered
        15200   LOAD_CONST                    0: 0
        15202   BINARY_SUBSCR                 
        15204   LOAD_GLOBAL                   360: PE_TGT_Triggered
        15208   LOAD_CONST                    29: 1
        15210   BINARY_SUBSCR                 
        15212   LOAD_CONST                    292: -1
        15216   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        15220   BINARY_MULTIPLY               
        15222   BUILD_LIST                    4
        15224   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        15226   LOAD_ATTR                     379: loc
        15230   LOAD_CONST                    0: 0
        15232   LOAD_NAME                     197: leg_cols
        15234   BUILD_TUPLE                   2
        15236   STORE_SUBSCR                  
        15238   LOAD_NAME                     24: pd
        15240   LOAD_METHOD                   380: concat
        15244   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        15246   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        15248   BUILD_LIST                    2
        15250   CALL_METHOD                   1
        15252   STORE_GLOBAL                  200: Current_legs
        15254   LOAD_NAME                     369: len
        15258   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15260   CALL_FUNCTION                 1
        15262   LOAD_CONST                    0: 0
        15264   COMPARE_OP                    4 (>)
        15266   POP_JUMP_IF_FALSE             7890 (to 15780)
        15270   LOAD_GLOBAL                   81: NULL + strAdminChatID
        15272   LOAD_CONST                    29: 1
        15274   COMPARE_OP                    2 (==)
        15276   POP_JUMP_IF_TRUE              7645 (to 15290)
        15280   LOAD_GLOBAL                   83: NULL + strChatID
        15282   LOAD_CONST                    29: 1
        15284   COMPARE_OP                    2 (==)
        15286   POP_JUMP_IF_FALSE             7765 (to 15530)
        15290   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        15292   LOAD_CONST                    341: 'NQ'
        15296   BINARY_SUBSCR                 
        15298   LOAD_METHOD                   390: sum
        15302   CALL_METHOD                   0
        15304   LOAD_CONST                    0: 0
        15306   COMPARE_OP                    2 (==)
        15308   POP_JUMP_IF_FALSE             7681 (to 15362)
        15312   LOAD_NAME                     44: int
        15314   LOAD_NAME                     44: int
        15316   LOAD_CONST                    169: 50
        15318   LOAD_NAME                     4: math
        15320   LOAD_METHOD                   392: ceil
        15324   LOAD_NAME                     44: int
        15326   LOAD_NAME                     91: float
        15328   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15330   LOAD_CONST                    292: -1
        15334   BINARY_SUBSCR                 
        15336   CALL_FUNCTION                 1
        15338   CALL_FUNCTION                 1
        15340   LOAD_CONST                    169: 50
        15342   BINARY_TRUE_DIVIDE            
        15344   CALL_METHOD                   1
        15346   BINARY_MULTIPLY               
        15348   CALL_FUNCTION                 1
        15350   LOAD_GLOBAL                   108: kernel32
        15352   BINARY_ADD                    
        15354   CALL_FUNCTION                 1
        15356   STORE_NAME                    262: current_strike_ce
        15360   JUMP_FORWARD                  24 (to 15410)
        15362   LOAD_NAME                     44: int
        15364   LOAD_NAME                     44: int
        15366   LOAD_CONST                    169: 50
        15368   LOAD_NAME                     374: round
        15372   LOAD_NAME                     44: int
        15374   LOAD_NAME                     91: float
        15376   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15378   LOAD_CONST                    292: -1
        15382   BINARY_SUBSCR                 
        15384   CALL_FUNCTION                 1
        15386   CALL_FUNCTION                 1
        15388   LOAD_CONST                    169: 50
        15390   BINARY_TRUE_DIVIDE            
        15392   LOAD_CONST                    0: 0
        15394   CALL_FUNCTION                 2
        15396   BINARY_MULTIPLY               
        15398   CALL_FUNCTION                 1
        15400   LOAD_GLOBAL                   108: kernel32
        15402   BINARY_ADD                    
        15404   CALL_FUNCTION                 1
        15406   STORE_NAME                    262: current_strike_ce
        15410   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        15412   LOAD_CONST                    341: 'NQ'
        15416   BINARY_SUBSCR                 
        15418   LOAD_METHOD                   390: sum
        15422   CALL_METHOD                   0
        15424   LOAD_CONST                    0: 0
        15426   COMPARE_OP                    2 (==)
        15428   POP_JUMP_IF_FALSE             7741 (to 15482)
        15432   LOAD_NAME                     44: int
        15434   LOAD_NAME                     44: int
        15436   LOAD_CONST                    169: 50
        15438   LOAD_NAME                     4: math
        15440   LOAD_METHOD                   393: floor
        15444   LOAD_NAME                     44: int
        15446   LOAD_NAME                     91: float
        15448   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15450   LOAD_CONST                    292: -1
        15454   BINARY_SUBSCR                 
        15456   CALL_FUNCTION                 1
        15458   CALL_FUNCTION                 1
        15460   LOAD_CONST                    169: 50
        15462   BINARY_TRUE_DIVIDE            
        15464   CALL_METHOD                   1
        15466   BINARY_MULTIPLY               
        15468   CALL_FUNCTION                 1
        15470   LOAD_GLOBAL                   109: NULL + kernel32
        15472   BINARY_SUBTRACT               
        15474   CALL_FUNCTION                 1
        15476   STORE_NAME                    263: current_strike_pe
        15480   JUMP_FORWARD                  24 (to 15530)
        15482   LOAD_NAME                     44: int
        15484   LOAD_NAME                     44: int
        15486   LOAD_CONST                    169: 50
        15488   LOAD_NAME                     374: round
        15492   LOAD_NAME                     44: int
        15494   LOAD_NAME                     91: float
        15496   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15498   LOAD_CONST                    292: -1
        15502   BINARY_SUBSCR                 
        15504   CALL_FUNCTION                 1
        15506   CALL_FUNCTION                 1
        15508   LOAD_CONST                    169: 50
        15510   BINARY_TRUE_DIVIDE            
        15512   LOAD_CONST                    0: 0
        15514   CALL_FUNCTION                 2
        15516   BINARY_MULTIPLY               
        15518   CALL_FUNCTION                 1
        15520   LOAD_GLOBAL                   109: NULL + kernel32
        15522   BINARY_SUBTRACT               
        15524   CALL_FUNCTION                 1
        15526   STORE_NAME                    263: current_strike_pe
        15530   LOAD_GLOBAL                   82: strChatID
        15532   LOAD_CONST                    29: 1
        15534   COMPARE_OP                    2 (==)
        15536   POP_JUMP_IF_FALSE             7890 (to 15780)
        15540   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        15542   LOAD_CONST                    341: 'NQ'
        15546   BINARY_SUBSCR                 
        15548   LOAD_METHOD                   390: sum
        15552   CALL_METHOD                   0
        15554   LOAD_CONST                    0: 0
        15556   COMPARE_OP                    2 (==)
        15558   POP_JUMP_IF_FALSE             7806 (to 15612)
        15562   LOAD_NAME                     44: int
        15564   LOAD_NAME                     44: int
        15566   LOAD_CONST                    73: 100
        15568   LOAD_NAME                     4: math
        15570   LOAD_METHOD                   392: ceil
        15574   LOAD_NAME                     44: int
        15576   LOAD_NAME                     91: float
        15578   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15580   LOAD_CONST                    292: -1
        15584   BINARY_SUBSCR                 
        15586   CALL_FUNCTION                 1
        15588   CALL_FUNCTION                 1
        15590   LOAD_CONST                    73: 100
        15592   BINARY_TRUE_DIVIDE            
        15594   CALL_METHOD                   1
        15596   BINARY_MULTIPLY               
        15598   CALL_FUNCTION                 1
        15600   LOAD_GLOBAL                   108: kernel32
        15602   BINARY_ADD                    
        15604   CALL_FUNCTION                 1
        15606   STORE_NAME                    262: current_strike_ce
        15610   JUMP_FORWARD                  24 (to 15660)
        15612   LOAD_NAME                     44: int
        15614   LOAD_NAME                     44: int
        15616   LOAD_CONST                    73: 100
        15618   LOAD_NAME                     374: round
        15622   LOAD_NAME                     44: int
        15624   LOAD_NAME                     91: float
        15626   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15628   LOAD_CONST                    292: -1
        15632   BINARY_SUBSCR                 
        15634   CALL_FUNCTION                 1
        15636   CALL_FUNCTION                 1
        15638   LOAD_CONST                    73: 100
        15640   BINARY_TRUE_DIVIDE            
        15642   LOAD_CONST                    0: 0
        15644   CALL_FUNCTION                 2
        15646   BINARY_MULTIPLY               
        15648   CALL_FUNCTION                 1
        15650   LOAD_GLOBAL                   108: kernel32
        15652   BINARY_ADD                    
        15654   CALL_FUNCTION                 1
        15656   STORE_NAME                    262: current_strike_ce
        15660   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        15662   LOAD_CONST                    341: 'NQ'
        15666   BINARY_SUBSCR                 
        15668   LOAD_METHOD                   390: sum
        15672   CALL_METHOD                   0
        15674   LOAD_CONST                    0: 0
        15676   COMPARE_OP                    2 (==)
        15678   POP_JUMP_IF_FALSE             7866 (to 15732)
        15682   LOAD_NAME                     44: int
        15684   LOAD_NAME                     44: int
        15686   LOAD_CONST                    73: 100
        15688   LOAD_NAME                     4: math
        15690   LOAD_METHOD                   393: floor
        15694   LOAD_NAME                     44: int
        15696   LOAD_NAME                     91: float
        15698   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15700   LOAD_CONST                    292: -1
        15704   BINARY_SUBSCR                 
        15706   CALL_FUNCTION                 1
        15708   CALL_FUNCTION                 1
        15710   LOAD_CONST                    73: 100
        15712   BINARY_TRUE_DIVIDE            
        15714   CALL_METHOD                   1
        15716   BINARY_MULTIPLY               
        15718   CALL_FUNCTION                 1
        15720   LOAD_GLOBAL                   109: NULL + kernel32
        15722   BINARY_SUBTRACT               
        15724   CALL_FUNCTION                 1
        15726   STORE_NAME                    263: current_strike_pe
        15730   JUMP_FORWARD                  24 (to 15780)
        15732   LOAD_NAME                     44: int
        15734   LOAD_NAME                     44: int
        15736   LOAD_CONST                    73: 100
        15738   LOAD_NAME                     374: round
        15742   LOAD_NAME                     44: int
        15744   LOAD_NAME                     91: float
        15746   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        15748   LOAD_CONST                    292: -1
        15752   BINARY_SUBSCR                 
        15754   CALL_FUNCTION                 1
        15756   CALL_FUNCTION                 1
        15758   LOAD_CONST                    73: 100
        15760   BINARY_TRUE_DIVIDE            
        15762   LOAD_CONST                    0: 0
        15764   CALL_FUNCTION                 2
        15766   BINARY_MULTIPLY               
        15768   CALL_FUNCTION                 1
        15770   LOAD_GLOBAL                   109: NULL + kernel32
        15772   BINARY_SUBTRACT               
        15774   CALL_FUNCTION                 1
        15776   STORE_NAME                    263: current_strike_pe
        15780   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        15784   LOAD_GLOBAL                   253: NULL + ST_Close
        15786   COMPARE_OP                    0 (<)
        15788   POP_JUMP_IF_FALSE             7903 (to 15806)
        15792   LOAD_GLOBAL                   382: df_cols
        15796   LOAD_NAME                     263: current_strike_pe
        15800   COMPARE_OP                    0 (<)
        15802   POP_JUMP_IF_TRUE              7909 (to 15818)
        15806   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        15810   LOAD_GLOBAL                   251: NULL + ST_Mult
        15812   COMPARE_OP                    4 (>)
        15814   POP_JUMP_IF_FALSE             7937 (to 15874)
        15818   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        15820   LOAD_CONST                    341: 'NQ'
        15824   BINARY_SUBSCR                 
        15826   LOAD_METHOD                   390: sum
        15830   CALL_METHOD                   0
        15832   LOAD_CONST                    0: 0
        15834   COMPARE_OP                    3 (!=)
        15836   POP_JUMP_IF_FALSE             7937 (to 15874)
        15840   LOAD_GLOBAL                   74: cfg
        15842   LOAD_GLOBAL                   162: Trade_Nifty
        15844   COMPARE_OP                    5 (>=)
        15846   POP_JUMP_IF_FALSE             7937 (to 15874)
        15850   LOAD_CONST                    359: ' PE Leg Stoploss/Target reached : Max order_limit_per_day Reached. Exiting trade for the day '
        15854   STORE_NAME                    65: strMsg
        15856   LOAD_NAME                     59: iLog
        15858   LOAD_NAME                     65: strMsg
        15860   LOAD_CONST                    42: 4
        15862   LOAD_CONST                    20: True
        15864   LOAD_CONST                    43: ('sendTeleMsg',)
        15866   CALL_FUNCTION_KW              3
        15868   POP_TOP                       
        15870   LOAD_CONST                    29: 1
        15872   STORE_GLOBAL                  80: ExitTradenow
        15874   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        15878   LOAD_GLOBAL                   253: NULL + ST_Close
        15880   COMPARE_OP                    0 (<)
        15882   POP_JUMP_IF_FALSE             7950 (to 15900)
        15886   LOAD_GLOBAL                   382: df_cols
        15890   LOAD_NAME                     263: current_strike_pe
        15894   COMPARE_OP                    0 (<)
        15896   POP_JUMP_IF_TRUE              7956 (to 15912)
        15900   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        15904   LOAD_GLOBAL                   251: NULL + ST_Mult
        15906   COMPARE_OP                    4 (>)
        15908   POP_JUMP_IF_FALSE             7984 (to 15968)
        15912   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        15914   LOAD_CONST                    341: 'NQ'
        15918   BINARY_SUBSCR                 
        15920   LOAD_METHOD                   390: sum
        15924   CALL_METHOD                   0
        15926   LOAD_CONST                    0: 0
        15928   COMPARE_OP                    3 (!=)
        15930   POP_JUMP_IF_FALSE             7984 (to 15968)
        15934   LOAD_GLOBAL                   76: read
        15936   LOAD_GLOBAL                   90: Send_Telegram
        15938   COMPARE_OP                    5 (>=)
        15940   POP_JUMP_IF_FALSE             7984 (to 15968)
        15944   LOAD_CONST                    360: ' PE Leg Stoploss/Target reached : Position change after MaxPositionChangeTime. Exiting trade for the day '
        15948   STORE_NAME                    65: strMsg
        15950   LOAD_NAME                     59: iLog
        15952   LOAD_NAME                     65: strMsg
        15954   LOAD_CONST                    42: 4
        15956   LOAD_CONST                    20: True
        15958   LOAD_CONST                    43: ('sendTeleMsg',)
        15960   CALL_FUNCTION_KW              3
        15962   POP_TOP                       
        15964   LOAD_CONST                    29: 1
        15966   STORE_GLOBAL                  80: ExitTradenow
        15968   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        15972   LOAD_GLOBAL                   253: NULL + ST_Close
        15974   COMPARE_OP                    0 (<)
        15976   POP_JUMP_IF_FALSE             7997 (to 15994)
        15980   LOAD_GLOBAL                   382: df_cols
        15984   LOAD_NAME                     263: current_strike_pe
        15988   COMPARE_OP                    0 (<)
        15990   POP_JUMP_IF_TRUE              8003 (to 16006)
        15994   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        15998   LOAD_GLOBAL                   251: NULL + ST_Mult
        16000   COMPARE_OP                    4 (>)
        16002   POP_JUMP_IF_FALSE             9121 (to 18242)
        16006   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        16008   LOAD_CONST                    341: 'NQ'
        16012   BINARY_SUBSCR                 
        16014   LOAD_METHOD                   390: sum
        16018   CALL_METHOD                   0
        16020   LOAD_CONST                    0: 0
        16022   COMPARE_OP                    3 (!=)
        16024   POP_JUMP_IF_FALSE             9121 (to 18242)
        16028   LOAD_GLOBAL                   76: read
        16030   LOAD_GLOBAL                   90: Send_Telegram
        16032   COMPARE_OP                    0 (<)
        16034   POP_JUMP_IF_FALSE             9121 (to 18242)
        16038   LOAD_GLOBAL                   74: cfg
        16040   LOAD_GLOBAL                   162: Trade_Nifty
        16042   COMPARE_OP                    0 (<)
        16044   POP_JUMP_IF_FALSE             9121 (to 18242)
        16048   LOAD_NAME                     375: abs
        16052   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        16056   LOAD_GLOBAL                   253: NULL + ST_Close
        16058   BINARY_SUBTRACT               
        16060   CALL_FUNCTION                 1
        16062   LOAD_NAME                     375: abs
        16066   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        16070   LOAD_GLOBAL                   251: NULL + ST_Mult
        16072   BINARY_SUBTRACT               
        16074   CALL_FUNCTION                 1
        16076   COMPARE_OP                    0 (<)
        16078   POP_JUMP_IF_FALSE             8083 (to 16166)
        16082   LOAD_GLOBAL                   382: df_cols
        16086   LOAD_NAME                     263: current_strike_pe
        16090   COMPARE_OP                    0 (<)
        16092   POP_JUMP_IF_FALSE             8083 (to 16166)
        16096   LOAD_CONST                    361: ' PE Leg Target Reached: (Current,Target) =  ('
        16100   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        16104   FORMAT_VALUE                  0
        16106   LOAD_CONST                    303: ','
        16110   LOAD_GLOBAL                   253: NULL + ST_Close
        16112   FORMAT_VALUE                  0
        16114   LOAD_CONST                    345: ') Strike (Old,New) = ('
        16118   LOAD_GLOBAL                   382: df_cols
        16122   FORMAT_VALUE                  0
        16124   LOAD_CONST                    303: ','
        16128   LOAD_NAME                     263: current_strike_pe
        16132   FORMAT_VALUE                  0
        16134   LOAD_CONST                    314: ') '
        16138   BUILD_STRING                  9
        16140   STORE_NAME                    65: strMsg
        16142   LOAD_NAME                     59: iLog
        16144   LOAD_NAME                     65: strMsg
        16146   LOAD_CONST                    52: 2
        16148   LOAD_CONST                    20: True
        16150   LOAD_CONST                    43: ('sendTeleMsg',)
        16152   CALL_FUNCTION_KW              3
        16154   POP_TOP                       
        16156   LOAD_CONST                    20: True
        16158   STORE_NAME                    180: PE_TGT_Triggered
        16160   LOAD_CONST                    30: False
        16162   STORE_NAME                    178: PE_SL_Triggered
        16164   JUMP_FORWARD                  30 (to 16226)
        16166   LOAD_CONST                    362: ' PE Leg Stoploss Reached: (Current,SL) =  ('
        16170   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        16174   FORMAT_VALUE                  0
        16176   LOAD_CONST                    303: ','
        16180   LOAD_GLOBAL                   251: NULL + ST_Mult
        16182   FORMAT_VALUE                  0
        16184   LOAD_CONST                    305: ')'
        16188   BUILD_STRING                  5
        16190   STORE_NAME                    65: strMsg
        16192   LOAD_NAME                     59: iLog
        16194   LOAD_NAME                     65: strMsg
        16196   LOAD_CONST                    52: 2
        16198   LOAD_CONST                    20: True
        16200   LOAD_CONST                    43: ('sendTeleMsg',)
        16202   CALL_FUNCTION_KW              3
        16204   POP_TOP                       
        16206   LOAD_CONST                    20: True
        16208   STORE_NAME                    178: PE_SL_Triggered
        16210   LOAD_CONST                    30: False
        16212   STORE_NAME                    180: PE_TGT_Triggered
        16214   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        16216   LOAD_CONST                    292: -1
        16220   BINARY_SUBSCR                 
        16222   STORE_NAME                    298: Single_Leg_Triggered_LTP
        16226   LOAD_GLOBAL                   78: get
        16228   LOAD_CONST                    29: 1
        16230   COMPARE_OP                    2 (==)
        16232   POP_JUMP_IF_FALSE             8453 (to 16906)
        16236   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        16240   STORE_GLOBAL                  221: Last_Traded_PE_Price
        16242   LOAD_CONST                    348: '  Place Buy order for Closing Existing '
        16246   LOAD_GLOBAL                   382: df_cols
        16250   FORMAT_VALUE                  0
        16252   LOAD_CONST                    363: ' PE at '
        16256   LOAD_GLOBAL                   221: NULL + strike_offset
        16258   FORMAT_VALUE                  0
        16260   BUILD_STRING                  4
        16262   STORE_NAME                    65: strMsg
        16264   LOAD_NAME                     59: iLog
        16266   LOAD_NAME                     65: strMsg
        16268   LOAD_CONST                    288: 5
        16272   LOAD_CONST                    20: True
        16274   LOAD_CONST                    43: ('sendTeleMsg',)
        16276   CALL_FUNCTION_KW              3
        16278   POP_TOP                       
        16280   LOAD_GLOBAL                   74: cfg
        16282   LOAD_CONST                    29: 1
        16284   BINARY_ADD                    
        16286   STORE_GLOBAL                  74: order_count
        16288   LOAD_GLOBAL                   76: read
        16290   LOAD_NAME                     376: Symbol
        16294   LOAD_GLOBAL                   382: df_cols
        16298   LOAD_CONST                    316: 'PE'
        16302   LOAD_CONST                    29: 1
        16304   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        16308   LOAD_GLOBAL                   221: NULL + strike_offset
        16310   LOAD_CONST                    292: -1
        16314   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        16318   BINARY_MULTIPLY               
        16320   LOAD_GLOBAL                   221: NULL + strike_offset
        16322   BINARY_MULTIPLY               
        16324   BUILD_LIST                    8
        16326   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        16328   LOAD_ATTR                     379: loc
        16332   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        16334   LOAD_NAME                     191: df_cols
        16336   BUILD_TUPLE                   2
        16338   STORE_SUBSCR                  
        16340   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        16342   LOAD_CONST                    29: 1
        16344   BINARY_ADD                    
        16346   STORE_GLOBAL                  190: df_king_cnt
        16348   LOAD_GLOBAL                   76: read
        16350   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        16354   LOAD_CONST                    0: 0
        16356   BINARY_SUBSCR                 
        16358   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        16362   LOAD_CONST                    29: 1
        16364   BINARY_SUBSCR                 
        16366   LOAD_CONST                    0: 0
        16368   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        16372   BINARY_MULTIPLY               
        16374   BUILD_LIST                    4
        16376   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        16378   LOAD_ATTR                     379: loc
        16382   LOAD_CONST                    0: 0
        16384   LOAD_NAME                     197: leg_cols
        16386   BUILD_TUPLE                   2
        16388   STORE_SUBSCR                  
        16390   LOAD_NAME                     24: pd
        16392   LOAD_METHOD                   380: concat
        16396   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        16398   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        16400   BUILD_LIST                    2
        16402   CALL_METHOD                   1
        16404   STORE_GLOBAL                  200: Current_legs
        16406   LOAD_GLOBAL                   248: ST_Period
        16408   LOAD_CONST                    0: 0
        16410   COMPARE_OP                    2 (==)
        16412   POP_JUMP_IF_FALSE             8211 (to 16422)
        16416   LOAD_NAME                     178: PE_SL_Triggered
        16418   POP_JUMP_IF_TRUE              8214 (to 16428)
        16422   LOAD_NAME                     180: PE_TGT_Triggered
        16424   POP_JUMP_IF_FALSE             8453 (to 16906)
        16428   LOAD_NAME                     180: PE_TGT_Triggered
        16430   POP_JUMP_IF_FALSE             8298 (to 16596)
        16434   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        16436   LOAD_CONST                    341: 'NQ'
        16440   BINARY_SUBSCR                 
        16442   LOAD_METHOD                   390: sum
        16446   CALL_METHOD                   0
        16448   LOAD_CONST                    0: 0
        16450   COMPARE_OP                    2 (==)
        16452   POP_JUMP_IF_FALSE             8298 (to 16596)
        16456   SETUP_FINALLY                 8 (to 16474)
        16458   LOAD_NAME                     331: get_option_tokens
        16462   LOAD_CONST                    364: 'PEF'
        16466   CALL_FUNCTION                 1
        16468   POP_TOP                       
        16470   POP_BLOCK                     
        16472   JUMP_FORWARD                  130 (to 16734)
        16474   POP_TOP                       
        16476   POP_TOP                       
        16478   POP_TOP                       
        16480   LOAD_NAME                     2: time
        16482   LOAD_METHOD                   355: sleep
        16486   LOAD_CONST                    288: 5
        16490   CALL_METHOD                   1
        16492   POP_TOP                       
        16494   SETUP_FINALLY                 8 (to 16512)
        16496   LOAD_NAME                     331: get_option_tokens
        16500   LOAD_CONST                    364: 'PEF'
        16504   CALL_FUNCTION                 1
        16506   POP_TOP                       
        16508   POP_BLOCK                     
        16510   JUMP_FORWARD                  40 (to 16592)
        16512   DUP_TOP                       
        16514   LOAD_NAME                     357: Exception
        16518   JUMP_IF_NOT_EXC_MATCH         8295 (to 16590)
        16522   POP_TOP                       
        16524   STORE_NAME                    358: ex
        16528   POP_TOP                       
        16530   SETUP_FINALLY                 23 (to 16578)
        16532   LOAD_NAME                     59: iLog
        16534   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        16538   LOAD_NAME                     343: str
        16542   LOAD_NAME                     358: ex
        16546   CALL_FUNCTION                 1
        16548   BINARY_ADD                    
        16550   LOAD_CONST                    271: 3
        16554   LOAD_CONST                    20: True
        16556   LOAD_CONST                    43: ('sendTeleMsg',)
        16558   CALL_FUNCTION_KW              3
        16560   POP_TOP                       
        16562   POP_BLOCK                     
        16564   POP_EXCEPT                    
        16566   LOAD_CONST                    1: None
        16568   STORE_NAME                    358: ex
        16572   DELETE_NAME                   358: ex
        16576   JUMP_FORWARD                  7 (to 16592)
        16578   LOAD_CONST                    1: None
        16580   STORE_NAME                    358: ex
        16584   DELETE_NAME                   358: ex
        16588   RERAISE                       1
        16590   RERAISE                       0
        16592   POP_EXCEPT                    
        16594   JUMP_FORWARD                  69 (to 16734)
        16596   SETUP_FINALLY                 8 (to 16614)
        16598   LOAD_NAME                     331: get_option_tokens
        16602   LOAD_CONST                    316: 'PE'
        16606   CALL_FUNCTION                 1
        16608   POP_TOP                       
        16610   POP_BLOCK                     
        16612   JUMP_FORWARD                  60 (to 16734)
        16614   POP_TOP                       
        16616   POP_TOP                       
        16618   POP_TOP                       
        16620   LOAD_NAME                     2: time
        16622   LOAD_METHOD                   355: sleep
        16626   LOAD_CONST                    288: 5
        16630   CALL_METHOD                   1
        16632   POP_TOP                       
        16634   SETUP_FINALLY                 8 (to 16652)
        16636   LOAD_NAME                     331: get_option_tokens
        16640   LOAD_CONST                    316: 'PE'
        16644   CALL_FUNCTION                 1
        16646   POP_TOP                       
        16648   POP_BLOCK                     
        16650   JUMP_FORWARD                  40 (to 16732)
        16652   DUP_TOP                       
        16654   LOAD_NAME                     357: Exception
        16658   JUMP_IF_NOT_EXC_MATCH         8365 (to 16730)
        16662   POP_TOP                       
        16664   STORE_NAME                    358: ex
        16668   POP_TOP                       
        16670   SETUP_FINALLY                 23 (to 16718)
        16672   LOAD_NAME                     59: iLog
        16674   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        16678   LOAD_NAME                     343: str
        16682   LOAD_NAME                     358: ex
        16686   CALL_FUNCTION                 1
        16688   BINARY_ADD                    
        16690   LOAD_CONST                    271: 3
        16694   LOAD_CONST                    20: True
        16696   LOAD_CONST                    43: ('sendTeleMsg',)
        16698   CALL_FUNCTION_KW              3
        16700   POP_TOP                       
        16702   POP_BLOCK                     
        16704   POP_EXCEPT                    
        16706   LOAD_CONST                    1: None
        16708   STORE_NAME                    358: ex
        16712   DELETE_NAME                   358: ex
        16716   JUMP_FORWARD                  7 (to 16732)
        16718   LOAD_CONST                    1: None
        16720   STORE_NAME                    358: ex
        16724   DELETE_NAME                   358: ex
        16728   RERAISE                       1
        16730   RERAISE                       0
        16732   POP_EXCEPT                    
        16734   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        16738   STORE_GLOBAL                  221: Last_Traded_PE_Price
        16740   LOAD_CONST                    351: '  Place SELL order for new  '
        16744   LOAD_GLOBAL                   382: df_cols
        16748   FORMAT_VALUE                  0
        16750   LOAD_CONST                    363: ' PE at '
        16754   LOAD_GLOBAL                   221: NULL + strike_offset
        16756   FORMAT_VALUE                  0
        16758   BUILD_STRING                  4
        16760   STORE_NAME                    65: strMsg
        16762   LOAD_NAME                     59: iLog
        16764   LOAD_NAME                     65: strMsg
        16766   LOAD_CONST                    288: 5
        16770   LOAD_CONST                    20: True
        16772   LOAD_CONST                    43: ('sendTeleMsg',)
        16774   CALL_FUNCTION_KW              3
        16776   POP_TOP                       
        16778   LOAD_GLOBAL                   74: cfg
        16780   LOAD_CONST                    29: 1
        16782   BINARY_ADD                    
        16784   STORE_GLOBAL                  74: order_count
        16786   LOAD_GLOBAL                   76: read
        16788   LOAD_NAME                     376: Symbol
        16792   LOAD_GLOBAL                   382: df_cols
        16796   LOAD_CONST                    316: 'PE'
        16800   LOAD_CONST                    292: -1
        16804   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        16808   LOAD_GLOBAL                   221: NULL + strike_offset
        16810   LOAD_CONST                    29: 1
        16812   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        16816   BINARY_MULTIPLY               
        16818   LOAD_GLOBAL                   221: NULL + strike_offset
        16820   BINARY_MULTIPLY               
        16822   BUILD_LIST                    8
        16824   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        16826   LOAD_ATTR                     379: loc
        16830   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        16832   LOAD_NAME                     191: df_cols
        16834   BUILD_TUPLE                   2
        16836   STORE_SUBSCR                  
        16838   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        16840   LOAD_CONST                    29: 1
        16842   BINARY_ADD                    
        16844   STORE_GLOBAL                  190: df_king_cnt
        16846   LOAD_GLOBAL                   76: read
        16848   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        16852   LOAD_CONST                    0: 0
        16854   BINARY_SUBSCR                 
        16856   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        16860   LOAD_CONST                    29: 1
        16862   BINARY_SUBSCR                 
        16864   LOAD_CONST                    292: -1
        16868   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        16872   BINARY_MULTIPLY               
        16874   BUILD_LIST                    4
        16876   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        16878   LOAD_ATTR                     379: loc
        16882   LOAD_CONST                    0: 0
        16884   LOAD_NAME                     197: leg_cols
        16886   BUILD_TUPLE                   2
        16888   STORE_SUBSCR                  
        16890   LOAD_NAME                     24: pd
        16892   LOAD_METHOD                   380: concat
        16896   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        16898   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        16900   BUILD_LIST                    2
        16902   CALL_METHOD                   1
        16904   STORE_GLOBAL                  200: Current_legs
        16906   LOAD_GLOBAL                   78: get
        16908   LOAD_CONST                    0: 0
        16910   COMPARE_OP                    2 (==)
        16912   POP_JUMP_IF_FALSE             9121 (to 18242)
        16916   LOAD_NAME                     308: place_order
        16920   LOAD_CONST                    318: 'B'
        16924   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        16928   LOAD_CONST                    52: 2
        16930   BINARY_SUBSCR                 
        16932   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        16936   CALL_FUNCTION                 3
        16938   STORE_GLOBAL                  389: order_id_PE
        16942   LOAD_GLOBAL                   74: cfg
        16944   LOAD_CONST                    29: 1
        16946   BINARY_ADD                    
        16948   STORE_GLOBAL                  74: order_count
        16950   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        16954   STORE_GLOBAL                  221: Last_Traded_PE_Price
        16956   LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        16960   LOAD_CONST                    319: 'norenordno'
        16964   BINARY_SUBSCR                 
        16966   STORE_NAME                    384: order_id
        16970   LOAD_NAME                     311: get_order_symbol
        16974   LOAD_NAME                     384: order_id
        16978   CALL_FUNCTION                 1
        16980   STORE_NAME                    376: Symbol
        16984   LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        16988   LOAD_CONST                    320: 'stat'
        16992   BINARY_SUBSCR                 
        16994   STORE_NAME                    385: Placed_Status
        16998   LOAD_NAME                     309: get_order_status
        17002   LOAD_NAME                     384: order_id
        17006   CALL_FUNCTION                 1
        17008   STORE_NAME                    386: Return_Status
        17012   LOAD_NAME                     310: get_order_price
        17016   LOAD_NAME                     384: order_id
        17020   CALL_FUNCTION                 1
        17022   STORE_NAME                    387: average_price
        17026   LOAD_NAME                     386: Return_Status
        17030   LOAD_METHOD                   352: upper
        17034   CALL_METHOD                   0
        17036   LOAD_CONST                    321: 'REJECTED'
        17040   COMPARE_OP                    2 (==)
        17042   POP_JUMP_IF_FALSE             8569 (to 17138)
        17046   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        17050   LOAD_NAME                     384: order_id
        17054   FORMAT_VALUE                  0
        17056   LOAD_CONST                    323: ', Ord_STS = '
        17060   LOAD_NAME                     385: Placed_Status
        17064   FORMAT_VALUE                  0
        17066   LOAD_CONST                    324: ', Ret_STS = '
        17070   LOAD_NAME                     386: Return_Status
        17074   FORMAT_VALUE                  0
        17076   LOAD_CONST                    333: '.'
        17080   BUILD_STRING                  7
        17082   STORE_NAME                    65: strMsg
        17084   LOAD_NAME                     59: iLog
        17086   LOAD_NAME                     65: strMsg
        17088   LOAD_CONST                    288: 5
        17092   LOAD_CONST                    20: True
        17094   LOAD_CONST                    43: ('sendTeleMsg',)
        17096   CALL_FUNCTION_KW              3
        17098   POP_TOP                       
        17100   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        17104   STORE_NAME                    65: strMsg
        17106   LOAD_NAME                     59: iLog
        17108   LOAD_NAME                     65: strMsg
        17110   LOAD_CONST                    42: 4
        17112   LOAD_CONST                    20: True
        17114   LOAD_CONST                    43: ('sendTeleMsg',)
        17116   CALL_FUNCTION_KW              3
        17118   POP_TOP                       
        17120   LOAD_NAME                     322: close_all_orders
        17124   CALL_FUNCTION                 0
        17126   POP_TOP                       
        17128   LOAD_NAME                     0: sys
        17130   LOAD_METHOD                   344: exit
        17134   CALL_METHOD                   0
        17136   POP_TOP                       
        17138   LOAD_NAME                     387: average_price
        17142   LOAD_CONST                    0: 0
        17144   COMPARE_OP                    4 (>)
        17146   POP_JUMP_IF_FALSE             8588 (to 17176)
        17150   LOAD_NAME                     386: Return_Status
        17154   LOAD_METHOD                   352: upper
        17158   CALL_METHOD                   0
        17160   LOAD_CONST                    327: 'COMPLETE'
        17164   COMPARE_OP                    2 (==)
        17166   POP_JUMP_IF_FALSE             8588 (to 17176)
        17170   LOAD_NAME                     387: average_price
        17174   STORE_GLOBAL                  221: Last_Traded_PE_Price
        17176   LOAD_GLOBAL                   76: read
        17178   LOAD_NAME                     376: Symbol
        17182   LOAD_GLOBAL                   382: df_cols
        17186   LOAD_CONST                    316: 'PE'
        17190   LOAD_CONST                    29: 1
        17192   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        17196   LOAD_GLOBAL                   221: NULL + strike_offset
        17198   LOAD_CONST                    292: -1
        17202   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        17206   BINARY_MULTIPLY               
        17208   LOAD_GLOBAL                   221: NULL + strike_offset
        17210   BINARY_MULTIPLY               
        17212   BUILD_LIST                    8
        17214   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        17216   LOAD_ATTR                     379: loc
        17220   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        17222   LOAD_NAME                     191: df_cols
        17224   BUILD_TUPLE                   2
        17226   STORE_SUBSCR                  
        17228   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        17230   LOAD_CONST                    29: 1
        17232   BINARY_ADD                    
        17234   STORE_GLOBAL                  190: df_king_cnt
        17236   LOAD_CONST                    20: True
        17238   STORE_GLOBAL                  170: First_Straddle
        17240   LOAD_CONST                    365: ' Placed PE Buy Market order for ATM Strike='
        17244   LOAD_GLOBAL                   382: df_cols
        17248   FORMAT_VALUE                  0
        17250   LOAD_CONST                    366: ', ATM PE='
        17254   LOAD_NAME                     387: average_price
        17258   FORMAT_VALUE                  0
        17260   LOAD_CONST                    330: ', Qty ='
        17264   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        17268   FORMAT_VALUE                  0
        17270   LOAD_CONST                    331: ', Ord_ID = '
        17274   LOAD_NAME                     384: order_id
        17278   FORMAT_VALUE                  0
        17280   LOAD_CONST                    323: ', Ord_STS = '
        17284   LOAD_NAME                     385: Placed_Status
        17288   FORMAT_VALUE                  0
        17290   LOAD_CONST                    324: ', Ret_STS = '
        17294   LOAD_NAME                     386: Return_Status
        17298   FORMAT_VALUE                  0
        17300   BUILD_STRING                  12
        17302   STORE_NAME                    65: strMsg
        17304   LOAD_NAME                     59: iLog
        17306   LOAD_NAME                     65: strMsg
        17308   LOAD_CONST                    288: 5
        17312   LOAD_CONST                    20: True
        17314   LOAD_CONST                    43: ('sendTeleMsg',)
        17316   CALL_FUNCTION_KW              3
        17318   POP_TOP                       
        17320   LOAD_NAME                     72: tl
        17322   LOAD_METHOD                   388: update_csv
        17326   LOAD_NAME                     376: Symbol
        17330   LOAD_CONST                    332: 'Buy'
        17334   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        17338   LOAD_GLOBAL                   221: NULL + strike_offset
        17340   LOAD_NAME                     384: order_id
        17344   LOAD_NAME                     385: Placed_Status
        17348   LOAD_NAME                     386: Return_Status
        17352   CALL_METHOD                   7
        17354   POP_TOP                       
        17356   LOAD_GLOBAL                   76: read
        17358   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        17362   LOAD_CONST                    0: 0
        17364   BINARY_SUBSCR                 
        17366   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        17370   LOAD_CONST                    29: 1
        17372   BINARY_SUBSCR                 
        17374   LOAD_CONST                    0: 0
        17376   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        17380   BINARY_MULTIPLY               
        17382   BUILD_LIST                    4
        17384   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        17386   LOAD_ATTR                     379: loc
        17390   LOAD_CONST                    0: 0
        17392   LOAD_NAME                     197: leg_cols
        17394   BUILD_TUPLE                   2
        17396   STORE_SUBSCR                  
        17398   LOAD_NAME                     24: pd
        17400   LOAD_METHOD                   380: concat
        17404   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        17406   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        17408   BUILD_LIST                    2
        17410   CALL_METHOD                   1
        17412   STORE_GLOBAL                  200: Current_legs
        17414   LOAD_GLOBAL                   248: ST_Period
        17416   LOAD_CONST                    0: 0
        17418   COMPARE_OP                    2 (==)
        17420   POP_JUMP_IF_FALSE             8715 (to 17430)
        17424   LOAD_NAME                     178: PE_SL_Triggered
        17426   POP_JUMP_IF_TRUE              8718 (to 17436)
        17430   LOAD_NAME                     180: PE_TGT_Triggered
        17432   POP_JUMP_IF_FALSE             9121 (to 18242)
        17436   LOAD_NAME                     180: PE_TGT_Triggered
        17438   POP_JUMP_IF_FALSE             8802 (to 17604)
        17442   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        17444   LOAD_CONST                    341: 'NQ'
        17448   BINARY_SUBSCR                 
        17450   LOAD_METHOD                   390: sum
        17454   CALL_METHOD                   0
        17456   LOAD_CONST                    0: 0
        17458   COMPARE_OP                    2 (==)
        17460   POP_JUMP_IF_FALSE             8802 (to 17604)
        17464   SETUP_FINALLY                 8 (to 17482)
        17466   LOAD_NAME                     331: get_option_tokens
        17470   LOAD_CONST                    364: 'PEF'
        17474   CALL_FUNCTION                 1
        17476   POP_TOP                       
        17478   POP_BLOCK                     
        17480   JUMP_FORWARD                  130 (to 17742)
        17482   POP_TOP                       
        17484   POP_TOP                       
        17486   POP_TOP                       
        17488   LOAD_NAME                     2: time
        17490   LOAD_METHOD                   355: sleep
        17494   LOAD_CONST                    288: 5
        17498   CALL_METHOD                   1
        17500   POP_TOP                       
        17502   SETUP_FINALLY                 8 (to 17520)
        17504   LOAD_NAME                     331: get_option_tokens
        17508   LOAD_CONST                    364: 'PEF'
        17512   CALL_FUNCTION                 1
        17514   POP_TOP                       
        17516   POP_BLOCK                     
        17518   JUMP_FORWARD                  40 (to 17600)
        17520   DUP_TOP                       
        17522   LOAD_NAME                     357: Exception
        17526   JUMP_IF_NOT_EXC_MATCH         8799 (to 17598)
        17530   POP_TOP                       
        17532   STORE_NAME                    358: ex
        17536   POP_TOP                       
        17538   SETUP_FINALLY                 23 (to 17586)
        17540   LOAD_NAME                     59: iLog
        17542   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        17546   LOAD_NAME                     343: str
        17550   LOAD_NAME                     358: ex
        17554   CALL_FUNCTION                 1
        17556   BINARY_ADD                    
        17558   LOAD_CONST                    271: 3
        17562   LOAD_CONST                    20: True
        17564   LOAD_CONST                    43: ('sendTeleMsg',)
        17566   CALL_FUNCTION_KW              3
        17568   POP_TOP                       
        17570   POP_BLOCK                     
        17572   POP_EXCEPT                    
        17574   LOAD_CONST                    1: None
        17576   STORE_NAME                    358: ex
        17580   DELETE_NAME                   358: ex
        17584   JUMP_FORWARD                  7 (to 17600)
        17586   LOAD_CONST                    1: None
        17588   STORE_NAME                    358: ex
        17592   DELETE_NAME                   358: ex
        17596   RERAISE                       1
        17598   RERAISE                       0
        17600   POP_EXCEPT                    
        17602   JUMP_FORWARD                  69 (to 17742)
        17604   SETUP_FINALLY                 8 (to 17622)
        17606   LOAD_NAME                     331: get_option_tokens
        17610   LOAD_CONST                    316: 'PE'
        17614   CALL_FUNCTION                 1
        17616   POP_TOP                       
        17618   POP_BLOCK                     
        17620   JUMP_FORWARD                  60 (to 17742)
        17622   POP_TOP                       
        17624   POP_TOP                       
        17626   POP_TOP                       
        17628   LOAD_NAME                     2: time
        17630   LOAD_METHOD                   355: sleep
        17634   LOAD_CONST                    288: 5
        17638   CALL_METHOD                   1
        17640   POP_TOP                       
        17642   SETUP_FINALLY                 8 (to 17660)
        17644   LOAD_NAME                     331: get_option_tokens
        17648   LOAD_CONST                    316: 'PE'
        17652   CALL_FUNCTION                 1
        17654   POP_TOP                       
        17656   POP_BLOCK                     
        17658   JUMP_FORWARD                  40 (to 17740)
        17660   DUP_TOP                       
        17662   LOAD_NAME                     357: Exception
        17666   JUMP_IF_NOT_EXC_MATCH         8869 (to 17738)
        17670   POP_TOP                       
        17672   STORE_NAME                    358: ex
        17676   POP_TOP                       
        17678   SETUP_FINALLY                 23 (to 17726)
        17680   LOAD_NAME                     59: iLog
        17682   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        17686   LOAD_NAME                     343: str
        17690   LOAD_NAME                     358: ex
        17694   CALL_FUNCTION                 1
        17696   BINARY_ADD                    
        17698   LOAD_CONST                    271: 3
        17702   LOAD_CONST                    20: True
        17704   LOAD_CONST                    43: ('sendTeleMsg',)
        17706   CALL_FUNCTION_KW              3
        17708   POP_TOP                       
        17710   POP_BLOCK                     
        17712   POP_EXCEPT                    
        17714   LOAD_CONST                    1: None
        17716   STORE_NAME                    358: ex
        17720   DELETE_NAME                   358: ex
        17724   JUMP_FORWARD                  7 (to 17740)
        17726   LOAD_CONST                    1: None
        17728   STORE_NAME                    358: ex
        17732   DELETE_NAME                   358: ex
        17736   RERAISE                       1
        17738   RERAISE                       0
        17740   POP_EXCEPT                    
        17742   LOAD_NAME                     308: place_order
        17746   LOAD_CONST                    337: 'S'
        17750   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        17754   LOAD_CONST                    52: 2
        17756   BINARY_SUBSCR                 
        17758   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        17762   CALL_FUNCTION                 3
        17764   STORE_NAME                    395: order_id_PE1
        17768   LOAD_GLOBAL                   74: cfg
        17770   LOAD_CONST                    29: 1
        17772   BINARY_ADD                    
        17774   STORE_GLOBAL                  74: order_count
        17776   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        17780   STORE_GLOBAL                  221: Last_Traded_PE_Price
        17782   LOAD_NAME                     395: order_id_PE1
        17786   LOAD_CONST                    319: 'norenordno'
        17790   BINARY_SUBSCR                 
        17792   STORE_NAME                    384: order_id
        17796   LOAD_NAME                     311: get_order_symbol
        17800   LOAD_NAME                     384: order_id
        17804   CALL_FUNCTION                 1
        17806   STORE_NAME                    376: Symbol
        17810   LOAD_NAME                     395: order_id_PE1
        17814   LOAD_CONST                    320: 'stat'
        17818   BINARY_SUBSCR                 
        17820   STORE_NAME                    385: Placed_Status
        17824   LOAD_NAME                     309: get_order_status
        17828   LOAD_NAME                     384: order_id
        17832   CALL_FUNCTION                 1
        17834   STORE_NAME                    386: Return_Status
        17838   LOAD_NAME                     310: get_order_price
        17842   LOAD_NAME                     384: order_id
        17846   CALL_FUNCTION                 1
        17848   STORE_NAME                    387: average_price
        17852   LOAD_NAME                     386: Return_Status
        17856   LOAD_METHOD                   352: upper
        17860   CALL_METHOD                   0
        17862   LOAD_CONST                    321: 'REJECTED'
        17866   COMPARE_OP                    2 (==)
        17868   POP_JUMP_IF_FALSE             8982 (to 17964)
        17872   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        17876   LOAD_NAME                     384: order_id
        17880   FORMAT_VALUE                  0
        17882   LOAD_CONST                    323: ', Ord_STS = '
        17886   LOAD_NAME                     385: Placed_Status
        17890   FORMAT_VALUE                  0
        17892   LOAD_CONST                    324: ', Ret_STS = '
        17896   LOAD_NAME                     386: Return_Status
        17900   FORMAT_VALUE                  0
        17902   LOAD_CONST                    333: '.'
        17906   BUILD_STRING                  7
        17908   STORE_NAME                    65: strMsg
        17910   LOAD_NAME                     59: iLog
        17912   LOAD_NAME                     65: strMsg
        17914   LOAD_CONST                    288: 5
        17918   LOAD_CONST                    20: True
        17920   LOAD_CONST                    43: ('sendTeleMsg',)
        17922   CALL_FUNCTION_KW              3
        17924   POP_TOP                       
        17926   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        17930   STORE_NAME                    65: strMsg
        17932   LOAD_NAME                     59: iLog
        17934   LOAD_NAME                     65: strMsg
        17936   LOAD_CONST                    42: 4
        17938   LOAD_CONST                    20: True
        17940   LOAD_CONST                    43: ('sendTeleMsg',)
        17942   CALL_FUNCTION_KW              3
        17944   POP_TOP                       
        17946   LOAD_NAME                     322: close_all_orders
        17950   CALL_FUNCTION                 0
        17952   POP_TOP                       
        17954   LOAD_NAME                     0: sys
        17956   LOAD_METHOD                   344: exit
        17960   CALL_METHOD                   0
        17962   POP_TOP                       
        17964   LOAD_NAME                     387: average_price
        17968   LOAD_CONST                    0: 0
        17970   COMPARE_OP                    4 (>)
        17972   POP_JUMP_IF_FALSE             9001 (to 18002)
        17976   LOAD_NAME                     386: Return_Status
        17980   LOAD_METHOD                   352: upper
        17984   CALL_METHOD                   0
        17986   LOAD_CONST                    327: 'COMPLETE'
        17990   COMPARE_OP                    2 (==)
        17992   POP_JUMP_IF_FALSE             9001 (to 18002)
        17996   LOAD_NAME                     387: average_price
        18000   STORE_GLOBAL                  221: Last_Traded_PE_Price
        18002   LOAD_GLOBAL                   76: read
        18004   LOAD_NAME                     376: Symbol
        18008   LOAD_GLOBAL                   382: df_cols
        18012   LOAD_CONST                    316: 'PE'
        18016   LOAD_CONST                    292: -1
        18020   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        18024   LOAD_GLOBAL                   221: NULL + strike_offset
        18026   LOAD_CONST                    29: 1
        18028   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        18032   BINARY_MULTIPLY               
        18034   LOAD_GLOBAL                   221: NULL + strike_offset
        18036   BINARY_MULTIPLY               
        18038   BUILD_LIST                    8
        18040   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        18042   LOAD_ATTR                     379: loc
        18046   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        18048   LOAD_NAME                     191: df_cols
        18050   BUILD_TUPLE                   2
        18052   STORE_SUBSCR                  
        18054   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        18056   LOAD_CONST                    29: 1
        18058   BINARY_ADD                    
        18060   STORE_GLOBAL                  190: df_king_cnt
        18062   LOAD_CONST                    20: True
        18064   STORE_GLOBAL                  170: First_Straddle
        18066   LOAD_CONST                    367: ' Placed PE Sell Market order for ATM Strike='
        18070   LOAD_GLOBAL                   382: df_cols
        18074   FORMAT_VALUE                  0
        18076   LOAD_CONST                    366: ', ATM PE='
        18080   LOAD_NAME                     387: average_price
        18084   FORMAT_VALUE                  0
        18086   LOAD_CONST                    330: ', Qty ='
        18090   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        18094   FORMAT_VALUE                  0
        18096   LOAD_CONST                    331: ', Ord_ID = '
        18100   LOAD_NAME                     384: order_id
        18104   FORMAT_VALUE                  0
        18106   LOAD_CONST                    323: ', Ord_STS = '
        18110   LOAD_NAME                     385: Placed_Status
        18114   FORMAT_VALUE                  0
        18116   LOAD_CONST                    324: ', Ret_STS = '
        18120   LOAD_NAME                     386: Return_Status
        18124   FORMAT_VALUE                  0
        18126   BUILD_STRING                  12
        18128   STORE_NAME                    65: strMsg
        18130   LOAD_NAME                     59: iLog
        18132   LOAD_NAME                     65: strMsg
        18134   LOAD_CONST                    288: 5
        18138   LOAD_CONST                    20: True
        18140   LOAD_CONST                    43: ('sendTeleMsg',)
        18142   CALL_FUNCTION_KW              3
        18144   POP_TOP                       
        18146   LOAD_NAME                     72: tl
        18148   LOAD_METHOD                   388: update_csv
        18152   LOAD_NAME                     376: Symbol
        18156   LOAD_CONST                    339: 'Sell'
        18160   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        18164   LOAD_GLOBAL                   221: NULL + strike_offset
        18166   LOAD_NAME                     384: order_id
        18170   LOAD_NAME                     385: Placed_Status
        18174   LOAD_NAME                     386: Return_Status
        18178   CALL_METHOD                   7
        18180   POP_TOP                       
        18182   LOAD_GLOBAL                   76: read
        18184   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        18188   LOAD_CONST                    0: 0
        18190   BINARY_SUBSCR                 
        18192   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        18196   LOAD_CONST                    29: 1
        18198   BINARY_SUBSCR                 
        18200   LOAD_CONST                    292: -1
        18204   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        18208   BINARY_MULTIPLY               
        18210   BUILD_LIST                    4
        18212   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        18214   LOAD_ATTR                     379: loc
        18218   LOAD_CONST                    0: 0
        18220   LOAD_NAME                     197: leg_cols
        18222   BUILD_TUPLE                   2
        18224   STORE_SUBSCR                  
        18226   LOAD_NAME                     24: pd
        18228   LOAD_METHOD                   380: concat
        18232   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        18234   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        18236   BUILD_LIST                    2
        18238   CALL_METHOD                   1
        18240   STORE_GLOBAL                  200: Current_legs
        18242   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        18246   LOAD_CONST                    0: 0
        18248   COMPARE_OP                    2 (==)
        18250   POP_JUMP_IF_FALSE             9219 (to 18438)
        18254   LOAD_GLOBAL                   248: ST_Period
        18256   LOAD_CONST                    29: 1
        18258   COMPARE_OP                    2 (==)
        18260   POP_JUMP_IF_FALSE             9219 (to 18438)
        18264   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        18266   LOAD_CONST                    341: 'NQ'
        18270   BINARY_SUBSCR                 
        18272   LOAD_METHOD                   390: sum
        18276   CALL_METHOD                   0
        18278   LOAD_CONST                    0: 0
        18280   COMPARE_OP                    2 (==)
        18282   POP_JUMP_IF_FALSE             9219 (to 18438)
        18286   LOAD_NAME                     44: int
        18288   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18290   LOAD_CONST                    292: -1
        18294   BINARY_SUBSCR                 
        18296   CALL_FUNCTION                 1
        18298   LOAD_GLOBAL                   109: NULL + kernel32
        18300   BINARY_SUBTRACT               
        18302   LOAD_GLOBAL                   382: df_cols
        18306   LOAD_GLOBAL                   157: NULL + papertrade
        18308   BINARY_ADD                    
        18310   COMPARE_OP                    4 (>)
        18312   POP_JUMP_IF_TRUE              9202 (to 18404)
        18316   LOAD_NAME                     44: int
        18318   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18320   LOAD_CONST                    292: -1
        18324   BINARY_SUBSCR                 
        18326   CALL_FUNCTION                 1
        18328   LOAD_GLOBAL                   108: kernel32
        18330   BINARY_ADD                    
        18332   LOAD_GLOBAL                   381: NULL + df_king_cnt
        18336   LOAD_GLOBAL                   157: NULL + papertrade
        18338   BINARY_ADD                    
        18340   COMPARE_OP                    4 (>)
        18342   POP_JUMP_IF_TRUE              9202 (to 18404)
        18346   LOAD_NAME                     44: int
        18348   LOAD_GLOBAL                   382: df_cols
        18352   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18354   LOAD_CONST                    292: -1
        18358   BINARY_SUBSCR                 
        18360   LOAD_GLOBAL                   109: NULL + kernel32
        18362   BINARY_SUBTRACT               
        18364   BINARY_SUBTRACT               
        18366   CALL_FUNCTION                 1
        18368   LOAD_NAME                     44: int
        18370   LOAD_GLOBAL                   382: df_cols
        18374   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        18378   LOAD_GLOBAL                   109: NULL + kernel32
        18380   BINARY_SUBTRACT               
        18382   BINARY_SUBTRACT               
        18384   CALL_FUNCTION                 1
        18386   LOAD_CONST                    73: 100
        18388   LOAD_GLOBAL                   249: NULL + ST_Period
        18390   BINARY_SUBTRACT               
        18392   BINARY_MULTIPLY               
        18394   LOAD_CONST                    73: 100
        18396   BINARY_TRUE_DIVIDE            
        18398   COMPARE_OP                    0 (<)
        18400   POP_JUMP_IF_FALSE             9219 (to 18438)
        18404   LOAD_GLOBAL                   74: cfg
        18406   LOAD_GLOBAL                   162: Trade_Nifty
        18408   COMPARE_OP                    5 (>=)
        18410   POP_JUMP_IF_FALSE             9219 (to 18438)
        18414   LOAD_CONST                    368: ' PE Leg Re-entry triggered : Max order_limit_per_day Reached. Exiting trade for the day '
        18418   STORE_NAME                    65: strMsg
        18420   LOAD_NAME                     59: iLog
        18422   LOAD_NAME                     65: strMsg
        18424   LOAD_CONST                    42: 4
        18426   LOAD_CONST                    20: True
        18428   LOAD_CONST                    43: ('sendTeleMsg',)
        18430   CALL_FUNCTION_KW              3
        18432   POP_TOP                       
        18434   LOAD_CONST                    29: 1
        18436   STORE_GLOBAL                  80: ExitTradenow
        18438   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        18442   LOAD_CONST                    0: 0
        18444   COMPARE_OP                    2 (==)
        18446   POP_JUMP_IF_FALSE             9317 (to 18634)
        18450   LOAD_GLOBAL                   248: ST_Period
        18452   LOAD_CONST                    29: 1
        18454   COMPARE_OP                    2 (==)
        18456   POP_JUMP_IF_FALSE             9317 (to 18634)
        18460   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        18462   LOAD_CONST                    341: 'NQ'
        18466   BINARY_SUBSCR                 
        18468   LOAD_METHOD                   390: sum
        18472   CALL_METHOD                   0
        18474   LOAD_CONST                    0: 0
        18476   COMPARE_OP                    2 (==)
        18478   POP_JUMP_IF_FALSE             9317 (to 18634)
        18482   LOAD_NAME                     44: int
        18484   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18486   LOAD_CONST                    292: -1
        18490   BINARY_SUBSCR                 
        18492   CALL_FUNCTION                 1
        18494   LOAD_GLOBAL                   109: NULL + kernel32
        18496   BINARY_SUBTRACT               
        18498   LOAD_GLOBAL                   382: df_cols
        18502   LOAD_GLOBAL                   157: NULL + papertrade
        18504   BINARY_ADD                    
        18506   COMPARE_OP                    4 (>)
        18508   POP_JUMP_IF_TRUE              9300 (to 18600)
        18512   LOAD_NAME                     44: int
        18514   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18516   LOAD_CONST                    292: -1
        18520   BINARY_SUBSCR                 
        18522   CALL_FUNCTION                 1
        18524   LOAD_GLOBAL                   108: kernel32
        18526   BINARY_ADD                    
        18528   LOAD_GLOBAL                   381: NULL + df_king_cnt
        18532   LOAD_GLOBAL                   157: NULL + papertrade
        18534   BINARY_ADD                    
        18536   COMPARE_OP                    4 (>)
        18538   POP_JUMP_IF_TRUE              9300 (to 18600)
        18542   LOAD_NAME                     44: int
        18544   LOAD_GLOBAL                   382: df_cols
        18548   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18550   LOAD_CONST                    292: -1
        18554   BINARY_SUBSCR                 
        18556   LOAD_GLOBAL                   109: NULL + kernel32
        18558   BINARY_SUBTRACT               
        18560   BINARY_SUBTRACT               
        18562   CALL_FUNCTION                 1
        18564   LOAD_NAME                     44: int
        18566   LOAD_GLOBAL                   382: df_cols
        18570   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        18574   LOAD_GLOBAL                   109: NULL + kernel32
        18576   BINARY_SUBTRACT               
        18578   BINARY_SUBTRACT               
        18580   CALL_FUNCTION                 1
        18582   LOAD_CONST                    73: 100
        18584   LOAD_GLOBAL                   249: NULL + ST_Period
        18586   BINARY_SUBTRACT               
        18588   BINARY_MULTIPLY               
        18590   LOAD_CONST                    73: 100
        18592   BINARY_TRUE_DIVIDE            
        18594   COMPARE_OP                    0 (<)
        18596   POP_JUMP_IF_FALSE             9317 (to 18634)
        18600   LOAD_GLOBAL                   76: read
        18602   LOAD_GLOBAL                   90: Send_Telegram
        18604   COMPARE_OP                    5 (>=)
        18606   POP_JUMP_IF_FALSE             9317 (to 18634)
        18610   LOAD_CONST                    369: ' PE Leg Re-entry triggered : Position change after MaxPositionChangeTime. Exiting trade for the day '
        18614   STORE_NAME                    65: strMsg
        18616   LOAD_NAME                     59: iLog
        18618   LOAD_NAME                     65: strMsg
        18620   LOAD_CONST                    42: 4
        18622   LOAD_CONST                    20: True
        18624   LOAD_CONST                    43: ('sendTeleMsg',)
        18626   CALL_FUNCTION_KW              3
        18628   POP_TOP                       
        18630   LOAD_CONST                    29: 1
        18632   STORE_GLOBAL                  80: ExitTradenow
        18634   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        18638   LOAD_CONST                    0: 0
        18640   COMPARE_OP                    2 (==)
        18642   POP_JUMP_IF_FALSE             10114 (to 20228)
        18646   LOAD_GLOBAL                   248: ST_Period
        18648   LOAD_CONST                    29: 1
        18650   COMPARE_OP                    2 (==)
        18652   POP_JUMP_IF_FALSE             10114 (to 20228)
        18656   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        18658   LOAD_CONST                    341: 'NQ'
        18662   BINARY_SUBSCR                 
        18664   LOAD_METHOD                   390: sum
        18668   CALL_METHOD                   0
        18670   LOAD_CONST                    0: 0
        18672   COMPARE_OP                    2 (==)
        18674   POP_JUMP_IF_FALSE             10114 (to 20228)
        18678   LOAD_NAME                     44: int
        18680   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18682   LOAD_CONST                    292: -1
        18686   BINARY_SUBSCR                 
        18688   CALL_FUNCTION                 1
        18690   LOAD_GLOBAL                   109: NULL + kernel32
        18692   BINARY_SUBTRACT               
        18694   LOAD_GLOBAL                   382: df_cols
        18698   LOAD_GLOBAL                   157: NULL + papertrade
        18700   BINARY_ADD                    
        18702   COMPARE_OP                    4 (>)
        18704   POP_JUMP_IF_TRUE              9398 (to 18796)
        18708   LOAD_NAME                     44: int
        18710   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18712   LOAD_CONST                    292: -1
        18716   BINARY_SUBSCR                 
        18718   CALL_FUNCTION                 1
        18720   LOAD_GLOBAL                   108: kernel32
        18722   BINARY_ADD                    
        18724   LOAD_GLOBAL                   381: NULL + df_king_cnt
        18728   LOAD_GLOBAL                   157: NULL + papertrade
        18730   BINARY_ADD                    
        18732   COMPARE_OP                    4 (>)
        18734   POP_JUMP_IF_TRUE              9398 (to 18796)
        18738   LOAD_NAME                     44: int
        18740   LOAD_GLOBAL                   382: df_cols
        18744   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18746   LOAD_CONST                    292: -1
        18750   BINARY_SUBSCR                 
        18752   LOAD_GLOBAL                   109: NULL + kernel32
        18754   BINARY_SUBTRACT               
        18756   BINARY_SUBTRACT               
        18758   CALL_FUNCTION                 1
        18760   LOAD_NAME                     44: int
        18762   LOAD_GLOBAL                   382: df_cols
        18766   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        18770   LOAD_GLOBAL                   109: NULL + kernel32
        18772   BINARY_SUBTRACT               
        18774   BINARY_SUBTRACT               
        18776   CALL_FUNCTION                 1
        18778   LOAD_CONST                    73: 100
        18780   LOAD_GLOBAL                   249: NULL + ST_Period
        18782   BINARY_SUBTRACT               
        18784   BINARY_MULTIPLY               
        18786   LOAD_CONST                    73: 100
        18788   BINARY_TRUE_DIVIDE            
        18790   COMPARE_OP                    0 (<)
        18792   POP_JUMP_IF_FALSE             10114 (to 20228)
        18796   LOAD_GLOBAL                   76: read
        18798   LOAD_GLOBAL                   90: Send_Telegram
        18800   COMPARE_OP                    0 (<)
        18802   POP_JUMP_IF_FALSE             10114 (to 20228)
        18806   LOAD_GLOBAL                   74: cfg
        18808   LOAD_GLOBAL                   162: Trade_Nifty
        18810   COMPARE_OP                    0 (<)
        18812   POP_JUMP_IF_FALSE             10114 (to 20228)
        18816   LOAD_CONST                    370: ' PE Leg Re-entry triggered (LTP,ATM_CE_Strike,ATM_PE_Strike,Delta_Limit,Actual_Delta): ('
        18820   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18822   LOAD_CONST                    292: -1
        18826   BINARY_SUBSCR                 
        18828   FORMAT_VALUE                  0
        18830   LOAD_CONST                    303: ','
        18834   LOAD_GLOBAL                   381: NULL + df_king_cnt
        18838   FORMAT_VALUE                  0
        18840   LOAD_CONST                    303: ','
        18844   LOAD_GLOBAL                   382: df_cols
        18848   FORMAT_VALUE                  0
        18850   LOAD_CONST                    303: ','
        18854   LOAD_NAME                     44: int
        18856   LOAD_GLOBAL                   382: df_cols
        18860   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        18864   LOAD_GLOBAL                   109: NULL + kernel32
        18866   BINARY_SUBTRACT               
        18868   BINARY_SUBTRACT               
        18870   CALL_FUNCTION                 1
        18872   LOAD_CONST                    73: 100
        18874   LOAD_GLOBAL                   249: NULL + ST_Period
        18876   BINARY_SUBTRACT               
        18878   BINARY_MULTIPLY               
        18880   LOAD_CONST                    73: 100
        18882   BINARY_TRUE_DIVIDE            
        18884   FORMAT_VALUE                  0
        18886   LOAD_CONST                    303: ','
        18890   LOAD_NAME                     44: int
        18892   LOAD_GLOBAL                   382: df_cols
        18896   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        18898   LOAD_CONST                    292: -1
        18902   BINARY_SUBSCR                 
        18904   LOAD_GLOBAL                   109: NULL + kernel32
        18906   BINARY_SUBTRACT               
        18908   BINARY_SUBTRACT               
        18910   CALL_FUNCTION                 1
        18912   FORMAT_VALUE                  0
        18914   LOAD_CONST                    305: ')'
        18918   BUILD_STRING                  11
        18920   STORE_NAME                    65: strMsg
        18922   LOAD_NAME                     59: iLog
        18924   LOAD_NAME                     65: strMsg
        18926   LOAD_CONST                    52: 2
        18928   LOAD_CONST                    20: True
        18930   LOAD_CONST                    43: ('sendTeleMsg',)
        18932   CALL_FUNCTION_KW              3
        18934   POP_TOP                       
        18936   LOAD_GLOBAL                   78: get
        18938   LOAD_CONST                    29: 1
        18940   COMPARE_OP                    2 (==)
        18942   POP_JUMP_IF_FALSE             9709 (to 19418)
        18946   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        18948   LOAD_CONST                    341: 'NQ'
        18952   BINARY_SUBSCR                 
        18954   LOAD_METHOD                   390: sum
        18958   CALL_METHOD                   0
        18960   LOAD_CONST                    0: 0
        18962   COMPARE_OP                    2 (==)
        18964   POP_JUMP_IF_FALSE             9554 (to 19108)
        18968   SETUP_FINALLY                 8 (to 18986)
        18970   LOAD_NAME                     331: get_option_tokens
        18974   LOAD_CONST                    364: 'PEF'
        18978   CALL_FUNCTION                 1
        18980   POP_TOP                       
        18982   POP_BLOCK                     
        18984   JUMP_FORWARD                  130 (to 19246)
        18986   POP_TOP                       
        18988   POP_TOP                       
        18990   POP_TOP                       
        18992   LOAD_NAME                     2: time
        18994   LOAD_METHOD                   355: sleep
        18998   LOAD_CONST                    288: 5
        19002   CALL_METHOD                   1
        19004   POP_TOP                       
        19006   SETUP_FINALLY                 8 (to 19024)
        19008   LOAD_NAME                     331: get_option_tokens
        19012   LOAD_CONST                    364: 'PEF'
        19016   CALL_FUNCTION                 1
        19018   POP_TOP                       
        19020   POP_BLOCK                     
        19022   JUMP_FORWARD                  40 (to 19104)
        19024   DUP_TOP                       
        19026   LOAD_NAME                     357: Exception
        19030   JUMP_IF_NOT_EXC_MATCH         9551 (to 19102)
        19034   POP_TOP                       
        19036   STORE_NAME                    358: ex
        19040   POP_TOP                       
        19042   SETUP_FINALLY                 23 (to 19090)
        19044   LOAD_NAME                     59: iLog
        19046   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        19050   LOAD_NAME                     343: str
        19054   LOAD_NAME                     358: ex
        19058   CALL_FUNCTION                 1
        19060   BINARY_ADD                    
        19062   LOAD_CONST                    271: 3
        19066   LOAD_CONST                    20: True
        19068   LOAD_CONST                    43: ('sendTeleMsg',)
        19070   CALL_FUNCTION_KW              3
        19072   POP_TOP                       
        19074   POP_BLOCK                     
        19076   POP_EXCEPT                    
        19078   LOAD_CONST                    1: None
        19080   STORE_NAME                    358: ex
        19084   DELETE_NAME                   358: ex
        19088   JUMP_FORWARD                  7 (to 19104)
        19090   LOAD_CONST                    1: None
        19092   STORE_NAME                    358: ex
        19096   DELETE_NAME                   358: ex
        19100   RERAISE                       1
        19102   RERAISE                       0
        19104   POP_EXCEPT                    
        19106   JUMP_FORWARD                  69 (to 19246)
        19108   SETUP_FINALLY                 8 (to 19126)
        19110   LOAD_NAME                     331: get_option_tokens
        19114   LOAD_CONST                    316: 'PE'
        19118   CALL_FUNCTION                 1
        19120   POP_TOP                       
        19122   POP_BLOCK                     
        19124   JUMP_FORWARD                  60 (to 19246)
        19126   POP_TOP                       
        19128   POP_TOP                       
        19130   POP_TOP                       
        19132   LOAD_NAME                     2: time
        19134   LOAD_METHOD                   355: sleep
        19138   LOAD_CONST                    288: 5
        19142   CALL_METHOD                   1
        19144   POP_TOP                       
        19146   SETUP_FINALLY                 8 (to 19164)
        19148   LOAD_NAME                     331: get_option_tokens
        19152   LOAD_CONST                    316: 'PE'
        19156   CALL_FUNCTION                 1
        19158   POP_TOP                       
        19160   POP_BLOCK                     
        19162   JUMP_FORWARD                  40 (to 19244)
        19164   DUP_TOP                       
        19166   LOAD_NAME                     357: Exception
        19170   JUMP_IF_NOT_EXC_MATCH         9621 (to 19242)
        19174   POP_TOP                       
        19176   STORE_NAME                    358: ex
        19180   POP_TOP                       
        19182   SETUP_FINALLY                 23 (to 19230)
        19184   LOAD_NAME                     59: iLog
        19186   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        19190   LOAD_NAME                     343: str
        19194   LOAD_NAME                     358: ex
        19198   CALL_FUNCTION                 1
        19200   BINARY_ADD                    
        19202   LOAD_CONST                    271: 3
        19206   LOAD_CONST                    20: True
        19208   LOAD_CONST                    43: ('sendTeleMsg',)
        19210   CALL_FUNCTION_KW              3
        19212   POP_TOP                       
        19214   POP_BLOCK                     
        19216   POP_EXCEPT                    
        19218   LOAD_CONST                    1: None
        19220   STORE_NAME                    358: ex
        19224   DELETE_NAME                   358: ex
        19228   JUMP_FORWARD                  7 (to 19244)
        19230   LOAD_CONST                    1: None
        19232   STORE_NAME                    358: ex
        19236   DELETE_NAME                   358: ex
        19240   RERAISE                       1
        19242   RERAISE                       0
        19244   POP_EXCEPT                    
        19246   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        19250   STORE_GLOBAL                  221: Last_Traded_PE_Price
        19252   LOAD_CONST                    371: '  Place SELL order for '
        19256   LOAD_GLOBAL                   382: df_cols
        19260   FORMAT_VALUE                  0
        19262   LOAD_CONST                    363: ' PE at '
        19266   LOAD_GLOBAL                   221: NULL + strike_offset
        19268   FORMAT_VALUE                  0
        19270   BUILD_STRING                  4
        19272   STORE_NAME                    65: strMsg
        19274   LOAD_NAME                     59: iLog
        19276   LOAD_NAME                     65: strMsg
        19278   LOAD_CONST                    288: 5
        19282   LOAD_CONST                    20: True
        19284   LOAD_CONST                    43: ('sendTeleMsg',)
        19286   CALL_FUNCTION_KW              3
        19288   POP_TOP                       
        19290   LOAD_GLOBAL                   74: cfg
        19292   LOAD_CONST                    29: 1
        19294   BINARY_ADD                    
        19296   STORE_GLOBAL                  74: order_count
        19298   LOAD_GLOBAL                   76: read
        19300   LOAD_NAME                     376: Symbol
        19304   LOAD_GLOBAL                   382: df_cols
        19308   LOAD_CONST                    316: 'PE'
        19312   LOAD_CONST                    292: -1
        19316   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        19320   LOAD_GLOBAL                   221: NULL + strike_offset
        19322   LOAD_CONST                    29: 1
        19324   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        19328   BINARY_MULTIPLY               
        19330   LOAD_GLOBAL                   221: NULL + strike_offset
        19332   BINARY_MULTIPLY               
        19334   BUILD_LIST                    8
        19336   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        19338   LOAD_ATTR                     379: loc
        19342   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        19344   LOAD_NAME                     191: df_cols
        19346   BUILD_TUPLE                   2
        19348   STORE_SUBSCR                  
        19350   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        19352   LOAD_CONST                    29: 1
        19354   BINARY_ADD                    
        19356   STORE_GLOBAL                  190: df_king_cnt
        19358   LOAD_GLOBAL                   76: read
        19360   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        19364   LOAD_CONST                    0: 0
        19366   BINARY_SUBSCR                 
        19368   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        19372   LOAD_CONST                    29: 1
        19374   BINARY_SUBSCR                 
        19376   LOAD_CONST                    292: -1
        19380   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        19384   BINARY_MULTIPLY               
        19386   BUILD_LIST                    4
        19388   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        19390   LOAD_ATTR                     379: loc
        19394   LOAD_CONST                    0: 0
        19396   LOAD_NAME                     197: leg_cols
        19398   BUILD_TUPLE                   2
        19400   STORE_SUBSCR                  
        19402   LOAD_NAME                     24: pd
        19404   LOAD_METHOD                   380: concat
        19408   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        19410   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        19412   BUILD_LIST                    2
        19414   CALL_METHOD                   1
        19416   STORE_GLOBAL                  200: Current_legs
        19418   LOAD_GLOBAL                   78: get
        19420   LOAD_CONST                    0: 0
        19422   COMPARE_OP                    2 (==)
        19424   POP_JUMP_IF_FALSE             10114 (to 20228)
        19428   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        19430   LOAD_CONST                    341: 'NQ'
        19434   BINARY_SUBSCR                 
        19436   LOAD_METHOD                   390: sum
        19440   CALL_METHOD                   0
        19442   LOAD_CONST                    0: 0
        19444   COMPARE_OP                    2 (==)
        19446   POP_JUMP_IF_FALSE             9795 (to 19590)
        19450   SETUP_FINALLY                 8 (to 19468)
        19452   LOAD_NAME                     331: get_option_tokens
        19456   LOAD_CONST                    364: 'PEF'
        19460   CALL_FUNCTION                 1
        19462   POP_TOP                       
        19464   POP_BLOCK                     
        19466   JUMP_FORWARD                  130 (to 19728)
        19468   POP_TOP                       
        19470   POP_TOP                       
        19472   POP_TOP                       
        19474   LOAD_NAME                     2: time
        19476   LOAD_METHOD                   355: sleep
        19480   LOAD_CONST                    288: 5
        19484   CALL_METHOD                   1
        19486   POP_TOP                       
        19488   SETUP_FINALLY                 8 (to 19506)
        19490   LOAD_NAME                     331: get_option_tokens
        19494   LOAD_CONST                    364: 'PEF'
        19498   CALL_FUNCTION                 1
        19500   POP_TOP                       
        19502   POP_BLOCK                     
        19504   JUMP_FORWARD                  40 (to 19586)
        19506   DUP_TOP                       
        19508   LOAD_NAME                     357: Exception
        19512   JUMP_IF_NOT_EXC_MATCH         9792 (to 19584)
        19516   POP_TOP                       
        19518   STORE_NAME                    358: ex
        19522   POP_TOP                       
        19524   SETUP_FINALLY                 23 (to 19572)
        19526   LOAD_NAME                     59: iLog
        19528   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        19532   LOAD_NAME                     343: str
        19536   LOAD_NAME                     358: ex
        19540   CALL_FUNCTION                 1
        19542   BINARY_ADD                    
        19544   LOAD_CONST                    271: 3
        19548   LOAD_CONST                    20: True
        19550   LOAD_CONST                    43: ('sendTeleMsg',)
        19552   CALL_FUNCTION_KW              3
        19554   POP_TOP                       
        19556   POP_BLOCK                     
        19558   POP_EXCEPT                    
        19560   LOAD_CONST                    1: None
        19562   STORE_NAME                    358: ex
        19566   DELETE_NAME                   358: ex
        19570   JUMP_FORWARD                  7 (to 19586)
        19572   LOAD_CONST                    1: None
        19574   STORE_NAME                    358: ex
        19578   DELETE_NAME                   358: ex
        19582   RERAISE                       1
        19584   RERAISE                       0
        19586   POP_EXCEPT                    
        19588   JUMP_FORWARD                  69 (to 19728)
        19590   SETUP_FINALLY                 8 (to 19608)
        19592   LOAD_NAME                     331: get_option_tokens
        19596   LOAD_CONST                    316: 'PE'
        19600   CALL_FUNCTION                 1
        19602   POP_TOP                       
        19604   POP_BLOCK                     
        19606   JUMP_FORWARD                  60 (to 19728)
        19608   POP_TOP                       
        19610   POP_TOP                       
        19612   POP_TOP                       
        19614   LOAD_NAME                     2: time
        19616   LOAD_METHOD                   355: sleep
        19620   LOAD_CONST                    288: 5
        19624   CALL_METHOD                   1
        19626   POP_TOP                       
        19628   SETUP_FINALLY                 8 (to 19646)
        19630   LOAD_NAME                     331: get_option_tokens
        19634   LOAD_CONST                    316: 'PE'
        19638   CALL_FUNCTION                 1
        19640   POP_TOP                       
        19642   POP_BLOCK                     
        19644   JUMP_FORWARD                  40 (to 19726)
        19646   DUP_TOP                       
        19648   LOAD_NAME                     357: Exception
        19652   JUMP_IF_NOT_EXC_MATCH         9862 (to 19724)
        19656   POP_TOP                       
        19658   STORE_NAME                    358: ex
        19662   POP_TOP                       
        19664   SETUP_FINALLY                 23 (to 19712)
        19666   LOAD_NAME                     59: iLog
        19668   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        19672   LOAD_NAME                     343: str
        19676   LOAD_NAME                     358: ex
        19680   CALL_FUNCTION                 1
        19682   BINARY_ADD                    
        19684   LOAD_CONST                    271: 3
        19688   LOAD_CONST                    20: True
        19690   LOAD_CONST                    43: ('sendTeleMsg',)
        19692   CALL_FUNCTION_KW              3
        19694   POP_TOP                       
        19696   POP_BLOCK                     
        19698   POP_EXCEPT                    
        19700   LOAD_CONST                    1: None
        19702   STORE_NAME                    358: ex
        19706   DELETE_NAME                   358: ex
        19710   JUMP_FORWARD                  7 (to 19726)
        19712   LOAD_CONST                    1: None
        19714   STORE_NAME                    358: ex
        19718   DELETE_NAME                   358: ex
        19722   RERAISE                       1
        19724   RERAISE                       0
        19726   POP_EXCEPT                    
        19728   LOAD_NAME                     308: place_order
        19732   LOAD_CONST                    337: 'S'
        19736   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        19740   LOAD_CONST                    52: 2
        19742   BINARY_SUBSCR                 
        19744   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        19748   CALL_FUNCTION                 3
        19750   STORE_NAME                    395: order_id_PE1
        19754   LOAD_GLOBAL                   74: cfg
        19756   LOAD_CONST                    29: 1
        19758   BINARY_ADD                    
        19760   STORE_GLOBAL                  74: order_count
        19762   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        19766   STORE_GLOBAL                  221: Last_Traded_PE_Price
        19768   LOAD_NAME                     395: order_id_PE1
        19772   LOAD_CONST                    319: 'norenordno'
        19776   BINARY_SUBSCR                 
        19778   STORE_NAME                    384: order_id
        19782   LOAD_NAME                     311: get_order_symbol
        19786   LOAD_NAME                     384: order_id
        19790   CALL_FUNCTION                 1
        19792   STORE_NAME                    376: Symbol
        19796   LOAD_NAME                     395: order_id_PE1
        19800   LOAD_CONST                    320: 'stat'
        19804   BINARY_SUBSCR                 
        19806   STORE_NAME                    385: Placed_Status
        19810   LOAD_NAME                     309: get_order_status
        19814   LOAD_NAME                     384: order_id
        19818   CALL_FUNCTION                 1
        19820   STORE_NAME                    386: Return_Status
        19824   LOAD_NAME                     310: get_order_price
        19828   LOAD_NAME                     384: order_id
        19832   CALL_FUNCTION                 1
        19834   STORE_NAME                    387: average_price
        19838   LOAD_NAME                     386: Return_Status
        19842   LOAD_METHOD                   352: upper
        19846   CALL_METHOD                   0
        19848   LOAD_CONST                    321: 'REJECTED'
        19852   COMPARE_OP                    2 (==)
        19854   POP_JUMP_IF_FALSE             9975 (to 19950)
        19858   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        19862   LOAD_NAME                     384: order_id
        19866   FORMAT_VALUE                  0
        19868   LOAD_CONST                    323: ', Ord_STS = '
        19872   LOAD_NAME                     385: Placed_Status
        19876   FORMAT_VALUE                  0
        19878   LOAD_CONST                    324: ', Ret_STS = '
        19882   LOAD_NAME                     386: Return_Status
        19886   FORMAT_VALUE                  0
        19888   LOAD_CONST                    333: '.'
        19892   BUILD_STRING                  7
        19894   STORE_NAME                    65: strMsg
        19896   LOAD_NAME                     59: iLog
        19898   LOAD_NAME                     65: strMsg
        19900   LOAD_CONST                    288: 5
        19904   LOAD_CONST                    20: True
        19906   LOAD_CONST                    43: ('sendTeleMsg',)
        19908   CALL_FUNCTION_KW              3
        19910   POP_TOP                       
        19912   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        19916   STORE_NAME                    65: strMsg
        19918   LOAD_NAME                     59: iLog
        19920   LOAD_NAME                     65: strMsg
        19922   LOAD_CONST                    42: 4
        19924   LOAD_CONST                    20: True
        19926   LOAD_CONST                    43: ('sendTeleMsg',)
        19928   CALL_FUNCTION_KW              3
        19930   POP_TOP                       
        19932   LOAD_NAME                     322: close_all_orders
        19936   CALL_FUNCTION                 0
        19938   POP_TOP                       
        19940   LOAD_NAME                     0: sys
        19942   LOAD_METHOD                   344: exit
        19946   CALL_METHOD                   0
        19948   POP_TOP                       
        19950   LOAD_NAME                     387: average_price
        19954   LOAD_CONST                    0: 0
        19956   COMPARE_OP                    4 (>)
        19958   POP_JUMP_IF_FALSE             9994 (to 19988)
        19962   LOAD_NAME                     386: Return_Status
        19966   LOAD_METHOD                   352: upper
        19970   CALL_METHOD                   0
        19972   LOAD_CONST                    327: 'COMPLETE'
        19976   COMPARE_OP                    2 (==)
        19978   POP_JUMP_IF_FALSE             9994 (to 19988)
        19982   LOAD_NAME                     387: average_price
        19986   STORE_GLOBAL                  221: Last_Traded_PE_Price
        19988   LOAD_GLOBAL                   76: read
        19990   LOAD_NAME                     376: Symbol
        19994   LOAD_GLOBAL                   382: df_cols
        19998   LOAD_CONST                    316: 'PE'
        20002   LOAD_CONST                    292: -1
        20006   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20010   LOAD_GLOBAL                   221: NULL + strike_offset
        20012   LOAD_CONST                    29: 1
        20014   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20018   BINARY_MULTIPLY               
        20020   LOAD_GLOBAL                   221: NULL + strike_offset
        20022   BINARY_MULTIPLY               
        20024   BUILD_LIST                    8
        20026   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        20028   LOAD_ATTR                     379: loc
        20032   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        20034   LOAD_NAME                     191: df_cols
        20036   BUILD_TUPLE                   2
        20038   STORE_SUBSCR                  
        20040   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        20042   LOAD_CONST                    29: 1
        20044   BINARY_ADD                    
        20046   STORE_GLOBAL                  190: df_king_cnt
        20048   LOAD_CONST                    20: True
        20050   STORE_GLOBAL                  170: First_Straddle
        20052   LOAD_CONST                    367: ' Placed PE Sell Market order for ATM Strike='
        20056   LOAD_GLOBAL                   382: df_cols
        20060   FORMAT_VALUE                  0
        20062   LOAD_CONST                    366: ', ATM PE='
        20066   LOAD_NAME                     387: average_price
        20070   FORMAT_VALUE                  0
        20072   LOAD_CONST                    330: ', Qty ='
        20076   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20080   FORMAT_VALUE                  0
        20082   LOAD_CONST                    331: ', Ord_ID = '
        20086   LOAD_NAME                     384: order_id
        20090   FORMAT_VALUE                  0
        20092   LOAD_CONST                    323: ', Ord_STS = '
        20096   LOAD_NAME                     385: Placed_Status
        20100   FORMAT_VALUE                  0
        20102   LOAD_CONST                    324: ', Ret_STS = '
        20106   LOAD_NAME                     386: Return_Status
        20110   FORMAT_VALUE                  0
        20112   BUILD_STRING                  12
        20114   STORE_NAME                    65: strMsg
        20116   LOAD_NAME                     59: iLog
        20118   LOAD_NAME                     65: strMsg
        20120   LOAD_CONST                    288: 5
        20124   LOAD_CONST                    20: True
        20126   LOAD_CONST                    43: ('sendTeleMsg',)
        20128   CALL_FUNCTION_KW              3
        20130   POP_TOP                       
        20132   LOAD_NAME                     72: tl
        20134   LOAD_METHOD                   388: update_csv
        20138   LOAD_NAME                     376: Symbol
        20142   LOAD_CONST                    339: 'Sell'
        20146   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20150   LOAD_GLOBAL                   221: NULL + strike_offset
        20152   LOAD_NAME                     384: order_id
        20156   LOAD_NAME                     385: Placed_Status
        20160   LOAD_NAME                     386: Return_Status
        20164   CALL_METHOD                   7
        20166   POP_TOP                       
        20168   LOAD_GLOBAL                   76: read
        20170   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        20174   LOAD_CONST                    0: 0
        20176   BINARY_SUBSCR                 
        20178   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        20182   LOAD_CONST                    29: 1
        20184   BINARY_SUBSCR                 
        20186   LOAD_CONST                    292: -1
        20190   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20194   BINARY_MULTIPLY               
        20196   BUILD_LIST                    4
        20198   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        20200   LOAD_ATTR                     379: loc
        20204   LOAD_CONST                    0: 0
        20206   LOAD_NAME                     197: leg_cols
        20208   BUILD_TUPLE                   2
        20210   STORE_SUBSCR                  
        20212   LOAD_NAME                     24: pd
        20214   LOAD_METHOD                   380: concat
        20218   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        20220   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        20222   BUILD_LIST                    2
        20224   CALL_METHOD                   1
        20226   STORE_GLOBAL                  200: Current_legs
        20228   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        20232   LOAD_CONST                    0: 0
        20234   COMPARE_OP                    2 (==)
        20236   POP_JUMP_IF_FALSE             10178 (to 20356)
        20240   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        20242   LOAD_CONST                    341: 'NQ'
        20246   BINARY_SUBSCR                 
        20248   LOAD_METHOD                   390: sum
        20252   CALL_METHOD                   0
        20254   LOAD_CONST                    0: 0
        20256   COMPARE_OP                    3 (!=)
        20258   POP_JUMP_IF_FALSE             10135 (to 20270)
        20262   LOAD_CONST                    292: -1
        20266   STORE_NAME                    396: CE_Mult
        20270   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        20272   LOAD_CONST                    341: 'NQ'
        20276   BINARY_SUBSCR                 
        20278   LOAD_METHOD                   390: sum
        20282   CALL_METHOD                   0
        20284   LOAD_CONST                    0: 0
        20286   COMPARE_OP                    2 (==)
        20288   POP_JUMP_IF_FALSE             10149 (to 20298)
        20292   LOAD_CONST                    0: 0
        20294   STORE_NAME                    396: CE_Mult
        20298   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        20300   LOAD_CONST                    341: 'NQ'
        20304   BINARY_SUBSCR                 
        20306   LOAD_METHOD                   390: sum
        20310   CALL_METHOD                   0
        20312   LOAD_CONST                    0: 0
        20314   COMPARE_OP                    3 (!=)
        20316   POP_JUMP_IF_FALSE             10164 (to 20328)
        20320   LOAD_CONST                    292: -1
        20324   STORE_NAME                    397: PE_Mult
        20328   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        20330   LOAD_CONST                    341: 'NQ'
        20334   BINARY_SUBSCR                 
        20336   LOAD_METHOD                   390: sum
        20340   CALL_METHOD                   0
        20342   LOAD_CONST                    0: 0
        20344   COMPARE_OP                    2 (==)
        20346   POP_JUMP_IF_FALSE             10178 (to 20356)
        20350   LOAD_CONST                    0: 0
        20352   STORE_NAME                    397: PE_Mult
        20356   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        20360   LOAD_CONST                    29: 1
        20362   COMPARE_OP                    2 (==)
        20364   POP_JUMP_IF_FALSE             10244 (to 20488)
        20368   LOAD_GLOBAL                   171: NULL + King_Candle_Max_SL
        20370   POP_JUMP_IF_FALSE             10244 (to 20488)
        20374   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        20376   LOAD_CONST                    341: 'NQ'
        20380   BINARY_SUBSCR                 
        20382   LOAD_METHOD                   390: sum
        20386   CALL_METHOD                   0
        20388   LOAD_CONST                    0: 0
        20390   COMPARE_OP                    3 (!=)
        20392   POP_JUMP_IF_FALSE             10201 (to 20402)
        20396   LOAD_CONST                    29: 1
        20398   STORE_NAME                    396: CE_Mult
        20402   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        20404   LOAD_CONST                    341: 'NQ'
        20408   BINARY_SUBSCR                 
        20410   LOAD_METHOD                   390: sum
        20414   CALL_METHOD                   0
        20416   LOAD_CONST                    0: 0
        20418   COMPARE_OP                    2 (==)
        20420   POP_JUMP_IF_FALSE             10215 (to 20430)
        20424   LOAD_CONST                    0: 0
        20426   STORE_NAME                    396: CE_Mult
        20430   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        20432   LOAD_CONST                    341: 'NQ'
        20436   BINARY_SUBSCR                 
        20438   LOAD_METHOD                   390: sum
        20442   CALL_METHOD                   0
        20444   LOAD_CONST                    0: 0
        20446   COMPARE_OP                    3 (!=)
        20448   POP_JUMP_IF_FALSE             10230 (to 20460)
        20452   LOAD_CONST                    292: -1
        20456   STORE_NAME                    397: PE_Mult
        20460   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        20462   LOAD_CONST                    341: 'NQ'
        20466   BINARY_SUBSCR                 
        20468   LOAD_METHOD                   390: sum
        20472   CALL_METHOD                   0
        20474   LOAD_CONST                    0: 0
        20476   COMPARE_OP                    2 (==)
        20478   POP_JUMP_IF_FALSE             10244 (to 20488)
        20482   LOAD_CONST                    0: 0
        20484   STORE_NAME                    397: PE_Mult
        20488   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        20492   LOAD_CONST                    292: -1
        20496   COMPARE_OP                    2 (==)
        20498   POP_JUMP_IF_FALSE             10311 (to 20622)
        20502   LOAD_GLOBAL                   172: time_offset_sec
        20504   POP_JUMP_IF_FALSE             10311 (to 20622)
        20508   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        20510   LOAD_CONST                    341: 'NQ'
        20514   BINARY_SUBSCR                 
        20516   LOAD_METHOD                   390: sum
        20520   CALL_METHOD                   0
        20522   LOAD_CONST                    0: 0
        20524   COMPARE_OP                    3 (!=)
        20526   POP_JUMP_IF_FALSE             10269 (to 20538)
        20530   LOAD_CONST                    292: -1
        20534   STORE_NAME                    396: CE_Mult
        20538   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        20540   LOAD_CONST                    341: 'NQ'
        20544   BINARY_SUBSCR                 
        20546   LOAD_METHOD                   390: sum
        20550   CALL_METHOD                   0
        20552   LOAD_CONST                    0: 0
        20554   COMPARE_OP                    2 (==)
        20556   POP_JUMP_IF_FALSE             10283 (to 20566)
        20560   LOAD_CONST                    0: 0
        20562   STORE_NAME                    396: CE_Mult
        20566   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        20568   LOAD_CONST                    341: 'NQ'
        20572   BINARY_SUBSCR                 
        20574   LOAD_METHOD                   390: sum
        20578   CALL_METHOD                   0
        20580   LOAD_CONST                    0: 0
        20582   COMPARE_OP                    3 (!=)
        20584   POP_JUMP_IF_FALSE             10297 (to 20594)
        20588   LOAD_CONST                    29: 1
        20590   STORE_NAME                    397: PE_Mult
        20594   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        20596   LOAD_CONST                    341: 'NQ'
        20600   BINARY_SUBSCR                 
        20602   LOAD_METHOD                   390: sum
        20606   CALL_METHOD                   0
        20608   LOAD_CONST                    0: 0
        20610   COMPARE_OP                    2 (==)
        20612   POP_JUMP_IF_FALSE             10311 (to 20622)
        20616   LOAD_CONST                    0: 0
        20618   STORE_NAME                    397: PE_Mult
        20622   LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        20624   LOAD_CONST                    341: 'NQ'
        20628   BINARY_SUBSCR                 
        20630   LOAD_METHOD                   390: sum
        20634   CALL_METHOD                   0
        20636   LOAD_CONST                    0: 0
        20638   COMPARE_OP                    3 (!=)
        20640   POP_JUMP_IF_FALSE             10326 (to 20652)
        20644   LOAD_CONST                    29: 1
        20646   STORE_NAME                    398: CE_Hedge_Mult
        20650   JUMP_FORWARD                  3 (to 20658)
        20652   LOAD_CONST                    0: 0
        20654   STORE_NAME                    398: CE_Hedge_Mult
        20658   LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        20660   LOAD_CONST                    341: 'NQ'
        20664   BINARY_SUBSCR                 
        20666   LOAD_METHOD                   390: sum
        20670   CALL_METHOD                   0
        20672   LOAD_CONST                    0: 0
        20674   COMPARE_OP                    3 (!=)
        20676   POP_JUMP_IF_FALSE             10344 (to 20688)
        20680   LOAD_CONST                    29: 1
        20682   STORE_NAME                    399: PE_Hedge_Mult
        20686   JUMP_FORWARD                  3 (to 20694)
        20688   LOAD_CONST                    0: 0
        20690   STORE_NAME                    399: PE_Hedge_Mult
        20694   LOAD_NAME                     44: int
        20696   LOAD_NAME                     21: datetime
        20698   LOAD_ATTR                     21: datetime
        20700   LOAD_METHOD                   51: now
        20702   CALL_METHOD                   0
        20704   LOAD_METHOD                   52: strftime
        20706   LOAD_CONST                    50: '%H%M'
        20708   CALL_METHOD                   1
        20710   CALL_FUNCTION                 1
        20712   STORE_GLOBAL                  76: cur_HHMM
        20714   LOAD_NAME                     44: int
        20716   LOAD_NAME                     21: datetime
        20718   LOAD_ATTR                     21: datetime
        20720   LOAD_METHOD                   51: now
        20722   CALL_METHOD                   0
        20724   LOAD_METHOD                   52: strftime
        20726   LOAD_CONST                    291: '%H%M%S'
        20730   CALL_METHOD                   1
        20732   CALL_FUNCTION                 1
        20734   STORE_GLOBAL                  368: cur_HHMMSS
        20738   LOAD_GLOBAL                   170: King_Candle_Max_SL
        20740   LOAD_CONST                    20: True
        20742   COMPARE_OP                    2 (==)
        20744   POP_JUMP_IF_FALSE             10506 (to 21012)
        20748   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        20752   LOAD_GLOBAL                   89: NULL + int
        20754   COMPARE_OP                    1 (<=)
        20756   POP_JUMP_IF_FALSE             10506 (to 21012)
        20760   LOAD_GLOBAL                   236: expiry_Perlot_MTM_lock_profit
        20762   POP_JUMP_IF_TRUE              10506 (to 21012)
        20766   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        20768   STORE_NAME                    220: Paper_MTM_old
        20770   LOAD_NAME                     374: round
        20774   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        20776   LOAD_CONST                    372: 'MTM'
        20780   BINARY_SUBSCR                 
        20782   LOAD_METHOD                   390: sum
        20786   CALL_METHOD                   0
        20788   LOAD_NAME                     396: CE_Mult
        20792   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20796   BINARY_MULTIPLY               
        20798   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        20802   BINARY_MULTIPLY               
        20804   BINARY_ADD                    
        20806   LOAD_NAME                     397: PE_Mult
        20810   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20814   BINARY_MULTIPLY               
        20816   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        20820   BINARY_MULTIPLY               
        20822   BINARY_ADD                    
        20824   LOAD_NAME                     398: CE_Hedge_Mult
        20828   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20832   BINARY_MULTIPLY               
        20834   LOAD_GLOBAL                   266: expiry_Single_Leg_Adj_Delta_PCT
        20838   BINARY_MULTIPLY               
        20840   BINARY_ADD                    
        20842   LOAD_NAME                     399: PE_Hedge_Mult
        20846   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20850   BINARY_MULTIPLY               
        20852   LOAD_GLOBAL                   267: NULL + expiry_Single_Leg_Adj_Delta_PCT
        20856   BINARY_MULTIPLY               
        20858   BINARY_ADD                    
        20860   LOAD_CONST                    0: 0
        20862   CALL_FUNCTION                 2
        20864   STORE_GLOBAL                  219: Paper_MTM
        20866   LOAD_NAME                     375: abs
        20870   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        20872   LOAD_GLOBAL                   182: float
        20874   BINARY_SUBTRACT               
        20876   LOAD_GLOBAL                   79: NULL + get
        20878   BINARY_TRUE_DIVIDE            
        20880   LOAD_NAME                     220: Paper_MTM_old
        20882   LOAD_GLOBAL                   182: float
        20884   BINARY_SUBTRACT               
        20886   LOAD_GLOBAL                   79: NULL + get
        20888   BINARY_TRUE_DIVIDE            
        20890   BINARY_SUBTRACT               
        20892   CALL_FUNCTION                 1
        20894   LOAD_CONST                    373: 2000
        20898   COMPARE_OP                    4 (>)
        20900   POP_JUMP_IF_FALSE             10506 (to 21012)
        20904   LOAD_NAME                     2: time
        20906   LOAD_METHOD                   355: sleep
        20910   LOAD_CONST                    52: 2
        20912   CALL_METHOD                   1
        20914   POP_TOP                       
        20916   LOAD_NAME                     374: round
        20920   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        20922   LOAD_CONST                    372: 'MTM'
        20926   BINARY_SUBSCR                 
        20928   LOAD_METHOD                   390: sum
        20932   CALL_METHOD                   0
        20934   LOAD_NAME                     396: CE_Mult
        20938   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20942   BINARY_MULTIPLY               
        20944   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        20948   BINARY_MULTIPLY               
        20950   BINARY_ADD                    
        20952   LOAD_NAME                     397: PE_Mult
        20956   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20960   BINARY_MULTIPLY               
        20962   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        20966   BINARY_MULTIPLY               
        20968   BINARY_ADD                    
        20970   LOAD_NAME                     398: CE_Hedge_Mult
        20974   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20978   BINARY_MULTIPLY               
        20980   LOAD_GLOBAL                   266: expiry_Single_Leg_Adj_Delta_PCT
        20984   BINARY_MULTIPLY               
        20986   BINARY_ADD                    
        20988   LOAD_NAME                     399: PE_Hedge_Mult
        20992   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        20996   BINARY_MULTIPLY               
        20998   LOAD_GLOBAL                   267: NULL + expiry_Single_Leg_Adj_Delta_PCT
        21002   BINARY_MULTIPLY               
        21004   BINARY_ADD                    
        21006   LOAD_CONST                    0: 0
        21008   CALL_FUNCTION                 2
        21010   STORE_GLOBAL                  219: Paper_MTM
        21012   LOAD_GLOBAL                   170: King_Candle_Max_SL
        21014   LOAD_CONST                    20: True
        21016   COMPARE_OP                    2 (==)
        21018   POP_JUMP_IF_FALSE             10518 (to 21036)
        21022   LOAD_GLOBAL                   236: expiry_Perlot_MTM_lock_profit
        21024   POP_JUMP_IF_TRUE              10518 (to 21036)
        21028   LOAD_NAME                     325: check_MTM_Limit
        21032   CALL_FUNCTION                 0
        21034   STORE_NAME                    229: MTM
        21036   LOAD_NAME                     44: int
        21038   LOAD_NAME                     21: datetime
        21040   LOAD_ATTR                     21: datetime
        21042   LOAD_METHOD                   51: now
        21044   CALL_METHOD                   0
        21046   LOAD_METHOD                   52: strftime
        21048   LOAD_CONST                    50: '%H%M'
        21050   CALL_METHOD                   1
        21052   CALL_FUNCTION                 1
        21054   STORE_GLOBAL                  76: cur_HHMM
        21056   LOAD_NAME                     44: int
        21058   LOAD_NAME                     21: datetime
        21060   LOAD_ATTR                     21: datetime
        21062   LOAD_METHOD                   51: now
        21064   CALL_METHOD                   0
        21066   LOAD_METHOD                   52: strftime
        21068   LOAD_CONST                    291: '%H%M%S'
        21072   CALL_METHOD                   1
        21074   CALL_FUNCTION                 1
        21076   STORE_GLOBAL                  368: cur_HHMMSS
        21080   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        21084   LOAD_GLOBAL                   89: NULL + int
        21086   COMPARE_OP                    5 (>=)
        21088   POP_JUMP_IF_FALSE             10901 (to 21802)
        21092   LOAD_GLOBAL                   236: expiry_Perlot_MTM_lock_profit
        21094   POP_JUMP_IF_TRUE              10901 (to 21802)
        21098   LOAD_CONST                    374: ' ExitTime Triggered : closing all Trades'
        21102   STORE_NAME                    65: strMsg
        21104   LOAD_NAME                     59: iLog
        21106   LOAD_NAME                     65: strMsg
        21108   LOAD_CONST                    42: 4
        21110   LOAD_CONST                    20: True
        21112   LOAD_CONST                    43: ('sendTeleMsg',)
        21114   CALL_FUNCTION_KW              3
        21116   POP_TOP                       
        21118   LOAD_GLOBAL                   78: get
        21120   LOAD_CONST                    0: 0
        21122   COMPARE_OP                    2 (==)
        21124   POP_JUMP_IF_FALSE             10568 (to 21136)
        21128   LOAD_NAME                     322: close_all_orders
        21132   CALL_FUNCTION                 0
        21134   POP_TOP                       
        21136   LOAD_GLOBAL                   78: get
        21138   LOAD_CONST                    29: 1
        21140   COMPARE_OP                    2 (==)
        21142   POP_JUMP_IF_FALSE             10787 (to 21574)
        21146   LOAD_GLOBAL                   76: read
        21148   LOAD_GLOBAL                   360: PE_TGT_Triggered
        21152   LOAD_CONST                    0: 0
        21154   BINARY_SUBSCR                 
        21156   LOAD_GLOBAL                   360: PE_TGT_Triggered
        21160   LOAD_CONST                    29: 1
        21162   BINARY_SUBSCR                 
        21164   LOAD_CONST                    0: 0
        21166   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        21170   BINARY_MULTIPLY               
        21172   BUILD_LIST                    4
        21174   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        21176   LOAD_ATTR                     379: loc
        21180   LOAD_CONST                    0: 0
        21182   LOAD_NAME                     197: leg_cols
        21184   BUILD_TUPLE                   2
        21186   STORE_SUBSCR                  
        21188   LOAD_GLOBAL                   76: read
        21190   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        21194   LOAD_CONST                    0: 0
        21196   BINARY_SUBSCR                 
        21198   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        21202   LOAD_CONST                    29: 1
        21204   BINARY_SUBSCR                 
        21206   LOAD_CONST                    0: 0
        21208   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        21212   BINARY_MULTIPLY               
        21214   BUILD_LIST                    4
        21216   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        21218   LOAD_ATTR                     379: loc
        21222   LOAD_CONST                    0: 0
        21224   LOAD_NAME                     197: leg_cols
        21226   BUILD_TUPLE                   2
        21228   STORE_SUBSCR                  
        21230   LOAD_NAME                     24: pd
        21232   LOAD_METHOD                   380: concat
        21236   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        21238   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        21240   BUILD_LIST                    2
        21242   CALL_METHOD                   1
        21244   STORE_GLOBAL                  200: Current_legs
        21246   LOAD_GLOBAL                   200: normal_StikeAdj_SLPer
        21248   LOAD_METHOD                   400: to_csv
        21252   LOAD_CONST                    26: './log/'
        21254   LOAD_GLOBAL                   46: pandas
        21256   BINARY_ADD                    
        21258   LOAD_CONST                    375: '_Current_legs.txt'
        21262   BINARY_ADD                    
        21264   CALL_METHOD                   1
        21266   POP_TOP                       
        21268   LOAD_GLOBAL                   144: tl
        21270   LOAD_CONST                    29: 1
        21272   COMPARE_OP                    2 (==)
        21274   POP_JUMP_IF_FALSE             10700 (to 21400)
        21278   LOAD_GLOBAL                   76: read
        21280   LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        21284   LOAD_CONST                    0: 0
        21286   BINARY_SUBSCR                 
        21288   LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        21292   LOAD_CONST                    29: 1
        21294   BINARY_SUBSCR                 
        21296   LOAD_CONST                    0: 0
        21298   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        21302   BINARY_MULTIPLY               
        21304   BUILD_LIST                    4
        21306   LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        21308   LOAD_ATTR                     379: loc
        21312   LOAD_CONST                    0: 0
        21314   LOAD_NAME                     197: leg_cols
        21316   BUILD_TUPLE                   2
        21318   STORE_SUBSCR                  
        21320   LOAD_GLOBAL                   76: read
        21322   LOAD_GLOBAL                   364: partial_profit_booked
        21326   LOAD_CONST                    0: 0
        21328   BINARY_SUBSCR                 
        21330   LOAD_GLOBAL                   364: partial_profit_booked
        21334   LOAD_CONST                    29: 1
        21336   BINARY_SUBSCR                 
        21338   LOAD_CONST                    0: 0
        21340   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        21344   BINARY_MULTIPLY               
        21346   BUILD_LIST                    4
        21348   LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        21350   LOAD_ATTR                     379: loc
        21354   LOAD_CONST                    0: 0
        21356   LOAD_NAME                     197: leg_cols
        21358   BUILD_TUPLE                   2
        21360   STORE_SUBSCR                  
        21362   LOAD_NAME                     24: pd
        21364   LOAD_METHOD                   380: concat
        21368   LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        21370   LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        21372   BUILD_LIST                    2
        21374   CALL_METHOD                   1
        21376   STORE_GLOBAL                  203: Current_legs_hedge
        21378   LOAD_GLOBAL                   203: NULL + normal_StikeAdj_TgtPer
        21380   LOAD_METHOD                   400: to_csv
        21384   LOAD_CONST                    26: './log/'
        21386   LOAD_GLOBAL                   46: pandas
        21388   BINARY_ADD                    
        21390   LOAD_CONST                    376: '_Current_legs_hedge.txt'
        21394   BINARY_ADD                    
        21396   CALL_METHOD                   1
        21398   POP_TOP                       
        21400   LOAD_NAME                     44: int
        21402   LOAD_NAME                     21: datetime
        21404   LOAD_ATTR                     21: datetime
        21406   LOAD_METHOD                   51: now
        21408   CALL_METHOD                   0
        21410   LOAD_METHOD                   52: strftime
        21412   LOAD_CONST                    50: '%H%M'
        21414   CALL_METHOD                   1
        21416   CALL_FUNCTION                 1
        21418   STORE_GLOBAL                  76: cur_HHMM
        21420   LOAD_NAME                     44: int
        21422   LOAD_NAME                     21: datetime
        21424   LOAD_ATTR                     21: datetime
        21426   LOAD_METHOD                   51: now
        21428   CALL_METHOD                   0
        21430   LOAD_METHOD                   52: strftime
        21432   LOAD_CONST                    291: '%H%M%S'
        21436   CALL_METHOD                   1
        21438   CALL_FUNCTION                 1
        21440   STORE_GLOBAL                  368: cur_HHMMSS
        21444   LOAD_NAME                     56: open
        21446   LOAD_CONST                    377: './PNL/'
        21450   LOAD_GLOBAL                   46: pandas
        21452   BINARY_ADD                    
        21454   LOAD_CONST                    378: '_PNL.txt'
        21458   BINARY_ADD                    
        21460   LOAD_CONST                    28: 'a'
        21462   LOAD_CONST                    379: ''
        21466   LOAD_CONST                    380: ('newline',)
        21470   CALL_FUNCTION_KW              3
        21472   SETUP_WITH                    41
        21474   STORE_NAME                    401: f_object
        21478   LOAD_NAME                     8: writer
        21480   LOAD_NAME                     401: f_object
        21484   CALL_FUNCTION                 1
        21486   STORE_NAME                    402: writer_object
        21490   LOAD_NAME                     21: datetime
        21492   LOAD_ATTR                     21: datetime
        21494   LOAD_METHOD                   51: now
        21496   CALL_METHOD                   0
        21498   LOAD_METHOD                   52: strftime
        21500   LOAD_CONST                    24: '%Y%m%d'
        21502   CALL_METHOD                   1
        21504   LOAD_GLOBAL                   78: get
        21506   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        21508   BUILD_LIST                    3
        21510   STORE_NAME                    403: List
        21514   LOAD_NAME                     402: writer_object
        21518   LOAD_METHOD                   404: writerow
        21522   LOAD_NAME                     403: List
        21526   CALL_METHOD                   1
        21528   POP_TOP                       
        21530   LOAD_NAME                     401: f_object
        21534   LOAD_METHOD                   405: close
        21538   CALL_METHOD                   0
        21540   POP_TOP                       
        21542   POP_BLOCK                     
        21544   LOAD_CONST                    1: None
        21546   DUP_TOP                       
        21548   DUP_TOP                       
        21550   CALL_FUNCTION                 3
        21552   POP_TOP                       
        21554   JUMP_FORWARD                  9 (to 21574)
        21556   WITH_EXCEPT_START             
        21558   POP_JUMP_IF_TRUE              10782 (to 21564)
        21562   RERAISE                       1
        21564   POP_TOP                       
        21566   POP_TOP                       
        21568   POP_TOP                       
        21570   POP_EXCEPT                    
        21572   POP_TOP                       
        21574   LOAD_CONST                    20: True
        21576   STORE_GLOBAL                  236: processIndexExitTradenow
        21578   LOAD_CONST                    381: ' Current LTP = '
        21582   LOAD_NAME                     44: int
        21584   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        21586   LOAD_CONST                    292: -1
        21590   BINARY_SUBSCR                 
        21592   CALL_FUNCTION                 1
        21594   FORMAT_VALUE                  0
        21596   LOAD_CONST                    313: ', '
        21600   LOAD_GLOBAL                   381: NULL + df_king_cnt
        21604   FORMAT_VALUE                  0
        21606   LOAD_CONST                    382: ' ATM CE = ('
        21610   LOAD_GLOBAL                   252: ST_Close
        21612   FORMAT_VALUE                  0
        21614   LOAD_CONST                    303: ','
        21618   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        21622   FORMAT_VALUE                  0
        21624   LOAD_CONST                    303: ','
        21628   LOAD_GLOBAL                   250: ST_Mult
        21630   FORMAT_VALUE                  0
        21632   LOAD_CONST                    383: '), '
        21636   LOAD_GLOBAL                   382: df_cols
        21640   FORMAT_VALUE                  0
        21642   LOAD_CONST                    384: ' ATM PE = ('
        21646   LOAD_GLOBAL                   253: NULL + ST_Close
        21648   FORMAT_VALUE                  0
        21650   LOAD_CONST                    303: ','
        21654   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        21658   FORMAT_VALUE                  0
        21660   LOAD_CONST                    303: ','
        21664   LOAD_GLOBAL                   251: NULL + ST_Mult
        21666   FORMAT_VALUE                  0
        21668   LOAD_CONST                    385: '),MTM SL='
        21672   LOAD_NAME                     374: round
        21676   LOAD_GLOBAL                   182: float
        21678   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        21680   LOAD_GLOBAL                   79: NULL + get
        21682   BINARY_MULTIPLY               
        21684   BINARY_ADD                    
        21686   LOAD_CONST                    0: 0
        21688   CALL_FUNCTION                 2
        21690   FORMAT_VALUE                  0
        21692   LOAD_CONST                    386: ',MTM TGT='
        21696   LOAD_NAME                     374: round
        21700   LOAD_GLOBAL                   182: float
        21702   LOAD_GLOBAL                   240: RSI_Low
        21704   LOAD_GLOBAL                   79: NULL + get
        21706   BINARY_MULTIPLY               
        21708   BINARY_ADD                    
        21710   LOAD_CONST                    0: 0
        21712   CALL_FUNCTION                 2
        21714   FORMAT_VALUE                  0
        21716   LOAD_CONST                    387: ', Calc MTM = '
        21720   LOAD_NAME                     374: round
        21724   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        21726   LOAD_CONST                    0: 0
        21728   CALL_FUNCTION                 2
        21730   FORMAT_VALUE                  0
        21732   BUILD_STRING                  24
        21734   STORE_NAME                    65: strMsg
        21736   LOAD_NAME                     59: iLog
        21738   LOAD_NAME                     65: strMsg
        21740   LOAD_CONST                    20: True
        21742   LOAD_CONST                    43: ('sendTeleMsg',)
        21744   CALL_FUNCTION_KW              2
        21746   POP_TOP                       
        21748   LOAD_NAME                     61: set_config_value
        21750   LOAD_CONST                    48: 'status'
        21752   LOAD_CONST                    49: 'algo_running_status'
        21754   LOAD_CONST                    122: '0'
        21756   CALL_FUNCTION                 3
        21758   POP_TOP                       
        21760   LOAD_NAME                     62: savedata
        21762   CALL_FUNCTION                 0
        21764   POP_TOP                       
        21766   LOAD_NAME                     59: iLog
        21768   LOAD_CONST                    267: ' Shutter down... Calling sys.exit() @ '
        21772   LOAD_NAME                     343: str
        21776   LOAD_GLOBAL                   76: read
        21778   CALL_FUNCTION                 1
        21780   BINARY_ADD                    
        21782   LOAD_CONST                    42: 4
        21784   LOAD_CONST                    20: True
        21786   LOAD_CONST                    43: ('sendTeleMsg',)
        21788   CALL_FUNCTION_KW              3
        21790   POP_TOP                       
        21792   LOAD_NAME                     0: sys
        21794   LOAD_METHOD                   344: exit
        21798   CALL_METHOD                   0
        21800   POP_TOP                       
        21802   LOAD_NAME                     21: datetime
        21804   LOAD_ATTR                     21: datetime
        21806   LOAD_METHOD                   51: now
        21808   CALL_METHOD                   0
        21810   LOAD_ATTR                     372: minute
        21814   STORE_NAME                    207: cur_min
        21816   LOAD_NAME                     207: cur_min
        21818   LOAD_GLOBAL                   159: NULL + no_of_lots
        21820   BINARY_MODULO                 
        21822   LOAD_CONST                    0: 0
        21824   COMPARE_OP                    2 (==)
        21826   POP_JUMP_IF_FALSE             11435 (to 22870)
        21830   LOAD_NAME                     210: log_min
        21832   LOAD_NAME                     207: cur_min
        21834   COMPARE_OP                    3 (!=)
        21836   POP_JUMP_IF_FALSE             11435 (to 22870)
        21840   LOAD_GLOBAL                   160: ExitTradenow
        21842   LOAD_CONST                    0: 0
        21844   COMPARE_OP                    2 (==)
        21846   POP_JUMP_IF_FALSE             11435 (to 22870)
        21850   LOAD_NAME                     207: cur_min
        21852   STORE_NAME                    210: log_min
        21854   LOAD_NAME                     2: time
        21856   LOAD_METHOD                   2: time
        21858   CALL_METHOD                   0
        21860   STORE_NAME                    373: t1
        21864   LOAD_GLOBAL                   170: King_Candle_Max_SL
        21866   LOAD_CONST                    20: True
        21868   COMPARE_OP                    2 (==)
        21870   POP_JUMP_IF_FALSE             11391 (to 22782)
        21874   LOAD_GLOBAL                   248: ST_Period
        21876   LOAD_CONST                    0: 0
        21878   COMPARE_OP                    2 (==)
        21880   POP_JUMP_IF_TRUE              10969 (to 21938)
        21884   LOAD_GLOBAL                   248: ST_Period
        21886   LOAD_CONST                    29: 1
        21888   COMPARE_OP                    2 (==)
        21890   POP_JUMP_IF_FALSE             11074 (to 22148)
        21894   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        21896   LOAD_CONST                    341: 'NQ'
        21900   BINARY_SUBSCR                 
        21902   LOAD_METHOD                   390: sum
        21906   CALL_METHOD                   0
        21908   LOAD_CONST                    0: 0
        21910   COMPARE_OP                    3 (!=)
        21912   POP_JUMP_IF_FALSE             11074 (to 22148)
        21916   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        21918   LOAD_CONST                    341: 'NQ'
        21922   BINARY_SUBSCR                 
        21924   LOAD_METHOD                   390: sum
        21928   CALL_METHOD                   0
        21930   LOAD_CONST                    0: 0
        21932   COMPARE_OP                    3 (!=)
        21934   POP_JUMP_IF_FALSE             11074 (to 22148)
        21938   LOAD_CONST                    388: ' Legs(CE,PE)=('
        21942   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        21944   LOAD_CONST                    341: 'NQ'
        21948   BINARY_SUBSCR                 
        21950   LOAD_METHOD                   390: sum
        21954   CALL_METHOD                   0
        21956   FORMAT_VALUE                  0
        21958   LOAD_CONST                    303: ','
        21962   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        21964   LOAD_CONST                    341: 'NQ'
        21968   BINARY_SUBSCR                 
        21970   LOAD_METHOD                   390: sum
        21974   CALL_METHOD                   0
        21976   FORMAT_VALUE                  0
        21978   LOAD_CONST                    389: ') LTP= '
        21982   LOAD_NAME                     44: int
        21984   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        21986   LOAD_CONST                    292: -1
        21990   BINARY_SUBSCR                 
        21992   CALL_FUNCTION                 1
        21994   FORMAT_VALUE                  0
        21996   LOAD_CONST                    303: ','
        22000   LOAD_GLOBAL                   381: NULL + df_king_cnt
        22004   FORMAT_VALUE                  0
        22006   LOAD_CONST                    390: ' ATM CE=('
        22010   LOAD_GLOBAL                   252: ST_Close
        22012   FORMAT_VALUE                  0
        22014   LOAD_CONST                    303: ','
        22018   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        22022   FORMAT_VALUE                  0
        22024   LOAD_CONST                    303: ','
        22028   LOAD_GLOBAL                   250: ST_Mult
        22030   FORMAT_VALUE                  0
        22032   LOAD_CONST                    391: '),'
        22036   LOAD_GLOBAL                   382: df_cols
        22040   FORMAT_VALUE                  0
        22042   LOAD_CONST                    384: ' ATM PE = ('
        22046   LOAD_GLOBAL                   253: NULL + ST_Close
        22048   FORMAT_VALUE                  0
        22050   LOAD_CONST                    303: ','
        22054   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        22058   FORMAT_VALUE                  0
        22060   LOAD_CONST                    303: ','
        22064   LOAD_GLOBAL                   251: NULL + ST_Mult
        22066   FORMAT_VALUE                  0
        22068   LOAD_CONST                    385: '),MTM SL='
        22072   LOAD_NAME                     374: round
        22076   LOAD_GLOBAL                   182: float
        22078   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        22080   LOAD_GLOBAL                   79: NULL + get
        22082   BINARY_MULTIPLY               
        22084   BINARY_ADD                    
        22086   LOAD_CONST                    0: 0
        22088   CALL_FUNCTION                 2
        22090   FORMAT_VALUE                  0
        22092   LOAD_CONST                    386: ',MTM TGT='
        22096   LOAD_NAME                     374: round
        22100   LOAD_GLOBAL                   182: float
        22102   LOAD_GLOBAL                   240: RSI_Low
        22104   LOAD_GLOBAL                   79: NULL + get
        22106   BINARY_MULTIPLY               
        22108   BINARY_ADD                    
        22110   LOAD_CONST                    0: 0
        22112   CALL_FUNCTION                 2
        22114   FORMAT_VALUE                  0
        22116   LOAD_CONST                    392: ',MTM= '
        22120   LOAD_NAME                     374: round
        22124   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        22126   LOAD_CONST                    0: 0
        22128   CALL_FUNCTION                 2
        22130   FORMAT_VALUE                  0
        22132   BUILD_STRING                  28
        22134   STORE_NAME                    65: strMsg
        22136   LOAD_NAME                     59: iLog
        22138   LOAD_NAME                     65: strMsg
        22140   LOAD_CONST                    20: True
        22142   LOAD_CONST                    43: ('sendTeleMsg',)
        22144   CALL_FUNCTION_KW              2
        22146   POP_TOP                       
        22148   LOAD_GLOBAL                   248: ST_Period
        22150   LOAD_CONST                    29: 1
        22152   COMPARE_OP                    2 (==)
        22154   POP_JUMP_IF_FALSE             11233 (to 22466)
        22158   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        22160   LOAD_CONST                    341: 'NQ'
        22164   BINARY_SUBSCR                 
        22166   LOAD_METHOD                   390: sum
        22170   CALL_METHOD                   0
        22172   LOAD_CONST                    0: 0
        22174   COMPARE_OP                    3 (!=)
        22176   POP_JUMP_IF_FALSE             11233 (to 22466)
        22180   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        22182   LOAD_CONST                    341: 'NQ'
        22186   BINARY_SUBSCR                 
        22188   LOAD_METHOD                   390: sum
        22192   CALL_METHOD                   0
        22194   LOAD_CONST                    0: 0
        22196   COMPARE_OP                    2 (==)
        22198   POP_JUMP_IF_FALSE             11233 (to 22466)
        22202   LOAD_NAME                     406: min
        22206   LOAD_GLOBAL                   381: NULL + df_king_cnt
        22210   LOAD_GLOBAL                   108: kernel32
        22212   BINARY_SUBTRACT               
        22214   LOAD_GLOBAL                   157: NULL + papertrade
        22216   BINARY_ADD                    
        22218   LOAD_GLOBAL                   382: df_cols
        22222   LOAD_GLOBAL                   109: NULL + kernel32
        22224   BINARY_ADD                    
        22226   LOAD_GLOBAL                   157: NULL + papertrade
        22228   UNARY_POSITIVE                
        22230   BINARY_ADD                    
        22232   LOAD_GLOBAL                   382: df_cols
        22236   LOAD_GLOBAL                   109: NULL + kernel32
        22238   BINARY_ADD                    
        22240   LOAD_NAME                     44: int
        22242   LOAD_GLOBAL                   382: df_cols
        22246   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        22250   BINARY_SUBTRACT               
        22252   LOAD_GLOBAL                   109: NULL + kernel32
        22254   BINARY_ADD                    
        22256   CALL_FUNCTION                 1
        22258   LOAD_CONST                    73: 100
        22260   LOAD_GLOBAL                   249: NULL + ST_Period
        22262   BINARY_SUBTRACT               
        22264   BINARY_MULTIPLY               
        22266   LOAD_CONST                    73: 100
        22268   BINARY_TRUE_DIVIDE            
        22270   BINARY_SUBTRACT               
        22272   CALL_FUNCTION                 3
        22274   STORE_NAME                    407: Reentry_LTP
        22278   LOAD_CONST                    388: ' Legs(CE,PE)=('
        22282   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        22284   LOAD_CONST                    341: 'NQ'
        22288   BINARY_SUBSCR                 
        22290   LOAD_METHOD                   390: sum
        22294   CALL_METHOD                   0
        22296   FORMAT_VALUE                  0
        22298   LOAD_CONST                    303: ','
        22302   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        22304   LOAD_CONST                    341: 'NQ'
        22308   BINARY_SUBSCR                 
        22310   LOAD_METHOD                   390: sum
        22314   CALL_METHOD                   0
        22316   FORMAT_VALUE                  0
        22318   LOAD_CONST                    389: ') LTP= '
        22322   LOAD_NAME                     44: int
        22324   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        22326   LOAD_CONST                    292: -1
        22330   BINARY_SUBSCR                 
        22332   CALL_FUNCTION                 1
        22334   FORMAT_VALUE                  0
        22336   LOAD_CONST                    393: ' Reentry LTP : '
        22340   LOAD_NAME                     44: int
        22342   LOAD_NAME                     407: Reentry_LTP
        22346   CALL_FUNCTION                 1
        22348   FORMAT_VALUE                  0
        22350   LOAD_CONST                    394: ' , '
        22354   LOAD_GLOBAL                   381: NULL + df_king_cnt
        22358   FORMAT_VALUE                  0
        22360   LOAD_CONST                    395: '  ATM CE=('
        22364   LOAD_GLOBAL                   252: ST_Close
        22366   FORMAT_VALUE                  0
        22368   LOAD_CONST                    303: ','
        22372   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        22376   FORMAT_VALUE                  0
        22378   LOAD_CONST                    303: ','
        22382   LOAD_GLOBAL                   250: ST_Mult
        22384   FORMAT_VALUE                  0
        22386   LOAD_CONST                    385: '),MTM SL='
        22390   LOAD_NAME                     374: round
        22394   LOAD_GLOBAL                   182: float
        22396   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        22398   LOAD_GLOBAL                   79: NULL + get
        22400   BINARY_MULTIPLY               
        22402   BINARY_ADD                    
        22404   LOAD_CONST                    0: 0
        22406   CALL_FUNCTION                 2
        22408   FORMAT_VALUE                  0
        22410   LOAD_CONST                    386: ',MTM TGT='
        22414   LOAD_NAME                     374: round
        22418   LOAD_GLOBAL                   182: float
        22420   LOAD_GLOBAL                   240: RSI_Low
        22422   LOAD_GLOBAL                   79: NULL + get
        22424   BINARY_MULTIPLY               
        22426   BINARY_ADD                    
        22428   LOAD_CONST                    0: 0
        22430   CALL_FUNCTION                 2
        22432   FORMAT_VALUE                  0
        22434   LOAD_CONST                    392: ',MTM= '
        22438   LOAD_NAME                     374: round
        22442   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        22444   LOAD_CONST                    0: 0
        22446   CALL_FUNCTION                 2
        22448   FORMAT_VALUE                  0
        22450   BUILD_STRING                  22
        22452   STORE_NAME                    65: strMsg
        22454   LOAD_NAME                     59: iLog
        22456   LOAD_NAME                     65: strMsg
        22458   LOAD_CONST                    20: True
        22460   LOAD_CONST                    43: ('sendTeleMsg',)
        22462   CALL_FUNCTION_KW              2
        22464   POP_TOP                       
        22466   LOAD_GLOBAL                   248: ST_Period
        22468   LOAD_CONST                    29: 1
        22470   COMPARE_OP                    2 (==)
        22472   POP_JUMP_IF_FALSE             11391 (to 22782)
        22476   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        22478   LOAD_CONST                    341: 'NQ'
        22482   BINARY_SUBSCR                 
        22484   LOAD_METHOD                   390: sum
        22488   CALL_METHOD                   0
        22490   LOAD_CONST                    0: 0
        22492   COMPARE_OP                    2 (==)
        22494   POP_JUMP_IF_FALSE             11391 (to 22782)
        22498   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        22500   LOAD_CONST                    341: 'NQ'
        22504   BINARY_SUBSCR                 
        22506   LOAD_METHOD                   390: sum
        22510   CALL_METHOD                   0
        22512   LOAD_CONST                    0: 0
        22514   COMPARE_OP                    3 (!=)
        22516   POP_JUMP_IF_FALSE             11391 (to 22782)
        22520   LOAD_NAME                     391: max
        22524   LOAD_GLOBAL                   381: NULL + df_king_cnt
        22528   LOAD_GLOBAL                   108: kernel32
        22530   BINARY_SUBTRACT               
        22532   LOAD_GLOBAL                   157: NULL + papertrade
        22534   BINARY_SUBTRACT               
        22536   LOAD_GLOBAL                   382: df_cols
        22540   LOAD_GLOBAL                   109: NULL + kernel32
        22542   BINARY_ADD                    
        22544   LOAD_GLOBAL                   157: NULL + papertrade
        22546   BINARY_SUBTRACT               
        22548   LOAD_GLOBAL                   381: NULL + df_king_cnt
        22552   LOAD_GLOBAL                   108: kernel32
        22554   BINARY_SUBTRACT               
        22556   LOAD_NAME                     44: int
        22558   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        22562   LOAD_GLOBAL                   108: kernel32
        22564   BINARY_ADD                    
        22566   LOAD_GLOBAL                   381: NULL + df_king_cnt
        22570   BINARY_SUBTRACT               
        22572   CALL_FUNCTION                 1
        22574   LOAD_CONST                    73: 100
        22576   LOAD_GLOBAL                   249: NULL + ST_Period
        22578   BINARY_SUBTRACT               
        22580   BINARY_MULTIPLY               
        22582   LOAD_CONST                    73: 100
        22584   BINARY_TRUE_DIVIDE            
        22586   BINARY_ADD                    
        22588   CALL_FUNCTION                 3
        22590   STORE_NAME                    407: Reentry_LTP
        22594   LOAD_CONST                    388: ' Legs(CE,PE)=('
        22598   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        22600   LOAD_CONST                    341: 'NQ'
        22604   BINARY_SUBSCR                 
        22606   LOAD_METHOD                   390: sum
        22610   CALL_METHOD                   0
        22612   FORMAT_VALUE                  0
        22614   LOAD_CONST                    303: ','
        22618   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        22620   LOAD_CONST                    341: 'NQ'
        22624   BINARY_SUBSCR                 
        22626   LOAD_METHOD                   390: sum
        22630   CALL_METHOD                   0
        22632   FORMAT_VALUE                  0
        22634   LOAD_CONST                    389: ') LTP= '
        22638   LOAD_NAME                     44: int
        22640   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        22642   LOAD_CONST                    292: -1
        22646   BINARY_SUBSCR                 
        22648   CALL_FUNCTION                 1
        22650   FORMAT_VALUE                  0
        22652   LOAD_CONST                    393: ' Reentry LTP : '
        22656   LOAD_NAME                     44: int
        22658   LOAD_NAME                     407: Reentry_LTP
        22662   CALL_FUNCTION                 1
        22664   FORMAT_VALUE                  0
        22666   LOAD_CONST                    394: ' , '
        22670   LOAD_GLOBAL                   382: df_cols
        22674   FORMAT_VALUE                  0
        22676   LOAD_CONST                    396: '  ATM PE=('
        22680   LOAD_GLOBAL                   253: NULL + ST_Close
        22682   FORMAT_VALUE                  0
        22684   LOAD_CONST                    303: ','
        22688   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        22692   FORMAT_VALUE                  0
        22694   LOAD_CONST                    303: ','
        22698   LOAD_GLOBAL                   251: NULL + ST_Mult
        22700   FORMAT_VALUE                  0
        22702   LOAD_CONST                    385: '),MTM SL='
        22706   LOAD_NAME                     374: round
        22710   LOAD_GLOBAL                   182: float
        22712   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        22714   LOAD_GLOBAL                   79: NULL + get
        22716   BINARY_MULTIPLY               
        22718   BINARY_ADD                    
        22720   LOAD_CONST                    0: 0
        22722   CALL_FUNCTION                 2
        22724   FORMAT_VALUE                  0
        22726   LOAD_CONST                    386: ',MTM TGT='
        22730   LOAD_NAME                     374: round
        22734   LOAD_GLOBAL                   182: float
        22736   LOAD_GLOBAL                   240: RSI_Low
        22738   LOAD_GLOBAL                   79: NULL + get
        22740   BINARY_MULTIPLY               
        22742   BINARY_ADD                    
        22744   LOAD_CONST                    0: 0
        22746   CALL_FUNCTION                 2
        22748   FORMAT_VALUE                  0
        22750   LOAD_CONST                    392: ',MTM= '
        22754   LOAD_NAME                     374: round
        22758   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        22760   LOAD_CONST                    0: 0
        22762   CALL_FUNCTION                 2
        22764   FORMAT_VALUE                  0
        22766   BUILD_STRING                  22
        22768   STORE_NAME                    65: strMsg
        22770   LOAD_NAME                     59: iLog
        22772   LOAD_NAME                     65: strMsg
        22774   LOAD_CONST                    20: True
        22776   LOAD_CONST                    43: ('sendTeleMsg',)
        22778   CALL_FUNCTION_KW              2
        22780   POP_TOP                       
        22782   LOAD_GLOBAL                   170: King_Candle_Max_SL
        22784   LOAD_CONST                    30: False
        22786   COMPARE_OP                    2 (==)
        22788   POP_JUMP_IF_FALSE             11435 (to 22870)
        22792   LOAD_CONST                    397: ' LTP = '
        22796   LOAD_NAME                     44: int
        22798   LOAD_NAME                     91: float
        22800   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        22802   LOAD_CONST                    292: -1
        22806   BINARY_SUBSCR                 
        22808   CALL_FUNCTION                 1
        22810   CALL_FUNCTION                 1
        22812   FORMAT_VALUE                  0
        22814   LOAD_CONST                    313: ', '
        22818   LOAD_GLOBAL                   381: NULL + df_king_cnt
        22822   FORMAT_VALUE                  0
        22824   LOAD_CONST                    398: ' ATM CE = '
        22828   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        22832   FORMAT_VALUE                  0
        22834   LOAD_CONST                    313: ', '
        22838   LOAD_GLOBAL                   382: df_cols
        22842   FORMAT_VALUE                  0
        22844   LOAD_CONST                    399: ' ATM PE = '
        22848   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        22852   FORMAT_VALUE                  0
        22854   BUILD_STRING                  10
        22856   STORE_NAME                    65: strMsg
        22858   LOAD_NAME                     59: iLog
        22860   LOAD_NAME                     65: strMsg
        22862   LOAD_CONST                    30: False
        22864   LOAD_CONST                    43: ('sendTeleMsg',)
        22866   CALL_FUNCTION_KW              2
        22868   POP_TOP                       
        22870   LOAD_GLOBAL                   160: ExitTradenow
        22872   LOAD_CONST                    29: 1
        22874   COMPARE_OP                    2 (==)
        22876   POP_JUMP_IF_FALSE             11934 (to 23868)
        22880   LOAD_GLOBAL                   170: King_Candle_Max_SL
        22882   LOAD_CONST                    20: True
        22884   COMPARE_OP                    2 (==)
        22886   POP_JUMP_IF_FALSE             11890 (to 23780)
        22890   LOAD_GLOBAL                   248: ST_Period
        22892   LOAD_CONST                    0: 0
        22894   COMPARE_OP                    2 (==)
        22896   POP_JUMP_IF_TRUE              11477 (to 22954)
        22900   LOAD_GLOBAL                   248: ST_Period
        22902   LOAD_CONST                    29: 1
        22904   COMPARE_OP                    2 (==)
        22906   POP_JUMP_IF_FALSE             11582 (to 23164)
        22910   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        22912   LOAD_CONST                    341: 'NQ'
        22916   BINARY_SUBSCR                 
        22918   LOAD_METHOD                   390: sum
        22922   CALL_METHOD                   0
        22924   LOAD_CONST                    0: 0
        22926   COMPARE_OP                    3 (!=)
        22928   POP_JUMP_IF_FALSE             11582 (to 23164)
        22932   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        22934   LOAD_CONST                    341: 'NQ'
        22938   BINARY_SUBSCR                 
        22940   LOAD_METHOD                   390: sum
        22944   CALL_METHOD                   0
        22946   LOAD_CONST                    0: 0
        22948   COMPARE_OP                    3 (!=)
        22950   POP_JUMP_IF_FALSE             11582 (to 23164)
        22954   LOAD_CONST                    388: ' Legs(CE,PE)=('
        22958   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        22960   LOAD_CONST                    341: 'NQ'
        22964   BINARY_SUBSCR                 
        22966   LOAD_METHOD                   390: sum
        22970   CALL_METHOD                   0
        22972   FORMAT_VALUE                  0
        22974   LOAD_CONST                    303: ','
        22978   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        22980   LOAD_CONST                    341: 'NQ'
        22984   BINARY_SUBSCR                 
        22986   LOAD_METHOD                   390: sum
        22990   CALL_METHOD                   0
        22992   FORMAT_VALUE                  0
        22994   LOAD_CONST                    389: ') LTP= '
        22998   LOAD_NAME                     44: int
        23000   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        23002   LOAD_CONST                    292: -1
        23006   BINARY_SUBSCR                 
        23008   CALL_FUNCTION                 1
        23010   FORMAT_VALUE                  0
        23012   LOAD_CONST                    303: ','
        23016   LOAD_GLOBAL                   381: NULL + df_king_cnt
        23020   FORMAT_VALUE                  0
        23022   LOAD_CONST                    390: ' ATM CE=('
        23026   LOAD_GLOBAL                   252: ST_Close
        23028   FORMAT_VALUE                  0
        23030   LOAD_CONST                    303: ','
        23034   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        23038   FORMAT_VALUE                  0
        23040   LOAD_CONST                    303: ','
        23044   LOAD_GLOBAL                   250: ST_Mult
        23046   FORMAT_VALUE                  0
        23048   LOAD_CONST                    391: '),'
        23052   LOAD_GLOBAL                   382: df_cols
        23056   FORMAT_VALUE                  0
        23058   LOAD_CONST                    384: ' ATM PE = ('
        23062   LOAD_GLOBAL                   253: NULL + ST_Close
        23064   FORMAT_VALUE                  0
        23066   LOAD_CONST                    303: ','
        23070   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        23074   FORMAT_VALUE                  0
        23076   LOAD_CONST                    303: ','
        23080   LOAD_GLOBAL                   251: NULL + ST_Mult
        23082   FORMAT_VALUE                  0
        23084   LOAD_CONST                    385: '),MTM SL='
        23088   LOAD_NAME                     374: round
        23092   LOAD_GLOBAL                   182: float
        23094   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        23096   LOAD_GLOBAL                   79: NULL + get
        23098   BINARY_MULTIPLY               
        23100   BINARY_ADD                    
        23102   LOAD_CONST                    0: 0
        23104   CALL_FUNCTION                 2
        23106   FORMAT_VALUE                  0
        23108   LOAD_CONST                    386: ',MTM TGT='
        23112   LOAD_NAME                     374: round
        23116   LOAD_GLOBAL                   182: float
        23118   LOAD_GLOBAL                   240: RSI_Low
        23120   LOAD_GLOBAL                   79: NULL + get
        23122   BINARY_MULTIPLY               
        23124   BINARY_ADD                    
        23126   LOAD_CONST                    0: 0
        23128   CALL_FUNCTION                 2
        23130   FORMAT_VALUE                  0
        23132   LOAD_CONST                    392: ',MTM= '
        23136   LOAD_NAME                     374: round
        23140   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        23142   LOAD_CONST                    0: 0
        23144   CALL_FUNCTION                 2
        23146   FORMAT_VALUE                  0
        23148   BUILD_STRING                  28
        23150   STORE_NAME                    65: strMsg
        23152   LOAD_NAME                     59: iLog
        23154   LOAD_NAME                     65: strMsg
        23156   LOAD_CONST                    20: True
        23158   LOAD_CONST                    43: ('sendTeleMsg',)
        23160   CALL_FUNCTION_KW              2
        23162   POP_TOP                       
        23164   LOAD_GLOBAL                   248: ST_Period
        23166   LOAD_CONST                    29: 1
        23168   COMPARE_OP                    2 (==)
        23170   POP_JUMP_IF_FALSE             11736 (to 23472)
        23174   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        23176   LOAD_CONST                    341: 'NQ'
        23180   BINARY_SUBSCR                 
        23182   LOAD_METHOD                   390: sum
        23186   CALL_METHOD                   0
        23188   LOAD_CONST                    0: 0
        23190   COMPARE_OP                    3 (!=)
        23192   POP_JUMP_IF_FALSE             11736 (to 23472)
        23196   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        23198   LOAD_CONST                    341: 'NQ'
        23202   BINARY_SUBSCR                 
        23204   LOAD_METHOD                   390: sum
        23208   CALL_METHOD                   0
        23210   LOAD_CONST                    0: 0
        23212   COMPARE_OP                    2 (==)
        23214   POP_JUMP_IF_FALSE             11736 (to 23472)
        23218   LOAD_NAME                     406: min
        23222   LOAD_GLOBAL                   381: NULL + df_king_cnt
        23226   LOAD_GLOBAL                   108: kernel32
        23228   BINARY_SUBTRACT               
        23230   LOAD_GLOBAL                   382: df_cols
        23234   LOAD_GLOBAL                   109: NULL + kernel32
        23236   BINARY_ADD                    
        23238   LOAD_GLOBAL                   382: df_cols
        23242   LOAD_GLOBAL                   109: NULL + kernel32
        23244   BINARY_ADD                    
        23246   LOAD_NAME                     44: int
        23248   LOAD_GLOBAL                   382: df_cols
        23252   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        23256   BINARY_SUBTRACT               
        23258   LOAD_GLOBAL                   109: NULL + kernel32
        23260   BINARY_SUBTRACT               
        23262   CALL_FUNCTION                 1
        23264   LOAD_CONST                    73: 100
        23266   LOAD_GLOBAL                   249: NULL + ST_Period
        23268   BINARY_SUBTRACT               
        23270   BINARY_MULTIPLY               
        23272   LOAD_CONST                    73: 100
        23274   BINARY_TRUE_DIVIDE            
        23276   BINARY_SUBTRACT               
        23278   CALL_FUNCTION                 3
        23280   STORE_NAME                    407: Reentry_LTP
        23284   LOAD_CONST                    388: ' Legs(CE,PE)=('
        23288   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        23290   LOAD_CONST                    341: 'NQ'
        23294   BINARY_SUBSCR                 
        23296   LOAD_METHOD                   390: sum
        23300   CALL_METHOD                   0
        23302   FORMAT_VALUE                  0
        23304   LOAD_CONST                    303: ','
        23308   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        23310   LOAD_CONST                    341: 'NQ'
        23314   BINARY_SUBSCR                 
        23316   LOAD_METHOD                   390: sum
        23320   CALL_METHOD                   0
        23322   FORMAT_VALUE                  0
        23324   LOAD_CONST                    389: ') LTP= '
        23328   LOAD_NAME                     44: int
        23330   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        23332   LOAD_CONST                    292: -1
        23336   BINARY_SUBSCR                 
        23338   CALL_FUNCTION                 1
        23340   FORMAT_VALUE                  0
        23342   LOAD_CONST                    393: ' Reentry LTP : '
        23346   LOAD_NAME                     44: int
        23348   LOAD_NAME                     407: Reentry_LTP
        23352   CALL_FUNCTION                 1
        23354   FORMAT_VALUE                  0
        23356   LOAD_CONST                    394: ' , '
        23360   LOAD_GLOBAL                   381: NULL + df_king_cnt
        23364   FORMAT_VALUE                  0
        23366   LOAD_CONST                    395: '  ATM CE=('
        23370   LOAD_GLOBAL                   252: ST_Close
        23372   FORMAT_VALUE                  0
        23374   LOAD_CONST                    303: ','
        23378   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        23382   FORMAT_VALUE                  0
        23384   LOAD_CONST                    303: ','
        23388   LOAD_GLOBAL                   250: ST_Mult
        23390   FORMAT_VALUE                  0
        23392   LOAD_CONST                    385: '),MTM SL='
        23396   LOAD_NAME                     374: round
        23400   LOAD_GLOBAL                   182: float
        23402   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        23404   LOAD_GLOBAL                   79: NULL + get
        23406   BINARY_MULTIPLY               
        23408   BINARY_ADD                    
        23410   LOAD_CONST                    0: 0
        23412   CALL_FUNCTION                 2
        23414   FORMAT_VALUE                  0
        23416   LOAD_CONST                    386: ',MTM TGT='
        23420   LOAD_NAME                     374: round
        23424   LOAD_GLOBAL                   182: float
        23426   LOAD_GLOBAL                   240: RSI_Low
        23428   LOAD_GLOBAL                   79: NULL + get
        23430   BINARY_MULTIPLY               
        23432   BINARY_ADD                    
        23434   LOAD_CONST                    0: 0
        23436   CALL_FUNCTION                 2
        23438   FORMAT_VALUE                  0
        23440   LOAD_CONST                    392: ',MTM= '
        23444   LOAD_NAME                     374: round
        23448   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        23450   LOAD_CONST                    0: 0
        23452   CALL_FUNCTION                 2
        23454   FORMAT_VALUE                  0
        23456   BUILD_STRING                  22
        23458   STORE_NAME                    65: strMsg
        23460   LOAD_NAME                     59: iLog
        23462   LOAD_NAME                     65: strMsg
        23464   LOAD_CONST                    20: True
        23466   LOAD_CONST                    43: ('sendTeleMsg',)
        23468   CALL_FUNCTION_KW              2
        23470   POP_TOP                       
        23472   LOAD_GLOBAL                   248: ST_Period
        23474   LOAD_CONST                    29: 1
        23476   COMPARE_OP                    2 (==)
        23478   POP_JUMP_IF_FALSE             11890 (to 23780)
        23482   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        23484   LOAD_CONST                    341: 'NQ'
        23488   BINARY_SUBSCR                 
        23490   LOAD_METHOD                   390: sum
        23494   CALL_METHOD                   0
        23496   LOAD_CONST                    0: 0
        23498   COMPARE_OP                    2 (==)
        23500   POP_JUMP_IF_FALSE             11890 (to 23780)
        23504   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        23506   LOAD_CONST                    341: 'NQ'
        23510   BINARY_SUBSCR                 
        23512   LOAD_METHOD                   390: sum
        23516   CALL_METHOD                   0
        23518   LOAD_CONST                    0: 0
        23520   COMPARE_OP                    3 (!=)
        23522   POP_JUMP_IF_FALSE             11890 (to 23780)
        23526   LOAD_NAME                     391: max
        23530   LOAD_GLOBAL                   381: NULL + df_king_cnt
        23534   LOAD_GLOBAL                   108: kernel32
        23536   BINARY_SUBTRACT               
        23538   LOAD_GLOBAL                   382: df_cols
        23542   LOAD_GLOBAL                   109: NULL + kernel32
        23544   BINARY_ADD                    
        23546   LOAD_GLOBAL                   381: NULL + df_king_cnt
        23550   LOAD_GLOBAL                   108: kernel32
        23552   BINARY_SUBTRACT               
        23554   LOAD_NAME                     44: int
        23556   LOAD_NAME                     298: Single_Leg_Triggered_LTP
        23560   LOAD_GLOBAL                   108: kernel32
        23562   BINARY_ADD                    
        23564   LOAD_GLOBAL                   381: NULL + df_king_cnt
        23568   BINARY_SUBTRACT               
        23570   CALL_FUNCTION                 1
        23572   LOAD_CONST                    73: 100
        23574   LOAD_GLOBAL                   249: NULL + ST_Period
        23576   BINARY_SUBTRACT               
        23578   BINARY_MULTIPLY               
        23580   LOAD_CONST                    73: 100
        23582   BINARY_TRUE_DIVIDE            
        23584   BINARY_ADD                    
        23586   CALL_FUNCTION                 3
        23588   STORE_NAME                    407: Reentry_LTP
        23592   LOAD_CONST                    388: ' Legs(CE,PE)=('
        23596   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        23598   LOAD_CONST                    341: 'NQ'
        23602   BINARY_SUBSCR                 
        23604   LOAD_METHOD                   390: sum
        23608   CALL_METHOD                   0
        23610   FORMAT_VALUE                  0
        23612   LOAD_CONST                    303: ','
        23616   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        23618   LOAD_CONST                    341: 'NQ'
        23622   BINARY_SUBSCR                 
        23624   LOAD_METHOD                   390: sum
        23628   CALL_METHOD                   0
        23630   FORMAT_VALUE                  0
        23632   LOAD_CONST                    389: ') LTP= '
        23636   LOAD_NAME                     44: int
        23638   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        23640   LOAD_CONST                    292: -1
        23644   BINARY_SUBSCR                 
        23646   CALL_FUNCTION                 1
        23648   FORMAT_VALUE                  0
        23650   LOAD_CONST                    393: ' Reentry LTP : '
        23654   LOAD_NAME                     44: int
        23656   LOAD_NAME                     407: Reentry_LTP
        23660   CALL_FUNCTION                 1
        23662   FORMAT_VALUE                  0
        23664   LOAD_CONST                    394: ' , '
        23668   LOAD_GLOBAL                   382: df_cols
        23672   FORMAT_VALUE                  0
        23674   LOAD_CONST                    396: '  ATM PE=('
        23678   LOAD_GLOBAL                   253: NULL + ST_Close
        23680   FORMAT_VALUE                  0
        23682   LOAD_CONST                    303: ','
        23686   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        23690   FORMAT_VALUE                  0
        23692   LOAD_CONST                    303: ','
        23696   LOAD_GLOBAL                   251: NULL + ST_Mult
        23698   FORMAT_VALUE                  0
        23700   LOAD_CONST                    385: '),MTM SL='
        23704   LOAD_NAME                     374: round
        23708   LOAD_GLOBAL                   182: float
        23710   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        23712   LOAD_GLOBAL                   79: NULL + get
        23714   BINARY_MULTIPLY               
        23716   BINARY_ADD                    
        23718   LOAD_CONST                    0: 0
        23720   CALL_FUNCTION                 2
        23722   FORMAT_VALUE                  0
        23724   LOAD_CONST                    386: ',MTM TGT='
        23728   LOAD_NAME                     374: round
        23732   LOAD_GLOBAL                   182: float
        23734   LOAD_GLOBAL                   240: RSI_Low
        23736   LOAD_GLOBAL                   79: NULL + get
        23738   BINARY_MULTIPLY               
        23740   BINARY_ADD                    
        23742   LOAD_CONST                    0: 0
        23744   CALL_FUNCTION                 2
        23746   FORMAT_VALUE                  0
        23748   LOAD_CONST                    392: ',MTM= '
        23752   LOAD_NAME                     374: round
        23756   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        23758   LOAD_CONST                    0: 0
        23760   CALL_FUNCTION                 2
        23762   FORMAT_VALUE                  0
        23764   BUILD_STRING                  22
        23766   STORE_NAME                    65: strMsg
        23768   LOAD_NAME                     59: iLog
        23770   LOAD_NAME                     65: strMsg
        23772   LOAD_CONST                    20: True
        23774   LOAD_CONST                    43: ('sendTeleMsg',)
        23776   CALL_FUNCTION_KW              2
        23778   POP_TOP                       
        23780   LOAD_GLOBAL                   170: King_Candle_Max_SL
        23782   LOAD_CONST                    30: False
        23784   COMPARE_OP                    2 (==)
        23786   POP_JUMP_IF_FALSE             11934 (to 23868)
        23790   LOAD_CONST                    397: ' LTP = '
        23794   LOAD_NAME                     44: int
        23796   LOAD_NAME                     91: float
        23798   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        23800   LOAD_CONST                    292: -1
        23804   BINARY_SUBSCR                 
        23806   CALL_FUNCTION                 1
        23808   CALL_FUNCTION                 1
        23810   FORMAT_VALUE                  0
        23812   LOAD_CONST                    313: ', '
        23816   LOAD_GLOBAL                   381: NULL + df_king_cnt
        23820   FORMAT_VALUE                  0
        23822   LOAD_CONST                    398: ' ATM CE = '
        23826   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        23830   FORMAT_VALUE                  0
        23832   LOAD_CONST                    313: ', '
        23836   LOAD_GLOBAL                   382: df_cols
        23840   FORMAT_VALUE                  0
        23842   LOAD_CONST                    399: ' ATM PE = '
        23846   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        23850   FORMAT_VALUE                  0
        23852   BUILD_STRING                  10
        23854   STORE_NAME                    65: strMsg
        23856   LOAD_NAME                     59: iLog
        23858   LOAD_NAME                     65: strMsg
        23860   LOAD_CONST                    30: False
        23862   LOAD_CONST                    43: ('sendTeleMsg',)
        23864   CALL_FUNCTION_KW              2
        23866   POP_TOP                       
        23868   LOAD_NAME                     44: int
        23870   LOAD_NAME                     21: datetime
        23872   LOAD_ATTR                     21: datetime
        23874   LOAD_METHOD                   51: now
        23876   CALL_METHOD                   0
        23878   LOAD_METHOD                   52: strftime
        23880   LOAD_CONST                    50: '%H%M'
        23882   CALL_METHOD                   1
        23884   CALL_FUNCTION                 1
        23886   STORE_GLOBAL                  76: cur_HHMM
        23888   LOAD_NAME                     44: int
        23890   LOAD_NAME                     21: datetime
        23892   LOAD_ATTR                     21: datetime
        23894   LOAD_METHOD                   51: now
        23896   CALL_METHOD                   0
        23898   LOAD_METHOD                   52: strftime
        23900   LOAD_CONST                    291: '%H%M%S'
        23904   CALL_METHOD                   1
        23906   CALL_FUNCTION                 1
        23908   STORE_GLOBAL                  368: cur_HHMMSS
        23912   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        23916   LOAD_GLOBAL                   87: NULL + strBotTokenWObot
        23918   COMPARE_OP                    4 (>)
        23920   POP_JUMP_IF_FALSE             12121 (to 24242)
        23924   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        23928   LOAD_GLOBAL                   89: NULL + int
        23930   COMPARE_OP                    1 (<=)
        23932   POP_JUMP_IF_FALSE             12121 (to 24242)
        23936   LOAD_NAME                     21: datetime
        23938   LOAD_ATTR                     347: date
        23942   LOAD_METHOD                   348: today
        23946   CALL_METHOD                   0
        23948   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        23952   COMPARE_OP                    3 (!=)
        23954   POP_JUMP_IF_FALSE             11984 (to 23968)
        23958   LOAD_GLOBAL                   93: NULL + log_file_name
        23960   LOAD_CONST                    29: 1
        23962   COMPARE_OP                    2 (==)
        23964   POP_JUMP_IF_TRUE              12000 (to 24000)
        23968   LOAD_NAME                     21: datetime
        23970   LOAD_ATTR                     347: date
        23974   LOAD_METHOD                   348: today
        23978   CALL_METHOD                   0
        23980   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        23984   COMPARE_OP                    2 (==)
        23986   POP_JUMP_IF_FALSE             12121 (to 24242)
        23990   LOAD_GLOBAL                   92: log_file_name
        23992   LOAD_CONST                    29: 1
        23994   COMPARE_OP                    2 (==)
        23996   POP_JUMP_IF_FALSE             12121 (to 24242)
        24000   LOAD_GLOBAL                   236: expiry_Perlot_MTM_lock_profit
        24002   POP_JUMP_IF_TRUE              12121 (to 24242)
        24006   LOAD_GLOBAL                   173: NULL + time_offset_sec
        24008   LOAD_CONST                    20: True
        24010   COMPARE_OP                    2 (==)
        24012   POP_JUMP_IF_FALSE             12021 (to 24042)
        24016   LOAD_NAME                     44: int
        24018   LOAD_NAME                     91: float
        24020   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24022   LOAD_CONST                    292: -1
        24026   BINARY_SUBSCR                 
        24028   CALL_FUNCTION                 1
        24030   CALL_FUNCTION                 1
        24032   LOAD_GLOBAL                   268: partial_profit_booking_enable
        24036   COMPARE_OP                    4 (>)
        24038   POP_JUMP_IF_TRUE              12039 (to 24078)
        24042   LOAD_GLOBAL                   174: StraddleEntryTime
        24044   LOAD_CONST                    20: True
        24046   COMPARE_OP                    2 (==)
        24048   POP_JUMP_IF_FALSE             12062 (to 24124)
        24052   LOAD_NAME                     44: int
        24054   LOAD_NAME                     91: float
        24056   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24058   LOAD_CONST                    292: -1
        24062   BINARY_SUBSCR                 
        24064   CALL_FUNCTION                 1
        24066   CALL_FUNCTION                 1
        24068   LOAD_GLOBAL                   285: NULL + max_entry_time
        24072   COMPARE_OP                    0 (<)
        24074   POP_JUMP_IF_FALSE             12062 (to 24124)
        24078   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        24082   LOAD_CONST                    0: 0
        24084   COMPARE_OP                    2 (==)
        24086   POP_JUMP_IF_FALSE             12062 (to 24124)
        24090   LOAD_GLOBAL                   74: cfg
        24092   LOAD_GLOBAL                   162: Trade_Nifty
        24094   COMPARE_OP                    5 (>=)
        24096   POP_JUMP_IF_FALSE             12062 (to 24124)
        24100   LOAD_CONST                    400: ' Direction change: Max order_limit_per_day Reached. Exiting trade for the day '
        24104   STORE_NAME                    65: strMsg
        24106   LOAD_NAME                     59: iLog
        24108   LOAD_NAME                     65: strMsg
        24110   LOAD_CONST                    42: 4
        24112   LOAD_CONST                    20: True
        24114   LOAD_CONST                    43: ('sendTeleMsg',)
        24116   CALL_FUNCTION_KW              3
        24118   POP_TOP                       
        24120   LOAD_CONST                    29: 1
        24122   STORE_GLOBAL                  80: ExitTradenow
        24124   LOAD_GLOBAL                   173: NULL + time_offset_sec
        24126   LOAD_CONST                    20: True
        24128   COMPARE_OP                    2 (==)
        24130   POP_JUMP_IF_FALSE             12080 (to 24160)
        24134   LOAD_NAME                     44: int
        24136   LOAD_NAME                     91: float
        24138   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24140   LOAD_CONST                    292: -1
        24144   BINARY_SUBSCR                 
        24146   CALL_FUNCTION                 1
        24148   CALL_FUNCTION                 1
        24150   LOAD_GLOBAL                   268: partial_profit_booking_enable
        24154   COMPARE_OP                    4 (>)
        24156   POP_JUMP_IF_TRUE              12098 (to 24196)
        24160   LOAD_GLOBAL                   174: StraddleEntryTime
        24162   LOAD_CONST                    20: True
        24164   COMPARE_OP                    2 (==)
        24166   POP_JUMP_IF_FALSE             12121 (to 24242)
        24170   LOAD_NAME                     44: int
        24172   LOAD_NAME                     91: float
        24174   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24176   LOAD_CONST                    292: -1
        24180   BINARY_SUBSCR                 
        24182   CALL_FUNCTION                 1
        24184   CALL_FUNCTION                 1
        24186   LOAD_GLOBAL                   285: NULL + max_entry_time
        24190   COMPARE_OP                    0 (<)
        24192   POP_JUMP_IF_FALSE             12121 (to 24242)
        24196   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        24200   LOAD_CONST                    0: 0
        24202   COMPARE_OP                    2 (==)
        24204   POP_JUMP_IF_FALSE             12121 (to 24242)
        24208   LOAD_GLOBAL                   76: read
        24210   LOAD_GLOBAL                   90: Send_Telegram
        24212   COMPARE_OP                    5 (>=)
        24214   POP_JUMP_IF_FALSE             12121 (to 24242)
        24218   LOAD_CONST                    401: ' Direction change after MaxPositionChangeTime. Exiting trade for the day '
        24222   STORE_NAME                    65: strMsg
        24224   LOAD_NAME                     59: iLog
        24226   LOAD_NAME                     65: strMsg
        24228   LOAD_CONST                    42: 4
        24230   LOAD_CONST                    20: True
        24232   LOAD_CONST                    43: ('sendTeleMsg',)
        24234   CALL_FUNCTION_KW              3
        24236   POP_TOP                       
        24238   LOAD_CONST                    29: 1
        24240   STORE_GLOBAL                  80: ExitTradenow
        24242   LOAD_CONST                    42: 4
        24244   STORE_NAME                    408: algo_interval1
        24248   LOAD_CONST                    402: 9
        24252   STORE_NAME                    409: algo_interval2
        24256   LOAD_CONST                    403: 55
        24260   STORE_NAME                    410: algo_interval_sec
        24264   LOAD_NAME                     21: datetime
        24266   LOAD_ATTR                     21: datetime
        24268   LOAD_METHOD                   51: now
        24270   CALL_METHOD                   0
        24272   LOAD_ATTR                     372: minute
        24276   STORE_NAME                    411: cur_min1
        24280   LOAD_NAME                     21: datetime
        24282   LOAD_ATTR                     21: datetime
        24284   LOAD_METHOD                   51: now
        24286   CALL_METHOD                   0
        24288   LOAD_ATTR                     412: second
        24292   STORE_NAME                    413: cur_sec1
        24296   LOAD_GLOBAL                   127: NULL + getAccessToken
        24298   LOAD_CONST                    29: 1
        24300   COMPARE_OP                    2 (==)
        24302   POP_JUMP_IF_FALSE             12218 (to 24436)
        24306   LOAD_GLOBAL                   158: no_of_lots
        24308   LOAD_CONST                    288: 5
        24312   COMPARE_OP                    2 (==)
        24314   POP_JUMP_IF_FALSE             12198 (to 24396)
        24318   LOAD_NAME                     411: cur_min1
        24322   LOAD_CONST                    404: 10
        24326   BINARY_MODULO                 
        24328   LOAD_NAME                     408: algo_interval1
        24332   COMPARE_OP                    2 (==)
        24334   POP_JUMP_IF_TRUE              12179 (to 24358)
        24338   LOAD_NAME                     411: cur_min1
        24342   LOAD_CONST                    404: 10
        24346   BINARY_MODULO                 
        24348   LOAD_NAME                     409: algo_interval2
        24352   COMPARE_OP                    2 (==)
        24354   POP_JUMP_IF_FALSE             12198 (to 24396)
        24358   LOAD_NAME                     413: cur_sec1
        24362   LOAD_NAME                     410: algo_interval_sec
        24366   COMPARE_OP                    4 (>)
        24368   POP_JUMP_IF_FALSE             12198 (to 24396)
        24372   LOAD_NAME                     214: algo_sec1
        24374   LOAD_NAME                     413: cur_sec1
        24378   COMPARE_OP                    3 (!=)
        24380   POP_JUMP_IF_FALSE             12198 (to 24396)
        24384   LOAD_NAME                     212: algo_min1
        24386   LOAD_NAME                     411: cur_min1
        24390   COMPARE_OP                    3 (!=)
        24392   POP_JUMP_IF_TRUE              12237 (to 24474)
        24396   LOAD_GLOBAL                   158: no_of_lots
        24398   LOAD_CONST                    271: 3
        24402   COMPARE_OP                    2 (==)
        24404   POP_JUMP_IF_FALSE             12218 (to 24436)
        24408   LOAD_NAME                     411: cur_min1
        24412   LOAD_GLOBAL                   158: no_of_lots
        24414   BINARY_MODULO                 
        24416   LOAD_CONST                    0: 0
        24418   COMPARE_OP                    2 (==)
        24420   POP_JUMP_IF_FALSE             12218 (to 24436)
        24424   LOAD_NAME                     213: algo_3min
        24426   LOAD_NAME                     411: cur_min1
        24430   COMPARE_OP                    3 (!=)
        24432   POP_JUMP_IF_TRUE              12237 (to 24474)
        24436   LOAD_GLOBAL                   127: NULL + getAccessToken
        24438   LOAD_CONST                    29: 1
        24440   COMPARE_OP                    3 (!=)
        24442   POP_JUMP_IF_FALSE             14263 (to 28526)
        24446   LOAD_NAME                     411: cur_min1
        24450   LOAD_CONST                    29: 1
        24452   BINARY_MODULO                 
        24454   LOAD_CONST                    0: 0
        24456   COMPARE_OP                    2 (==)
        24458   POP_JUMP_IF_FALSE             14263 (to 28526)
        24462   LOAD_NAME                     212: algo_min1
        24464   LOAD_NAME                     411: cur_min1
        24468   COMPARE_OP                    3 (!=)
        24470   POP_JUMP_IF_FALSE             14263 (to 28526)
        24474   LOAD_NAME                     411: cur_min1
        24478   STORE_NAME                    212: algo_min1
        24480   LOAD_NAME                     413: cur_sec1
        24484   STORE_NAME                    214: algo_sec1
        24486   LOAD_NAME                     411: cur_min1
        24490   STORE_NAME                    213: algo_3min
        24492   LOAD_NAME                     44: int
        24494   LOAD_NAME                     21: datetime
        24496   LOAD_ATTR                     21: datetime
        24498   LOAD_METHOD                   51: now
        24500   CALL_METHOD                   0
        24502   LOAD_METHOD                   52: strftime
        24504   LOAD_CONST                    50: '%H%M'
        24506   CALL_METHOD                   1
        24508   CALL_FUNCTION                 1
        24510   STORE_GLOBAL                  76: cur_HHMM
        24512   LOAD_NAME                     44: int
        24514   LOAD_NAME                     21: datetime
        24516   LOAD_ATTR                     21: datetime
        24518   LOAD_METHOD                   51: now
        24520   CALL_METHOD                   0
        24522   LOAD_METHOD                   52: strftime
        24524   LOAD_CONST                    291: '%H%M%S'
        24528   CALL_METHOD                   1
        24530   CALL_FUNCTION                 1
        24532   STORE_GLOBAL                  368: cur_HHMMSS
        24536   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        24540   LOAD_GLOBAL                   87: NULL + strBotTokenWObot
        24542   COMPARE_OP                    4 (>)
        24544   POP_JUMP_IF_FALSE             14263 (to 28526)
        24548   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        24552   LOAD_GLOBAL                   89: NULL + int
        24554   COMPARE_OP                    1 (<=)
        24556   POP_JUMP_IF_FALSE             14263 (to 28526)
        24560   LOAD_NAME                     21: datetime
        24562   LOAD_ATTR                     347: date
        24566   LOAD_METHOD                   348: today
        24570   CALL_METHOD                   0
        24572   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        24576   COMPARE_OP                    3 (!=)
        24578   POP_JUMP_IF_FALSE             12296 (to 24592)
        24582   LOAD_GLOBAL                   93: NULL + log_file_name
        24584   LOAD_CONST                    29: 1
        24586   COMPARE_OP                    2 (==)
        24588   POP_JUMP_IF_TRUE              12312 (to 24624)
        24592   LOAD_NAME                     21: datetime
        24594   LOAD_ATTR                     347: date
        24598   LOAD_METHOD                   348: today
        24602   CALL_METHOD                   0
        24604   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        24608   COMPARE_OP                    2 (==)
        24610   POP_JUMP_IF_FALSE             14263 (to 28526)
        24614   LOAD_GLOBAL                   92: log_file_name
        24616   LOAD_CONST                    29: 1
        24618   COMPARE_OP                    2 (==)
        24620   POP_JUMP_IF_FALSE             14263 (to 28526)
        24624   LOAD_GLOBAL                   236: expiry_Perlot_MTM_lock_profit
        24626   POP_JUMP_IF_TRUE              14263 (to 28526)
        24630   LOAD_GLOBAL                   173: NULL + time_offset_sec
        24632   LOAD_CONST                    20: True
        24634   COMPARE_OP                    2 (==)
        24636   POP_JUMP_IF_FALSE             12409 (to 24818)
        24640   LOAD_NAME                     44: int
        24642   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24644   LOAD_CONST                    292: -1
        24648   BINARY_SUBSCR                 
        24650   CALL_FUNCTION                 1
        24652   LOAD_GLOBAL                   268: partial_profit_booking_enable
        24656   COMPARE_OP                    4 (>)
        24658   POP_JUMP_IF_FALSE             12409 (to 24818)
        24662   LOAD_GLOBAL                   126: getAccessToken
        24664   LOAD_CONST                    29: 1
        24666   COMPARE_OP                    2 (==)
        24668   POP_JUMP_IF_FALSE             12345 (to 24690)
        24672   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        24676   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        24680   LOAD_GLOBAL                   84: strBotToken
        24682   BINARY_ADD                    
        24684   COMPARE_OP                    4 (>)
        24686   POP_JUMP_IF_TRUE              12363 (to 24726)
        24690   LOAD_GLOBAL                   126: getAccessToken
        24692   LOAD_CONST                    29: 1
        24694   COMPARE_OP                    3 (!=)
        24696   POP_JUMP_IF_FALSE             12409 (to 24818)
        24700   LOAD_NAME                     44: int
        24702   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24704   LOAD_CONST                    292: -1
        24708   BINARY_SUBSCR                 
        24710   CALL_FUNCTION                 1
        24712   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        24716   LOAD_GLOBAL                   84: strBotToken
        24718   BINARY_ADD                    
        24720   COMPARE_OP                    4 (>)
        24722   POP_JUMP_IF_FALSE             12409 (to 24818)
        24726   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        24730   LOAD_CONST                    0: 0
        24732   COMPARE_OP                    2 (==)
        24734   POP_JUMP_IF_FALSE             12409 (to 24818)
        24738   LOAD_GLOBAL                   76: read
        24740   LOAD_GLOBAL                   90: Send_Telegram
        24742   COMPARE_OP                    0 (<)
        24744   POP_JUMP_IF_FALSE             12409 (to 24818)
        24748   LOAD_GLOBAL                   74: cfg
        24750   LOAD_GLOBAL                   162: Trade_Nifty
        24752   COMPARE_OP                    0 (<)
        24754   POP_JUMP_IF_FALSE             12409 (to 24818)
        24758   LOAD_CONST                    29: 1
        24760   STORE_GLOBAL                  296: K_Direction
        24764   LOAD_CONST                    405: ' King Candle Breakout LTP = '
        24768   LOAD_NAME                     44: int
        24770   LOAD_NAME                     91: float
        24772   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24774   LOAD_CONST                    292: -1
        24778   BINARY_SUBSCR                 
        24780   CALL_FUNCTION                 1
        24782   CALL_FUNCTION                 1
        24784   FORMAT_VALUE                  0
        24786   LOAD_CONST                    406: ', higher than King Candle= '
        24790   LOAD_GLOBAL                   268: partial_profit_booking_enable
        24794   FORMAT_VALUE                  0
        24796   LOAD_CONST                    407: ' '
        24800   BUILD_STRING                  5
        24802   STORE_NAME                    65: strMsg
        24804   LOAD_NAME                     59: iLog
        24806   LOAD_NAME                     65: strMsg
        24808   LOAD_CONST                    52: 2
        24810   LOAD_CONST                    20: True
        24812   LOAD_CONST                    43: ('sendTeleMsg',)
        24814   CALL_FUNCTION_KW              3
        24816   POP_TOP                       
        24818   LOAD_GLOBAL                   174: StraddleEntryTime
        24820   LOAD_CONST                    20: True
        24822   COMPARE_OP                    2 (==)
        24824   POP_JUMP_IF_FALSE             12504 (to 25008)
        24828   LOAD_NAME                     44: int
        24830   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24832   LOAD_CONST                    292: -1
        24836   BINARY_SUBSCR                 
        24838   CALL_FUNCTION                 1
        24840   LOAD_GLOBAL                   285: NULL + max_entry_time
        24844   COMPARE_OP                    0 (<)
        24846   POP_JUMP_IF_FALSE             12504 (to 25008)
        24850   LOAD_GLOBAL                   126: getAccessToken
        24852   LOAD_CONST                    29: 1
        24854   COMPARE_OP                    2 (==)
        24856   POP_JUMP_IF_FALSE             12439 (to 24878)
        24860   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        24864   LOAD_GLOBAL                   294: hedge_buy_price
        24868   LOAD_GLOBAL                   84: strBotToken
        24870   BINARY_SUBTRACT               
        24872   COMPARE_OP                    0 (<)
        24874   POP_JUMP_IF_TRUE              12457 (to 24914)
        24878   LOAD_GLOBAL                   126: getAccessToken
        24880   LOAD_CONST                    29: 1
        24882   COMPARE_OP                    3 (!=)
        24884   POP_JUMP_IF_FALSE             12504 (to 25008)
        24888   LOAD_NAME                     44: int
        24890   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24892   LOAD_CONST                    292: -1
        24896   BINARY_SUBSCR                 
        24898   CALL_FUNCTION                 1
        24900   LOAD_GLOBAL                   294: hedge_buy_price
        24904   LOAD_GLOBAL                   84: strBotToken
        24906   BINARY_SUBTRACT               
        24908   COMPARE_OP                    0 (<)
        24910   POP_JUMP_IF_FALSE             12504 (to 25008)
        24914   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        24918   LOAD_CONST                    0: 0
        24920   COMPARE_OP                    2 (==)
        24922   POP_JUMP_IF_FALSE             12504 (to 25008)
        24926   LOAD_GLOBAL                   76: read
        24928   LOAD_GLOBAL                   90: Send_Telegram
        24930   COMPARE_OP                    0 (<)
        24932   POP_JUMP_IF_FALSE             12504 (to 25008)
        24936   LOAD_GLOBAL                   74: cfg
        24938   LOAD_GLOBAL                   162: Trade_Nifty
        24940   COMPARE_OP                    0 (<)
        24942   POP_JUMP_IF_FALSE             12504 (to 25008)
        24946   LOAD_CONST                    292: -1
        24950   STORE_GLOBAL                  296: K_Direction
        24954   LOAD_CONST                    408: ' Queen Candle Breakout LTP ='
        24958   LOAD_NAME                     44: int
        24960   LOAD_NAME                     91: float
        24962   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        24964   LOAD_CONST                    292: -1
        24968   BINARY_SUBSCR                 
        24970   CALL_FUNCTION                 1
        24972   CALL_FUNCTION                 1
        24974   FORMAT_VALUE                  0
        24976   LOAD_CONST                    409: ', lower than Queen Candle= '
        24980   LOAD_GLOBAL                   285: NULL + max_entry_time
        24984   FORMAT_VALUE                  0
        24986   LOAD_CONST                    407: ' '
        24990   BUILD_STRING                  5
        24992   STORE_NAME                    65: strMsg
        24994   LOAD_NAME                     59: iLog
        24996   LOAD_NAME                     65: strMsg
        24998   LOAD_CONST                    52: 2
        25000   LOAD_CONST                    20: True
        25002   LOAD_CONST                    43: ('sendTeleMsg',)
        25004   CALL_FUNCTION_KW              3
        25006   POP_TOP                       
        25008   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        25012   LOAD_CONST                    29: 1
        25014   COMPARE_OP                    2 (==)
        25016   POP_JUMP_IF_FALSE             13381 (to 26762)
        25020   LOAD_GLOBAL                   171: NULL + King_Candle_Max_SL
        25022   LOAD_CONST                    30: False
        25024   COMPARE_OP                    2 (==)
        25026   POP_JUMP_IF_FALSE             13381 (to 26762)
        25030   LOAD_GLOBAL                   78: get
        25032   LOAD_CONST                    29: 1
        25034   COMPARE_OP                    2 (==)
        25036   POP_JUMP_IF_FALSE             12782 (to 25564)
        25040   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        25042   LOAD_CONST                    341: 'NQ'
        25046   BINARY_SUBSCR                 
        25048   LOAD_METHOD                   390: sum
        25052   CALL_METHOD                   0
        25054   LOAD_CONST                    0: 0
        25056   COMPARE_OP                    3 (!=)
        25058   POP_JUMP_IF_FALSE             12616 (to 25232)
        25062   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        25066   STORE_GLOBAL                  222: Last_Traded_CE_Price
        25068   LOAD_CONST                    410: '  Place CE Buy order for '
        25072   LOAD_GLOBAL                   381: NULL + df_king_cnt
        25076   FORMAT_VALUE                  0
        25078   LOAD_CONST                    349: ' CE at '
        25082   LOAD_GLOBAL                   222: entry_price
        25084   FORMAT_VALUE                  0
        25086   BUILD_STRING                  4
        25088   STORE_NAME                    65: strMsg
        25090   LOAD_NAME                     59: iLog
        25092   LOAD_NAME                     65: strMsg
        25094   LOAD_CONST                    288: 5
        25098   LOAD_CONST                    20: True
        25100   LOAD_CONST                    43: ('sendTeleMsg',)
        25102   CALL_FUNCTION_KW              3
        25104   POP_TOP                       
        25106   LOAD_GLOBAL                   74: cfg
        25108   LOAD_CONST                    29: 1
        25110   BINARY_ADD                    
        25112   STORE_GLOBAL                  74: order_count
        25114   LOAD_GLOBAL                   76: read
        25116   LOAD_NAME                     376: Symbol
        25120   LOAD_GLOBAL                   381: NULL + df_king_cnt
        25124   LOAD_CONST                    315: 'CE'
        25128   LOAD_CONST                    29: 1
        25130   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25134   LOAD_GLOBAL                   222: entry_price
        25136   LOAD_CONST                    292: -1
        25140   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25144   BINARY_MULTIPLY               
        25146   LOAD_GLOBAL                   222: entry_price
        25148   BINARY_MULTIPLY               
        25150   BUILD_LIST                    8
        25152   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        25154   LOAD_ATTR                     379: loc
        25158   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        25160   LOAD_NAME                     191: df_cols
        25162   BUILD_TUPLE                   2
        25164   STORE_SUBSCR                  
        25166   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        25168   LOAD_CONST                    29: 1
        25170   BINARY_ADD                    
        25172   STORE_GLOBAL                  190: df_king_cnt
        25174   LOAD_GLOBAL                   76: read
        25176   LOAD_GLOBAL                   360: PE_TGT_Triggered
        25180   LOAD_CONST                    0: 0
        25182   BINARY_SUBSCR                 
        25184   LOAD_GLOBAL                   360: PE_TGT_Triggered
        25188   LOAD_CONST                    29: 1
        25190   BINARY_SUBSCR                 
        25192   LOAD_CONST                    0: 0
        25194   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25198   BINARY_MULTIPLY               
        25200   BUILD_LIST                    4
        25202   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        25204   LOAD_ATTR                     379: loc
        25208   LOAD_CONST                    0: 0
        25210   LOAD_NAME                     197: leg_cols
        25212   BUILD_TUPLE                   2
        25214   STORE_SUBSCR                  
        25216   LOAD_NAME                     24: pd
        25218   LOAD_METHOD                   380: concat
        25222   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        25224   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        25226   BUILD_LIST                    2
        25228   CALL_METHOD                   1
        25230   STORE_GLOBAL                  200: Current_legs
        25232   LOAD_GLOBAL                   247: NULL + ADX_Period
        25234   LOAD_CONST                    29: 1
        25236   COMPARE_OP                    2 (==)
        25238   POP_JUMP_IF_FALSE             12782 (to 25564)
        25242   LOAD_GLOBAL                   381: NULL + df_king_cnt
        25246   LOAD_GLOBAL                   382: df_cols
        25250   COMPARE_OP                    0 (<)
        25252   POP_JUMP_IF_FALSE             12697 (to 25394)
        25256   SETUP_FINALLY                 8 (to 25274)
        25258   LOAD_NAME                     331: get_option_tokens
        25262   LOAD_CONST                    315: 'CE'
        25266   CALL_FUNCTION                 1
        25268   POP_TOP                       
        25270   POP_BLOCK                     
        25272   JUMP_FORWARD                  60 (to 25394)
        25274   POP_TOP                       
        25276   POP_TOP                       
        25278   POP_TOP                       
        25280   LOAD_NAME                     2: time
        25282   LOAD_METHOD                   355: sleep
        25286   LOAD_CONST                    288: 5
        25290   CALL_METHOD                   1
        25292   POP_TOP                       
        25294   SETUP_FINALLY                 8 (to 25312)
        25296   LOAD_NAME                     331: get_option_tokens
        25300   LOAD_CONST                    315: 'CE'
        25304   CALL_FUNCTION                 1
        25306   POP_TOP                       
        25308   POP_BLOCK                     
        25310   JUMP_FORWARD                  40 (to 25392)
        25312   DUP_TOP                       
        25314   LOAD_NAME                     357: Exception
        25318   JUMP_IF_NOT_EXC_MATCH         12695 (to 25390)
        25322   POP_TOP                       
        25324   STORE_NAME                    358: ex
        25328   POP_TOP                       
        25330   SETUP_FINALLY                 23 (to 25378)
        25332   LOAD_NAME                     59: iLog
        25334   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        25338   LOAD_NAME                     343: str
        25342   LOAD_NAME                     358: ex
        25346   CALL_FUNCTION                 1
        25348   BINARY_ADD                    
        25350   LOAD_CONST                    271: 3
        25354   LOAD_CONST                    20: True
        25356   LOAD_CONST                    43: ('sendTeleMsg',)
        25358   CALL_FUNCTION_KW              3
        25360   POP_TOP                       
        25362   POP_BLOCK                     
        25364   POP_EXCEPT                    
        25366   LOAD_CONST                    1: None
        25368   STORE_NAME                    358: ex
        25372   DELETE_NAME                   358: ex
        25376   JUMP_FORWARD                  7 (to 25392)
        25378   LOAD_CONST                    1: None
        25380   STORE_NAME                    358: ex
        25384   DELETE_NAME                   358: ex
        25388   RERAISE                       1
        25390   RERAISE                       0
        25392   POP_EXCEPT                    
        25394   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        25398   STORE_GLOBAL                  222: Last_Traded_CE_Price
        25400   LOAD_CONST                    411: '  Place CE Buy order for addtional '
        25404   LOAD_GLOBAL                   381: NULL + df_king_cnt
        25408   FORMAT_VALUE                  0
        25410   LOAD_CONST                    349: ' CE at '
        25414   LOAD_GLOBAL                   222: entry_price
        25416   FORMAT_VALUE                  0
        25418   BUILD_STRING                  4
        25420   STORE_NAME                    65: strMsg
        25422   LOAD_NAME                     59: iLog
        25424   LOAD_NAME                     65: strMsg
        25426   LOAD_CONST                    288: 5
        25430   LOAD_CONST                    20: True
        25432   LOAD_CONST                    43: ('sendTeleMsg',)
        25434   CALL_FUNCTION_KW              3
        25436   POP_TOP                       
        25438   LOAD_GLOBAL                   74: cfg
        25440   LOAD_CONST                    29: 1
        25442   BINARY_ADD                    
        25444   STORE_GLOBAL                  74: order_count
        25446   LOAD_GLOBAL                   76: read
        25448   LOAD_NAME                     376: Symbol
        25452   LOAD_GLOBAL                   381: NULL + df_king_cnt
        25456   LOAD_CONST                    315: 'CE'
        25460   LOAD_CONST                    29: 1
        25462   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25466   LOAD_GLOBAL                   222: entry_price
        25468   LOAD_CONST                    292: -1
        25472   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25476   BINARY_MULTIPLY               
        25478   LOAD_GLOBAL                   222: entry_price
        25480   BINARY_MULTIPLY               
        25482   BUILD_LIST                    8
        25484   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        25486   LOAD_ATTR                     379: loc
        25490   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        25492   LOAD_NAME                     191: df_cols
        25494   BUILD_TUPLE                   2
        25496   STORE_SUBSCR                  
        25498   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        25500   LOAD_CONST                    29: 1
        25502   BINARY_ADD                    
        25504   STORE_GLOBAL                  190: df_king_cnt
        25506   LOAD_GLOBAL                   76: read
        25508   LOAD_GLOBAL                   360: PE_TGT_Triggered
        25512   LOAD_CONST                    0: 0
        25514   BINARY_SUBSCR                 
        25516   LOAD_GLOBAL                   360: PE_TGT_Triggered
        25520   LOAD_CONST                    29: 1
        25522   BINARY_SUBSCR                 
        25524   LOAD_CONST                    29: 1
        25526   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25530   BINARY_MULTIPLY               
        25532   BUILD_LIST                    4
        25534   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        25536   LOAD_ATTR                     379: loc
        25540   LOAD_CONST                    0: 0
        25542   LOAD_NAME                     197: leg_cols
        25544   BUILD_TUPLE                   2
        25546   STORE_SUBSCR                  
        25548   LOAD_NAME                     24: pd
        25550   LOAD_METHOD                   380: concat
        25554   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        25556   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        25558   BUILD_LIST                    2
        25560   CALL_METHOD                   1
        25562   STORE_GLOBAL                  200: Current_legs
        25564   LOAD_GLOBAL                   78: get
        25566   LOAD_CONST                    0: 0
        25568   COMPARE_OP                    2 (==)
        25570   POP_JUMP_IF_FALSE             13373 (to 26746)
        25574   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        25576   LOAD_CONST                    341: 'NQ'
        25580   BINARY_SUBSCR                 
        25582   LOAD_METHOD                   390: sum
        25586   CALL_METHOD                   0
        25588   LOAD_CONST                    0: 0
        25590   COMPARE_OP                    3 (!=)
        25592   POP_JUMP_IF_FALSE             13045 (to 26090)
        25596   LOAD_NAME                     308: place_order
        25600   LOAD_CONST                    318: 'B'
        25604   LOAD_GLOBAL                   360: PE_TGT_Triggered
        25608   LOAD_CONST                    52: 2
        25610   BINARY_SUBSCR                 
        25612   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25616   CALL_FUNCTION                 3
        25618   STORE_GLOBAL                  383: order_id_CE
        25622   LOAD_GLOBAL                   74: cfg
        25624   LOAD_CONST                    29: 1
        25626   BINARY_ADD                    
        25628   STORE_GLOBAL                  74: order_count
        25630   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        25634   STORE_GLOBAL                  222: Last_Traded_CE_Price
        25636   LOAD_GLOBAL                   383: NULL + df_cols
        25640   LOAD_CONST                    319: 'norenordno'
        25644   BINARY_SUBSCR                 
        25646   STORE_NAME                    384: order_id
        25650   LOAD_NAME                     311: get_order_symbol
        25654   LOAD_NAME                     384: order_id
        25658   CALL_FUNCTION                 1
        25660   STORE_NAME                    376: Symbol
        25664   LOAD_GLOBAL                   383: NULL + df_cols
        25668   LOAD_CONST                    320: 'stat'
        25672   BINARY_SUBSCR                 
        25674   STORE_NAME                    385: Placed_Status
        25678   LOAD_NAME                     309: get_order_status
        25682   LOAD_NAME                     384: order_id
        25686   CALL_FUNCTION                 1
        25688   STORE_NAME                    386: Return_Status
        25692   LOAD_NAME                     310: get_order_price
        25696   LOAD_NAME                     384: order_id
        25700   CALL_FUNCTION                 1
        25702   STORE_NAME                    387: average_price
        25706   LOAD_NAME                     386: Return_Status
        25710   LOAD_METHOD                   352: upper
        25714   CALL_METHOD                   0
        25716   LOAD_CONST                    321: 'REJECTED'
        25720   COMPARE_OP                    2 (==)
        25722   POP_JUMP_IF_FALSE             12909 (to 25818)
        25726   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        25730   LOAD_NAME                     384: order_id
        25734   FORMAT_VALUE                  0
        25736   LOAD_CONST                    323: ', Ord_STS = '
        25740   LOAD_NAME                     385: Placed_Status
        25744   FORMAT_VALUE                  0
        25746   LOAD_CONST                    324: ', Ret_STS = '
        25750   LOAD_NAME                     386: Return_Status
        25754   FORMAT_VALUE                  0
        25756   LOAD_CONST                    333: '.'
        25760   BUILD_STRING                  7
        25762   STORE_NAME                    65: strMsg
        25764   LOAD_NAME                     59: iLog
        25766   LOAD_NAME                     65: strMsg
        25768   LOAD_CONST                    288: 5
        25772   LOAD_CONST                    20: True
        25774   LOAD_CONST                    43: ('sendTeleMsg',)
        25776   CALL_FUNCTION_KW              3
        25778   POP_TOP                       
        25780   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        25784   STORE_NAME                    65: strMsg
        25786   LOAD_NAME                     59: iLog
        25788   LOAD_NAME                     65: strMsg
        25790   LOAD_CONST                    42: 4
        25792   LOAD_CONST                    20: True
        25794   LOAD_CONST                    43: ('sendTeleMsg',)
        25796   CALL_FUNCTION_KW              3
        25798   POP_TOP                       
        25800   LOAD_NAME                     322: close_all_orders
        25804   CALL_FUNCTION                 0
        25806   POP_TOP                       
        25808   LOAD_NAME                     0: sys
        25810   LOAD_METHOD                   344: exit
        25814   CALL_METHOD                   0
        25816   POP_TOP                       
        25818   LOAD_NAME                     387: average_price
        25822   LOAD_CONST                    0: 0
        25824   COMPARE_OP                    4 (>)
        25826   POP_JUMP_IF_FALSE             12928 (to 25856)
        25830   LOAD_NAME                     386: Return_Status
        25834   LOAD_METHOD                   352: upper
        25838   CALL_METHOD                   0
        25840   LOAD_CONST                    327: 'COMPLETE'
        25844   COMPARE_OP                    2 (==)
        25846   POP_JUMP_IF_FALSE             12928 (to 25856)
        25850   LOAD_NAME                     387: average_price
        25854   STORE_GLOBAL                  222: Last_Traded_CE_Price
        25856   LOAD_GLOBAL                   76: read
        25858   LOAD_NAME                     376: Symbol
        25862   LOAD_GLOBAL                   381: NULL + df_king_cnt
        25866   LOAD_CONST                    315: 'CE'
        25870   LOAD_CONST                    29: 1
        25872   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25876   LOAD_GLOBAL                   222: entry_price
        25878   LOAD_CONST                    292: -1
        25882   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25886   BINARY_MULTIPLY               
        25888   LOAD_GLOBAL                   222: entry_price
        25890   BINARY_MULTIPLY               
        25892   BUILD_LIST                    8
        25894   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        25896   LOAD_ATTR                     379: loc
        25900   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        25902   LOAD_NAME                     191: df_cols
        25904   BUILD_TUPLE                   2
        25906   STORE_SUBSCR                  
        25908   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        25910   LOAD_CONST                    29: 1
        25912   BINARY_ADD                    
        25914   STORE_GLOBAL                  190: df_king_cnt
        25916   LOAD_CONST                    352: ' Placed CE Buy Market order for ATM Strike='
        25920   LOAD_GLOBAL                   381: NULL + df_king_cnt
        25924   FORMAT_VALUE                  0
        25926   LOAD_CONST                    353: ', ATM CE='
        25930   LOAD_NAME                     387: average_price
        25934   FORMAT_VALUE                  0
        25936   LOAD_CONST                    330: ', Qty ='
        25940   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        25944   FORMAT_VALUE                  0
        25946   LOAD_CONST                    331: ', Ord_ID = '
        25950   LOAD_NAME                     384: order_id
        25954   FORMAT_VALUE                  0
        25956   LOAD_CONST                    323: ', Ord_STS = '
        25960   LOAD_NAME                     385: Placed_Status
        25964   FORMAT_VALUE                  0
        25966   LOAD_CONST                    324: ', Ret_STS = '
        25970   LOAD_NAME                     386: Return_Status
        25974   FORMAT_VALUE                  0
        25976   BUILD_STRING                  12
        25978   STORE_NAME                    65: strMsg
        25980   LOAD_NAME                     59: iLog
        25982   LOAD_NAME                     65: strMsg
        25984   LOAD_CONST                    288: 5
        25988   LOAD_CONST                    20: True
        25990   LOAD_CONST                    43: ('sendTeleMsg',)
        25992   CALL_FUNCTION_KW              3
        25994   POP_TOP                       
        25996   LOAD_NAME                     72: tl
        25998   LOAD_METHOD                   388: update_csv
        26002   LOAD_NAME                     376: Symbol
        26006   LOAD_CONST                    332: 'Buy'
        26010   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26014   LOAD_GLOBAL                   222: entry_price
        26016   LOAD_NAME                     384: order_id
        26020   LOAD_NAME                     385: Placed_Status
        26024   LOAD_NAME                     386: Return_Status
        26028   CALL_METHOD                   7
        26030   POP_TOP                       
        26032   LOAD_GLOBAL                   76: read
        26034   LOAD_GLOBAL                   360: PE_TGT_Triggered
        26038   LOAD_CONST                    0: 0
        26040   BINARY_SUBSCR                 
        26042   LOAD_GLOBAL                   360: PE_TGT_Triggered
        26046   LOAD_CONST                    29: 1
        26048   BINARY_SUBSCR                 
        26050   LOAD_CONST                    0: 0
        26052   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26056   BINARY_MULTIPLY               
        26058   BUILD_LIST                    4
        26060   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        26062   LOAD_ATTR                     379: loc
        26066   LOAD_CONST                    0: 0
        26068   LOAD_NAME                     197: leg_cols
        26070   BUILD_TUPLE                   2
        26072   STORE_SUBSCR                  
        26074   LOAD_NAME                     24: pd
        26076   LOAD_METHOD                   380: concat
        26080   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        26082   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        26084   BUILD_LIST                    2
        26086   CALL_METHOD                   1
        26088   STORE_GLOBAL                  200: Current_legs
        26090   LOAD_GLOBAL                   247: NULL + ADX_Period
        26092   LOAD_CONST                    29: 1
        26094   COMPARE_OP                    2 (==)
        26096   POP_JUMP_IF_FALSE             13373 (to 26746)
        26100   LOAD_GLOBAL                   381: NULL + df_king_cnt
        26104   LOAD_GLOBAL                   382: df_cols
        26108   COMPARE_OP                    0 (<)
        26110   POP_JUMP_IF_FALSE             13126 (to 26252)
        26114   SETUP_FINALLY                 8 (to 26132)
        26116   LOAD_NAME                     331: get_option_tokens
        26120   LOAD_CONST                    315: 'CE'
        26124   CALL_FUNCTION                 1
        26126   POP_TOP                       
        26128   POP_BLOCK                     
        26130   JUMP_FORWARD                  60 (to 26252)
        26132   POP_TOP                       
        26134   POP_TOP                       
        26136   POP_TOP                       
        26138   LOAD_NAME                     2: time
        26140   LOAD_METHOD                   355: sleep
        26144   LOAD_CONST                    288: 5
        26148   CALL_METHOD                   1
        26150   POP_TOP                       
        26152   SETUP_FINALLY                 8 (to 26170)
        26154   LOAD_NAME                     331: get_option_tokens
        26158   LOAD_CONST                    315: 'CE'
        26162   CALL_FUNCTION                 1
        26164   POP_TOP                       
        26166   POP_BLOCK                     
        26168   JUMP_FORWARD                  40 (to 26250)
        26170   DUP_TOP                       
        26172   LOAD_NAME                     357: Exception
        26176   JUMP_IF_NOT_EXC_MATCH         13124 (to 26248)
        26180   POP_TOP                       
        26182   STORE_NAME                    358: ex
        26186   POP_TOP                       
        26188   SETUP_FINALLY                 23 (to 26236)
        26190   LOAD_NAME                     59: iLog
        26192   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        26196   LOAD_NAME                     343: str
        26200   LOAD_NAME                     358: ex
        26204   CALL_FUNCTION                 1
        26206   BINARY_ADD                    
        26208   LOAD_CONST                    271: 3
        26212   LOAD_CONST                    20: True
        26214   LOAD_CONST                    43: ('sendTeleMsg',)
        26216   CALL_FUNCTION_KW              3
        26218   POP_TOP                       
        26220   POP_BLOCK                     
        26222   POP_EXCEPT                    
        26224   LOAD_CONST                    1: None
        26226   STORE_NAME                    358: ex
        26230   DELETE_NAME                   358: ex
        26234   JUMP_FORWARD                  7 (to 26250)
        26236   LOAD_CONST                    1: None
        26238   STORE_NAME                    358: ex
        26242   DELETE_NAME                   358: ex
        26246   RERAISE                       1
        26248   RERAISE                       0
        26250   POP_EXCEPT                    
        26252   LOAD_NAME                     308: place_order
        26256   LOAD_CONST                    318: 'B'
        26260   LOAD_GLOBAL                   360: PE_TGT_Triggered
        26264   LOAD_CONST                    52: 2
        26266   BINARY_SUBSCR                 
        26268   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26272   CALL_FUNCTION                 3
        26274   STORE_NAME                    394: order_id_CE1
        26278   LOAD_GLOBAL                   74: cfg
        26280   LOAD_CONST                    29: 1
        26282   BINARY_ADD                    
        26284   STORE_GLOBAL                  74: order_count
        26286   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        26290   STORE_GLOBAL                  222: Last_Traded_CE_Price
        26292   LOAD_NAME                     394: order_id_CE1
        26296   LOAD_CONST                    319: 'norenordno'
        26300   BINARY_SUBSCR                 
        26302   STORE_NAME                    384: order_id
        26306   LOAD_NAME                     311: get_order_symbol
        26310   LOAD_NAME                     384: order_id
        26314   CALL_FUNCTION                 1
        26316   STORE_NAME                    376: Symbol
        26320   LOAD_NAME                     394: order_id_CE1
        26324   LOAD_CONST                    320: 'stat'
        26328   BINARY_SUBSCR                 
        26330   STORE_NAME                    385: Placed_Status
        26334   LOAD_NAME                     309: get_order_status
        26338   LOAD_NAME                     384: order_id
        26342   CALL_FUNCTION                 1
        26344   STORE_NAME                    386: Return_Status
        26348   LOAD_NAME                     310: get_order_price
        26352   LOAD_NAME                     384: order_id
        26356   CALL_FUNCTION                 1
        26358   STORE_NAME                    387: average_price
        26362   LOAD_NAME                     386: Return_Status
        26366   LOAD_METHOD                   352: upper
        26370   CALL_METHOD                   0
        26372   LOAD_CONST                    321: 'REJECTED'
        26376   COMPARE_OP                    2 (==)
        26378   POP_JUMP_IF_FALSE             13237 (to 26474)
        26382   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        26386   LOAD_NAME                     384: order_id
        26390   FORMAT_VALUE                  0
        26392   LOAD_CONST                    323: ', Ord_STS = '
        26396   LOAD_NAME                     385: Placed_Status
        26400   FORMAT_VALUE                  0
        26402   LOAD_CONST                    324: ', Ret_STS = '
        26406   LOAD_NAME                     386: Return_Status
        26410   FORMAT_VALUE                  0
        26412   LOAD_CONST                    333: '.'
        26416   BUILD_STRING                  7
        26418   STORE_NAME                    65: strMsg
        26420   LOAD_NAME                     59: iLog
        26422   LOAD_NAME                     65: strMsg
        26424   LOAD_CONST                    288: 5
        26428   LOAD_CONST                    20: True
        26430   LOAD_CONST                    43: ('sendTeleMsg',)
        26432   CALL_FUNCTION_KW              3
        26434   POP_TOP                       
        26436   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        26440   STORE_NAME                    65: strMsg
        26442   LOAD_NAME                     59: iLog
        26444   LOAD_NAME                     65: strMsg
        26446   LOAD_CONST                    42: 4
        26448   LOAD_CONST                    20: True
        26450   LOAD_CONST                    43: ('sendTeleMsg',)
        26452   CALL_FUNCTION_KW              3
        26454   POP_TOP                       
        26456   LOAD_NAME                     322: close_all_orders
        26460   CALL_FUNCTION                 0
        26462   POP_TOP                       
        26464   LOAD_NAME                     0: sys
        26466   LOAD_METHOD                   344: exit
        26470   CALL_METHOD                   0
        26472   POP_TOP                       
        26474   LOAD_NAME                     387: average_price
        26478   LOAD_CONST                    0: 0
        26480   COMPARE_OP                    4 (>)
        26482   POP_JUMP_IF_FALSE             13256 (to 26512)
        26486   LOAD_NAME                     386: Return_Status
        26490   LOAD_METHOD                   352: upper
        26494   CALL_METHOD                   0
        26496   LOAD_CONST                    327: 'COMPLETE'
        26500   COMPARE_OP                    2 (==)
        26502   POP_JUMP_IF_FALSE             13256 (to 26512)
        26506   LOAD_NAME                     387: average_price
        26510   STORE_GLOBAL                  222: Last_Traded_CE_Price
        26512   LOAD_GLOBAL                   76: read
        26514   LOAD_NAME                     376: Symbol
        26518   LOAD_GLOBAL                   381: NULL + df_king_cnt
        26522   LOAD_CONST                    315: 'CE'
        26526   LOAD_CONST                    29: 1
        26528   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26532   LOAD_GLOBAL                   222: entry_price
        26534   LOAD_CONST                    292: -1
        26538   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26542   BINARY_MULTIPLY               
        26544   LOAD_GLOBAL                   222: entry_price
        26546   BINARY_MULTIPLY               
        26548   BUILD_LIST                    8
        26550   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        26552   LOAD_ATTR                     379: loc
        26556   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        26558   LOAD_NAME                     191: df_cols
        26560   BUILD_TUPLE                   2
        26562   STORE_SUBSCR                  
        26564   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        26566   LOAD_CONST                    29: 1
        26568   BINARY_ADD                    
        26570   STORE_GLOBAL                  190: df_king_cnt
        26572   LOAD_CONST                    352: ' Placed CE Buy Market order for ATM Strike='
        26576   LOAD_GLOBAL                   381: NULL + df_king_cnt
        26580   FORMAT_VALUE                  0
        26582   LOAD_CONST                    353: ', ATM CE='
        26586   LOAD_NAME                     387: average_price
        26590   FORMAT_VALUE                  0
        26592   LOAD_CONST                    330: ', Qty ='
        26596   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26600   FORMAT_VALUE                  0
        26602   LOAD_CONST                    331: ', Ord_ID = '
        26606   LOAD_NAME                     384: order_id
        26610   FORMAT_VALUE                  0
        26612   LOAD_CONST                    323: ', Ord_STS = '
        26616   LOAD_NAME                     385: Placed_Status
        26620   FORMAT_VALUE                  0
        26622   LOAD_CONST                    324: ', Ret_STS = '
        26626   LOAD_NAME                     386: Return_Status
        26630   FORMAT_VALUE                  0
        26632   BUILD_STRING                  12
        26634   STORE_NAME                    65: strMsg
        26636   LOAD_NAME                     59: iLog
        26638   LOAD_NAME                     65: strMsg
        26640   LOAD_CONST                    288: 5
        26644   LOAD_CONST                    20: True
        26646   LOAD_CONST                    43: ('sendTeleMsg',)
        26648   CALL_FUNCTION_KW              3
        26650   POP_TOP                       
        26652   LOAD_NAME                     72: tl
        26654   LOAD_METHOD                   388: update_csv
        26658   LOAD_NAME                     376: Symbol
        26662   LOAD_CONST                    332: 'Buy'
        26666   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26670   LOAD_GLOBAL                   222: entry_price
        26672   LOAD_NAME                     384: order_id
        26676   LOAD_NAME                     385: Placed_Status
        26680   LOAD_NAME                     386: Return_Status
        26684   CALL_METHOD                   7
        26686   POP_TOP                       
        26688   LOAD_GLOBAL                   76: read
        26690   LOAD_GLOBAL                   360: PE_TGT_Triggered
        26694   LOAD_CONST                    0: 0
        26696   BINARY_SUBSCR                 
        26698   LOAD_GLOBAL                   360: PE_TGT_Triggered
        26702   LOAD_CONST                    29: 1
        26704   BINARY_SUBSCR                 
        26706   LOAD_CONST                    29: 1
        26708   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26712   BINARY_MULTIPLY               
        26714   BUILD_LIST                    4
        26716   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        26718   LOAD_ATTR                     379: loc
        26722   LOAD_CONST                    0: 0
        26724   LOAD_NAME                     197: leg_cols
        26726   BUILD_TUPLE                   2
        26728   STORE_SUBSCR                  
        26730   LOAD_NAME                     24: pd
        26732   LOAD_METHOD                   380: concat
        26736   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        26738   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        26740   BUILD_LIST                    2
        26742   CALL_METHOD                   1
        26744   STORE_GLOBAL                  200: Current_legs
        26746   LOAD_CONST                    20: True
        26748   STORE_GLOBAL                  171: King_Order_Placed
        26750   LOAD_NAME                     297: K_Direction_Change_Count
        26754   LOAD_CONST                    29: 1
        26756   BINARY_ADD                    
        26758   STORE_NAME                    297: K_Direction_Change_Count
        26762   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        26766   LOAD_CONST                    292: -1
        26770   COMPARE_OP                    2 (==)
        26772   POP_JUMP_IF_FALSE             14263 (to 28526)
        26776   LOAD_GLOBAL                   172: time_offset_sec
        26778   LOAD_CONST                    30: False
        26780   COMPARE_OP                    2 (==)
        26782   POP_JUMP_IF_FALSE             14263 (to 28526)
        26786   LOAD_GLOBAL                   78: get
        26788   LOAD_CONST                    29: 1
        26790   COMPARE_OP                    2 (==)
        26792   POP_JUMP_IF_FALSE             13660 (to 27320)
        26796   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        26798   LOAD_CONST                    341: 'NQ'
        26802   BINARY_SUBSCR                 
        26804   LOAD_METHOD                   390: sum
        26808   CALL_METHOD                   0
        26810   LOAD_CONST                    0: 0
        26812   COMPARE_OP                    3 (!=)
        26814   POP_JUMP_IF_FALSE             13494 (to 26988)
        26818   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        26822   STORE_GLOBAL                  221: Last_Traded_PE_Price
        26824   LOAD_CONST                    412: '  Place PE Buy order for '
        26828   LOAD_GLOBAL                   382: df_cols
        26832   FORMAT_VALUE                  0
        26834   LOAD_CONST                    363: ' PE at '
        26838   LOAD_GLOBAL                   221: NULL + strike_offset
        26840   FORMAT_VALUE                  0
        26842   BUILD_STRING                  4
        26844   STORE_NAME                    65: strMsg
        26846   LOAD_NAME                     59: iLog
        26848   LOAD_NAME                     65: strMsg
        26850   LOAD_CONST                    288: 5
        26854   LOAD_CONST                    20: True
        26856   LOAD_CONST                    43: ('sendTeleMsg',)
        26858   CALL_FUNCTION_KW              3
        26860   POP_TOP                       
        26862   LOAD_GLOBAL                   74: cfg
        26864   LOAD_CONST                    29: 1
        26866   BINARY_ADD                    
        26868   STORE_GLOBAL                  74: order_count
        26870   LOAD_GLOBAL                   76: read
        26872   LOAD_NAME                     376: Symbol
        26876   LOAD_GLOBAL                   382: df_cols
        26880   LOAD_CONST                    316: 'PE'
        26884   LOAD_CONST                    29: 1
        26886   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26890   LOAD_GLOBAL                   221: NULL + strike_offset
        26892   LOAD_CONST                    292: -1
        26896   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26900   BINARY_MULTIPLY               
        26902   LOAD_GLOBAL                   221: NULL + strike_offset
        26904   BINARY_MULTIPLY               
        26906   BUILD_LIST                    8
        26908   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        26910   LOAD_ATTR                     379: loc
        26914   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        26916   LOAD_NAME                     191: df_cols
        26918   BUILD_TUPLE                   2
        26920   STORE_SUBSCR                  
        26922   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        26924   LOAD_CONST                    29: 1
        26926   BINARY_ADD                    
        26928   STORE_GLOBAL                  190: df_king_cnt
        26930   LOAD_GLOBAL                   76: read
        26932   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        26936   LOAD_CONST                    0: 0
        26938   BINARY_SUBSCR                 
        26940   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        26944   LOAD_CONST                    29: 1
        26946   BINARY_SUBSCR                 
        26948   LOAD_CONST                    0: 0
        26950   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        26954   BINARY_MULTIPLY               
        26956   BUILD_LIST                    4
        26958   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        26960   LOAD_ATTR                     379: loc
        26964   LOAD_CONST                    0: 0
        26966   LOAD_NAME                     197: leg_cols
        26968   BUILD_TUPLE                   2
        26970   STORE_SUBSCR                  
        26972   LOAD_NAME                     24: pd
        26974   LOAD_METHOD                   380: concat
        26978   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        26980   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        26982   BUILD_LIST                    2
        26984   CALL_METHOD                   1
        26986   STORE_GLOBAL                  200: Current_legs
        26988   LOAD_GLOBAL                   247: NULL + ADX_Period
        26990   LOAD_CONST                    29: 1
        26992   COMPARE_OP                    2 (==)
        26994   POP_JUMP_IF_FALSE             13660 (to 27320)
        26998   LOAD_GLOBAL                   382: df_cols
        27002   LOAD_GLOBAL                   381: NULL + df_king_cnt
        27006   COMPARE_OP                    4 (>)
        27008   POP_JUMP_IF_FALSE             13575 (to 27150)
        27012   SETUP_FINALLY                 8 (to 27030)
        27014   LOAD_NAME                     331: get_option_tokens
        27018   LOAD_CONST                    316: 'PE'
        27022   CALL_FUNCTION                 1
        27024   POP_TOP                       
        27026   POP_BLOCK                     
        27028   JUMP_FORWARD                  60 (to 27150)
        27030   POP_TOP                       
        27032   POP_TOP                       
        27034   POP_TOP                       
        27036   LOAD_NAME                     2: time
        27038   LOAD_METHOD                   355: sleep
        27042   LOAD_CONST                    288: 5
        27046   CALL_METHOD                   1
        27048   POP_TOP                       
        27050   SETUP_FINALLY                 8 (to 27068)
        27052   LOAD_NAME                     331: get_option_tokens
        27056   LOAD_CONST                    316: 'PE'
        27060   CALL_FUNCTION                 1
        27062   POP_TOP                       
        27064   POP_BLOCK                     
        27066   JUMP_FORWARD                  40 (to 27148)
        27068   DUP_TOP                       
        27070   LOAD_NAME                     357: Exception
        27074   JUMP_IF_NOT_EXC_MATCH         13573 (to 27146)
        27078   POP_TOP                       
        27080   STORE_NAME                    358: ex
        27084   POP_TOP                       
        27086   SETUP_FINALLY                 23 (to 27134)
        27088   LOAD_NAME                     59: iLog
        27090   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        27094   LOAD_NAME                     343: str
        27098   LOAD_NAME                     358: ex
        27102   CALL_FUNCTION                 1
        27104   BINARY_ADD                    
        27106   LOAD_CONST                    271: 3
        27110   LOAD_CONST                    20: True
        27112   LOAD_CONST                    43: ('sendTeleMsg',)
        27114   CALL_FUNCTION_KW              3
        27116   POP_TOP                       
        27118   POP_BLOCK                     
        27120   POP_EXCEPT                    
        27122   LOAD_CONST                    1: None
        27124   STORE_NAME                    358: ex
        27128   DELETE_NAME                   358: ex
        27132   JUMP_FORWARD                  7 (to 27148)
        27134   LOAD_CONST                    1: None
        27136   STORE_NAME                    358: ex
        27140   DELETE_NAME                   358: ex
        27144   RERAISE                       1
        27146   RERAISE                       0
        27148   POP_EXCEPT                    
        27150   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        27154   STORE_GLOBAL                  221: Last_Traded_PE_Price
        27156   LOAD_CONST                    413: '  Place PE Buy order for addtional '
        27160   LOAD_GLOBAL                   382: df_cols
        27164   FORMAT_VALUE                  0
        27166   LOAD_CONST                    363: ' PE at '
        27170   LOAD_GLOBAL                   221: NULL + strike_offset
        27172   FORMAT_VALUE                  0
        27174   BUILD_STRING                  4
        27176   STORE_NAME                    65: strMsg
        27178   LOAD_NAME                     59: iLog
        27180   LOAD_NAME                     65: strMsg
        27182   LOAD_CONST                    288: 5
        27186   LOAD_CONST                    20: True
        27188   LOAD_CONST                    43: ('sendTeleMsg',)
        27190   CALL_FUNCTION_KW              3
        27192   POP_TOP                       
        27194   LOAD_GLOBAL                   74: cfg
        27196   LOAD_CONST                    29: 1
        27198   BINARY_ADD                    
        27200   STORE_GLOBAL                  74: order_count
        27202   LOAD_GLOBAL                   76: read
        27204   LOAD_NAME                     376: Symbol
        27208   LOAD_GLOBAL                   382: df_cols
        27212   LOAD_CONST                    316: 'PE'
        27216   LOAD_CONST                    29: 1
        27218   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27222   LOAD_GLOBAL                   221: NULL + strike_offset
        27224   LOAD_CONST                    292: -1
        27228   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27232   BINARY_MULTIPLY               
        27234   LOAD_GLOBAL                   221: NULL + strike_offset
        27236   BINARY_MULTIPLY               
        27238   BUILD_LIST                    8
        27240   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        27242   LOAD_ATTR                     379: loc
        27246   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        27248   LOAD_NAME                     191: df_cols
        27250   BUILD_TUPLE                   2
        27252   STORE_SUBSCR                  
        27254   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        27256   LOAD_CONST                    29: 1
        27258   BINARY_ADD                    
        27260   STORE_GLOBAL                  190: df_king_cnt
        27262   LOAD_GLOBAL                   76: read
        27264   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        27268   LOAD_CONST                    0: 0
        27270   BINARY_SUBSCR                 
        27272   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        27276   LOAD_CONST                    29: 1
        27278   BINARY_SUBSCR                 
        27280   LOAD_CONST                    29: 1
        27282   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27286   BINARY_MULTIPLY               
        27288   BUILD_LIST                    4
        27290   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        27292   LOAD_ATTR                     379: loc
        27296   LOAD_CONST                    0: 0
        27298   LOAD_NAME                     197: leg_cols
        27300   BUILD_TUPLE                   2
        27302   STORE_SUBSCR                  
        27304   LOAD_NAME                     24: pd
        27306   LOAD_METHOD                   380: concat
        27310   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        27312   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        27314   BUILD_LIST                    2
        27316   CALL_METHOD                   1
        27318   STORE_GLOBAL                  200: Current_legs
        27320   LOAD_GLOBAL                   78: get
        27322   LOAD_CONST                    0: 0
        27324   COMPARE_OP                    2 (==)
        27326   POP_JUMP_IF_FALSE             14255 (to 28510)
        27330   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        27332   LOAD_CONST                    341: 'NQ'
        27336   BINARY_SUBSCR                 
        27338   LOAD_METHOD                   390: sum
        27342   CALL_METHOD                   0
        27344   LOAD_CONST                    0: 0
        27346   COMPARE_OP                    3 (!=)
        27348   POP_JUMP_IF_FALSE             13925 (to 27850)
        27352   LOAD_NAME                     308: place_order
        27356   LOAD_CONST                    318: 'B'
        27360   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        27364   LOAD_CONST                    52: 2
        27366   BINARY_SUBSCR                 
        27368   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27372   CALL_FUNCTION                 3
        27374   STORE_GLOBAL                  389: order_id_PE
        27378   LOAD_GLOBAL                   74: cfg
        27380   LOAD_CONST                    29: 1
        27382   BINARY_ADD                    
        27384   STORE_GLOBAL                  74: order_count
        27386   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        27390   STORE_GLOBAL                  221: Last_Traded_PE_Price
        27392   LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        27396   LOAD_CONST                    319: 'norenordno'
        27400   BINARY_SUBSCR                 
        27402   STORE_NAME                    384: order_id
        27406   LOAD_NAME                     311: get_order_symbol
        27410   LOAD_NAME                     384: order_id
        27414   CALL_FUNCTION                 1
        27416   STORE_NAME                    376: Symbol
        27420   LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        27424   LOAD_CONST                    320: 'stat'
        27428   BINARY_SUBSCR                 
        27430   STORE_NAME                    385: Placed_Status
        27434   LOAD_NAME                     309: get_order_status
        27438   LOAD_NAME                     384: order_id
        27442   CALL_FUNCTION                 1
        27444   STORE_NAME                    386: Return_Status
        27448   LOAD_NAME                     310: get_order_price
        27452   LOAD_NAME                     384: order_id
        27456   CALL_FUNCTION                 1
        27458   STORE_NAME                    387: average_price
        27462   LOAD_NAME                     386: Return_Status
        27466   LOAD_METHOD                   352: upper
        27470   CALL_METHOD                   0
        27472   LOAD_CONST                    321: 'REJECTED'
        27476   COMPARE_OP                    2 (==)
        27478   POP_JUMP_IF_FALSE             13787 (to 27574)
        27482   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        27486   LOAD_NAME                     384: order_id
        27490   FORMAT_VALUE                  0
        27492   LOAD_CONST                    323: ', Ord_STS = '
        27496   LOAD_NAME                     385: Placed_Status
        27500   FORMAT_VALUE                  0
        27502   LOAD_CONST                    324: ', Ret_STS = '
        27506   LOAD_NAME                     386: Return_Status
        27510   FORMAT_VALUE                  0
        27512   LOAD_CONST                    333: '.'
        27516   BUILD_STRING                  7
        27518   STORE_NAME                    65: strMsg
        27520   LOAD_NAME                     59: iLog
        27522   LOAD_NAME                     65: strMsg
        27524   LOAD_CONST                    288: 5
        27528   LOAD_CONST                    20: True
        27530   LOAD_CONST                    43: ('sendTeleMsg',)
        27532   CALL_FUNCTION_KW              3
        27534   POP_TOP                       
        27536   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        27540   STORE_NAME                    65: strMsg
        27542   LOAD_NAME                     59: iLog
        27544   LOAD_NAME                     65: strMsg
        27546   LOAD_CONST                    42: 4
        27548   LOAD_CONST                    20: True
        27550   LOAD_CONST                    43: ('sendTeleMsg',)
        27552   CALL_FUNCTION_KW              3
        27554   POP_TOP                       
        27556   LOAD_NAME                     322: close_all_orders
        27560   CALL_FUNCTION                 0
        27562   POP_TOP                       
        27564   LOAD_NAME                     0: sys
        27566   LOAD_METHOD                   344: exit
        27570   CALL_METHOD                   0
        27572   POP_TOP                       
        27574   LOAD_NAME                     387: average_price
        27578   LOAD_CONST                    0: 0
        27580   COMPARE_OP                    4 (>)
        27582   POP_JUMP_IF_FALSE             13806 (to 27612)
        27586   LOAD_NAME                     386: Return_Status
        27590   LOAD_METHOD                   352: upper
        27594   CALL_METHOD                   0
        27596   LOAD_CONST                    327: 'COMPLETE'
        27600   COMPARE_OP                    2 (==)
        27602   POP_JUMP_IF_FALSE             13806 (to 27612)
        27606   LOAD_NAME                     387: average_price
        27610   STORE_GLOBAL                  221: Last_Traded_PE_Price
        27612   LOAD_GLOBAL                   76: read
        27614   LOAD_NAME                     376: Symbol
        27618   LOAD_GLOBAL                   382: df_cols
        27622   LOAD_CONST                    316: 'PE'
        27626   LOAD_CONST                    29: 1
        27628   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27632   LOAD_GLOBAL                   221: NULL + strike_offset
        27634   LOAD_CONST                    292: -1
        27638   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27642   BINARY_MULTIPLY               
        27644   LOAD_GLOBAL                   221: NULL + strike_offset
        27646   BINARY_MULTIPLY               
        27648   BUILD_LIST                    8
        27650   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        27652   LOAD_ATTR                     379: loc
        27656   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        27658   LOAD_NAME                     191: df_cols
        27660   BUILD_TUPLE                   2
        27662   STORE_SUBSCR                  
        27664   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        27666   LOAD_CONST                    29: 1
        27668   BINARY_ADD                    
        27670   STORE_GLOBAL                  190: df_king_cnt
        27672   LOAD_CONST                    20: True
        27674   STORE_GLOBAL                  170: First_Straddle
        27676   LOAD_CONST                    365: ' Placed PE Buy Market order for ATM Strike='
        27680   LOAD_GLOBAL                   382: df_cols
        27684   FORMAT_VALUE                  0
        27686   LOAD_CONST                    366: ', ATM PE='
        27690   LOAD_NAME                     387: average_price
        27694   FORMAT_VALUE                  0
        27696   LOAD_CONST                    330: ', Qty ='
        27700   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27704   FORMAT_VALUE                  0
        27706   LOAD_CONST                    331: ', Ord_ID = '
        27710   LOAD_NAME                     384: order_id
        27714   FORMAT_VALUE                  0
        27716   LOAD_CONST                    323: ', Ord_STS = '
        27720   LOAD_NAME                     385: Placed_Status
        27724   FORMAT_VALUE                  0
        27726   LOAD_CONST                    324: ', Ret_STS = '
        27730   LOAD_NAME                     386: Return_Status
        27734   FORMAT_VALUE                  0
        27736   BUILD_STRING                  12
        27738   STORE_NAME                    65: strMsg
        27740   LOAD_NAME                     59: iLog
        27742   LOAD_NAME                     65: strMsg
        27744   LOAD_CONST                    288: 5
        27748   LOAD_CONST                    20: True
        27750   LOAD_CONST                    43: ('sendTeleMsg',)
        27752   CALL_FUNCTION_KW              3
        27754   POP_TOP                       
        27756   LOAD_NAME                     72: tl
        27758   LOAD_METHOD                   388: update_csv
        27762   LOAD_NAME                     376: Symbol
        27766   LOAD_CONST                    332: 'Buy'
        27770   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27774   LOAD_GLOBAL                   221: NULL + strike_offset
        27776   LOAD_NAME                     384: order_id
        27780   LOAD_NAME                     385: Placed_Status
        27784   LOAD_NAME                     386: Return_Status
        27788   CALL_METHOD                   7
        27790   POP_TOP                       
        27792   LOAD_GLOBAL                   76: read
        27794   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        27798   LOAD_CONST                    0: 0
        27800   BINARY_SUBSCR                 
        27802   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        27806   LOAD_CONST                    29: 1
        27808   BINARY_SUBSCR                 
        27810   LOAD_CONST                    0: 0
        27812   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        27816   BINARY_MULTIPLY               
        27818   BUILD_LIST                    4
        27820   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        27822   LOAD_ATTR                     379: loc
        27826   LOAD_CONST                    0: 0
        27828   LOAD_NAME                     197: leg_cols
        27830   BUILD_TUPLE                   2
        27832   STORE_SUBSCR                  
        27834   LOAD_NAME                     24: pd
        27836   LOAD_METHOD                   380: concat
        27840   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        27842   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        27844   BUILD_LIST                    2
        27846   CALL_METHOD                   1
        27848   STORE_GLOBAL                  200: Current_legs
        27850   LOAD_GLOBAL                   247: NULL + ADX_Period
        27852   LOAD_CONST                    29: 1
        27854   COMPARE_OP                    2 (==)
        27856   POP_JUMP_IF_FALSE             14255 (to 28510)
        27860   LOAD_GLOBAL                   382: df_cols
        27864   LOAD_GLOBAL                   381: NULL + df_king_cnt
        27868   COMPARE_OP                    4 (>)
        27870   POP_JUMP_IF_FALSE             14006 (to 28012)
        27874   SETUP_FINALLY                 8 (to 27892)
        27876   LOAD_NAME                     331: get_option_tokens
        27880   LOAD_CONST                    316: 'PE'
        27884   CALL_FUNCTION                 1
        27886   POP_TOP                       
        27888   POP_BLOCK                     
        27890   JUMP_FORWARD                  60 (to 28012)
        27892   POP_TOP                       
        27894   POP_TOP                       
        27896   POP_TOP                       
        27898   LOAD_NAME                     2: time
        27900   LOAD_METHOD                   355: sleep
        27904   LOAD_CONST                    288: 5
        27908   CALL_METHOD                   1
        27910   POP_TOP                       
        27912   SETUP_FINALLY                 8 (to 27930)
        27914   LOAD_NAME                     331: get_option_tokens
        27918   LOAD_CONST                    316: 'PE'
        27922   CALL_FUNCTION                 1
        27924   POP_TOP                       
        27926   POP_BLOCK                     
        27928   JUMP_FORWARD                  40 (to 28010)
        27930   DUP_TOP                       
        27932   LOAD_NAME                     357: Exception
        27936   JUMP_IF_NOT_EXC_MATCH         14004 (to 28008)
        27940   POP_TOP                       
        27942   STORE_NAME                    358: ex
        27946   POP_TOP                       
        27948   SETUP_FINALLY                 23 (to 27996)
        27950   LOAD_NAME                     59: iLog
        27952   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        27956   LOAD_NAME                     343: str
        27960   LOAD_NAME                     358: ex
        27964   CALL_FUNCTION                 1
        27966   BINARY_ADD                    
        27968   LOAD_CONST                    271: 3
        27972   LOAD_CONST                    20: True
        27974   LOAD_CONST                    43: ('sendTeleMsg',)
        27976   CALL_FUNCTION_KW              3
        27978   POP_TOP                       
        27980   POP_BLOCK                     
        27982   POP_EXCEPT                    
        27984   LOAD_CONST                    1: None
        27986   STORE_NAME                    358: ex
        27990   DELETE_NAME                   358: ex
        27994   JUMP_FORWARD                  7 (to 28010)
        27996   LOAD_CONST                    1: None
        27998   STORE_NAME                    358: ex
        28002   DELETE_NAME                   358: ex
        28006   RERAISE                       1
        28008   RERAISE                       0
        28010   POP_EXCEPT                    
        28012   LOAD_NAME                     308: place_order
        28016   LOAD_CONST                    318: 'B'
        28020   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        28024   LOAD_CONST                    52: 2
        28026   BINARY_SUBSCR                 
        28028   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        28032   CALL_FUNCTION                 3
        28034   STORE_NAME                    395: order_id_PE1
        28038   LOAD_GLOBAL                   74: cfg
        28040   LOAD_CONST                    29: 1
        28042   BINARY_ADD                    
        28044   STORE_GLOBAL                  74: order_count
        28046   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        28050   STORE_GLOBAL                  221: Last_Traded_PE_Price
        28052   LOAD_NAME                     395: order_id_PE1
        28056   LOAD_CONST                    319: 'norenordno'
        28060   BINARY_SUBSCR                 
        28062   STORE_NAME                    384: order_id
        28066   LOAD_NAME                     311: get_order_symbol
        28070   LOAD_NAME                     384: order_id
        28074   CALL_FUNCTION                 1
        28076   STORE_NAME                    376: Symbol
        28080   LOAD_NAME                     395: order_id_PE1
        28084   LOAD_CONST                    320: 'stat'
        28088   BINARY_SUBSCR                 
        28090   STORE_NAME                    385: Placed_Status
        28094   LOAD_NAME                     309: get_order_status
        28098   LOAD_NAME                     384: order_id
        28102   CALL_FUNCTION                 1
        28104   STORE_NAME                    386: Return_Status
        28108   LOAD_NAME                     310: get_order_price
        28112   LOAD_NAME                     384: order_id
        28116   CALL_FUNCTION                 1
        28118   STORE_NAME                    387: average_price
        28122   LOAD_NAME                     386: Return_Status
        28126   LOAD_METHOD                   352: upper
        28130   CALL_METHOD                   0
        28132   LOAD_CONST                    321: 'REJECTED'
        28136   COMPARE_OP                    2 (==)
        28138   POP_JUMP_IF_FALSE             14117 (to 28234)
        28142   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        28146   LOAD_NAME                     384: order_id
        28150   FORMAT_VALUE                  0
        28152   LOAD_CONST                    323: ', Ord_STS = '
        28156   LOAD_NAME                     385: Placed_Status
        28160   FORMAT_VALUE                  0
        28162   LOAD_CONST                    324: ', Ret_STS = '
        28166   LOAD_NAME                     386: Return_Status
        28170   FORMAT_VALUE                  0
        28172   LOAD_CONST                    333: '.'
        28176   BUILD_STRING                  7
        28178   STORE_NAME                    65: strMsg
        28180   LOAD_NAME                     59: iLog
        28182   LOAD_NAME                     65: strMsg
        28184   LOAD_CONST                    288: 5
        28188   LOAD_CONST                    20: True
        28190   LOAD_CONST                    43: ('sendTeleMsg',)
        28192   CALL_FUNCTION_KW              3
        28194   POP_TOP                       
        28196   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        28200   STORE_NAME                    65: strMsg
        28202   LOAD_NAME                     59: iLog
        28204   LOAD_NAME                     65: strMsg
        28206   LOAD_CONST                    42: 4
        28208   LOAD_CONST                    20: True
        28210   LOAD_CONST                    43: ('sendTeleMsg',)
        28212   CALL_FUNCTION_KW              3
        28214   POP_TOP                       
        28216   LOAD_NAME                     322: close_all_orders
        28220   CALL_FUNCTION                 0
        28222   POP_TOP                       
        28224   LOAD_NAME                     0: sys
        28226   LOAD_METHOD                   344: exit
        28230   CALL_METHOD                   0
        28232   POP_TOP                       
        28234   LOAD_NAME                     387: average_price
        28238   LOAD_CONST                    0: 0
        28240   COMPARE_OP                    4 (>)
        28242   POP_JUMP_IF_FALSE             14136 (to 28272)
        28246   LOAD_NAME                     386: Return_Status
        28250   LOAD_METHOD                   352: upper
        28254   CALL_METHOD                   0
        28256   LOAD_CONST                    327: 'COMPLETE'
        28260   COMPARE_OP                    2 (==)
        28262   POP_JUMP_IF_FALSE             14136 (to 28272)
        28266   LOAD_NAME                     387: average_price
        28270   STORE_GLOBAL                  221: Last_Traded_PE_Price
        28272   LOAD_GLOBAL                   76: read
        28274   LOAD_NAME                     376: Symbol
        28278   LOAD_GLOBAL                   382: df_cols
        28282   LOAD_CONST                    316: 'PE'
        28286   LOAD_CONST                    29: 1
        28288   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        28292   LOAD_GLOBAL                   221: NULL + strike_offset
        28294   LOAD_CONST                    292: -1
        28298   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        28302   BINARY_MULTIPLY               
        28304   LOAD_GLOBAL                   221: NULL + strike_offset
        28306   BINARY_MULTIPLY               
        28308   BUILD_LIST                    8
        28310   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        28312   LOAD_ATTR                     379: loc
        28316   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        28318   LOAD_NAME                     191: df_cols
        28320   BUILD_TUPLE                   2
        28322   STORE_SUBSCR                  
        28324   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        28326   LOAD_CONST                    29: 1
        28328   BINARY_ADD                    
        28330   STORE_GLOBAL                  190: df_king_cnt
        28332   LOAD_CONST                    20: True
        28334   STORE_GLOBAL                  170: First_Straddle
        28336   LOAD_CONST                    365: ' Placed PE Buy Market order for ATM Strike='
        28340   LOAD_GLOBAL                   382: df_cols
        28344   FORMAT_VALUE                  0
        28346   LOAD_CONST                    366: ', ATM PE='
        28350   LOAD_NAME                     387: average_price
        28354   FORMAT_VALUE                  0
        28356   LOAD_CONST                    330: ', Qty ='
        28360   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        28364   FORMAT_VALUE                  0
        28366   LOAD_CONST                    331: ', Ord_ID = '
        28370   LOAD_NAME                     384: order_id
        28374   FORMAT_VALUE                  0
        28376   LOAD_CONST                    323: ', Ord_STS = '
        28380   LOAD_NAME                     385: Placed_Status
        28384   FORMAT_VALUE                  0
        28386   LOAD_CONST                    324: ', Ret_STS = '
        28390   LOAD_NAME                     386: Return_Status
        28394   FORMAT_VALUE                  0
        28396   BUILD_STRING                  12
        28398   STORE_NAME                    65: strMsg
        28400   LOAD_NAME                     59: iLog
        28402   LOAD_NAME                     65: strMsg
        28404   LOAD_CONST                    288: 5
        28408   LOAD_CONST                    20: True
        28410   LOAD_CONST                    43: ('sendTeleMsg',)
        28412   CALL_FUNCTION_KW              3
        28414   POP_TOP                       
        28416   LOAD_NAME                     72: tl
        28418   LOAD_METHOD                   388: update_csv
        28422   LOAD_NAME                     376: Symbol
        28426   LOAD_CONST                    332: 'Buy'
        28430   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        28434   LOAD_GLOBAL                   221: NULL + strike_offset
        28436   LOAD_NAME                     384: order_id
        28440   LOAD_NAME                     385: Placed_Status
        28444   LOAD_NAME                     386: Return_Status
        28448   CALL_METHOD                   7
        28450   POP_TOP                       
        28452   LOAD_GLOBAL                   76: read
        28454   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        28458   LOAD_CONST                    0: 0
        28460   BINARY_SUBSCR                 
        28462   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        28466   LOAD_CONST                    29: 1
        28468   BINARY_SUBSCR                 
        28470   LOAD_CONST                    29: 1
        28472   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        28476   BINARY_MULTIPLY               
        28478   BUILD_LIST                    4
        28480   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        28482   LOAD_ATTR                     379: loc
        28486   LOAD_CONST                    0: 0
        28488   LOAD_NAME                     197: leg_cols
        28490   BUILD_TUPLE                   2
        28492   STORE_SUBSCR                  
        28494   LOAD_NAME                     24: pd
        28496   LOAD_METHOD                   380: concat
        28500   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        28502   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        28504   BUILD_LIST                    2
        28506   CALL_METHOD                   1
        28508   STORE_GLOBAL                  200: Current_legs
        28510   LOAD_CONST                    20: True
        28512   STORE_GLOBAL                  172: Queen_Order_Placed
        28514   LOAD_NAME                     297: K_Direction_Change_Count
        28518   LOAD_CONST                    29: 1
        28520   BINARY_ADD                    
        28522   STORE_NAME                    297: K_Direction_Change_Count
        28526   LOAD_NAME                     44: int
        28528   LOAD_NAME                     21: datetime
        28530   LOAD_ATTR                     21: datetime
        28532   LOAD_METHOD                   51: now
        28534   CALL_METHOD                   0
        28536   LOAD_METHOD                   52: strftime
        28538   LOAD_CONST                    50: '%H%M'
        28540   CALL_METHOD                   1
        28542   CALL_FUNCTION                 1
        28544   STORE_GLOBAL                  76: cur_HHMM
        28546   LOAD_NAME                     44: int
        28548   LOAD_NAME                     21: datetime
        28550   LOAD_ATTR                     21: datetime
        28552   LOAD_METHOD                   51: now
        28554   CALL_METHOD                   0
        28556   LOAD_METHOD                   52: strftime
        28558   LOAD_CONST                    291: '%H%M%S'
        28562   CALL_METHOD                   1
        28564   CALL_FUNCTION                 1
        28566   STORE_GLOBAL                  368: cur_HHMMSS
        28570   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        28574   LOAD_GLOBAL                   87: NULL + strBotTokenWObot
        28576   COMPARE_OP                    4 (>)
        28578   POP_JUMP_IF_FALSE             16634 (to 33268)
        28582   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        28586   LOAD_GLOBAL                   89: NULL + int
        28588   COMPARE_OP                    1 (<=)
        28590   POP_JUMP_IF_FALSE             16634 (to 33268)
        28594   LOAD_NAME                     21: datetime
        28596   LOAD_ATTR                     347: date
        28600   LOAD_METHOD                   348: today
        28604   CALL_METHOD                   0
        28606   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        28610   COMPARE_OP                    3 (!=)
        28612   POP_JUMP_IF_FALSE             14313 (to 28626)
        28616   LOAD_GLOBAL                   93: NULL + log_file_name
        28618   LOAD_CONST                    29: 1
        28620   COMPARE_OP                    2 (==)
        28622   POP_JUMP_IF_TRUE              14329 (to 28658)
        28626   LOAD_NAME                     21: datetime
        28628   LOAD_ATTR                     347: date
        28632   LOAD_METHOD                   348: today
        28636   CALL_METHOD                   0
        28638   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        28642   COMPARE_OP                    2 (==)
        28644   POP_JUMP_IF_FALSE             16634 (to 33268)
        28648   LOAD_GLOBAL                   92: log_file_name
        28650   LOAD_CONST                    29: 1
        28652   COMPARE_OP                    2 (==)
        28654   POP_JUMP_IF_FALSE             16634 (to 33268)
        28658   LOAD_GLOBAL                   236: expiry_Perlot_MTM_lock_profit
        28660   POP_JUMP_IF_TRUE              16634 (to 33268)
        28664   LOAD_NAME                     21: datetime
        28666   LOAD_ATTR                     21: datetime
        28668   LOAD_METHOD                   51: now
        28670   CALL_METHOD                   0
        28672   LOAD_ATTR                     372: minute
        28676   STORE_NAME                    207: cur_min
        28678   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        28682   LOAD_CONST                    29: 1
        28684   COMPARE_OP                    2 (==)
        28686   POP_JUMP_IF_FALSE             14406 (to 28812)
        28690   LOAD_GLOBAL                   171: NULL + King_Candle_Max_SL
        28692   LOAD_CONST                    20: True
        28694   COMPARE_OP                    2 (==)
        28696   POP_JUMP_IF_FALSE             14406 (to 28812)
        28700   LOAD_NAME                     44: int
        28702   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        28704   LOAD_CONST                    292: -1
        28708   BINARY_SUBSCR                 
        28710   CALL_FUNCTION                 1
        28712   LOAD_GLOBAL                   269: NULL + partial_profit_booking_enable
        28716   COMPARE_OP                    0 (<)
        28718   POP_JUMP_IF_TRUE              14389 (to 28778)
        28722   LOAD_GLOBAL                   126: getAccessToken
        28724   LOAD_CONST                    29: 1
        28726   COMPARE_OP                    2 (==)
        28728   POP_JUMP_IF_FALSE             14373 (to 28746)
        28732   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        28736   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        28740   COMPARE_OP                    1 (<=)
        28742   POP_JUMP_IF_TRUE              14389 (to 28778)
        28746   LOAD_GLOBAL                   126: getAccessToken
        28748   LOAD_CONST                    29: 1
        28750   COMPARE_OP                    3 (!=)
        28752   POP_JUMP_IF_FALSE             14406 (to 28812)
        28756   LOAD_NAME                     44: int
        28758   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        28760   LOAD_CONST                    292: -1
        28764   BINARY_SUBSCR                 
        28766   CALL_FUNCTION                 1
        28768   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        28772   COMPARE_OP                    1 (<=)
        28774   POP_JUMP_IF_FALSE             14406 (to 28812)
        28778   LOAD_GLOBAL                   74: cfg
        28780   LOAD_GLOBAL                   162: Trade_Nifty
        28782   COMPARE_OP                    5 (>=)
        28784   POP_JUMP_IF_FALSE             14406 (to 28812)
        28788   LOAD_CONST                    414: ' King Stoploss triggered : Max order_limit_per_day Reached. Exiting trade for the day '
        28792   STORE_NAME                    65: strMsg
        28794   LOAD_NAME                     59: iLog
        28796   LOAD_NAME                     65: strMsg
        28798   LOAD_CONST                    42: 4
        28800   LOAD_CONST                    20: True
        28802   LOAD_CONST                    43: ('sendTeleMsg',)
        28804   CALL_FUNCTION_KW              3
        28806   POP_TOP                       
        28808   LOAD_CONST                    29: 1
        28810   STORE_GLOBAL                  80: ExitTradenow
        28812   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        28816   LOAD_CONST                    29: 1
        28818   COMPARE_OP                    2 (==)
        28820   POP_JUMP_IF_FALSE             14473 (to 28946)
        28824   LOAD_GLOBAL                   171: NULL + King_Candle_Max_SL
        28826   LOAD_CONST                    20: True
        28828   COMPARE_OP                    2 (==)
        28830   POP_JUMP_IF_FALSE             14473 (to 28946)
        28834   LOAD_NAME                     44: int
        28836   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        28838   LOAD_CONST                    292: -1
        28842   BINARY_SUBSCR                 
        28844   CALL_FUNCTION                 1
        28846   LOAD_GLOBAL                   269: NULL + partial_profit_booking_enable
        28850   COMPARE_OP                    0 (<)
        28852   POP_JUMP_IF_TRUE              14456 (to 28912)
        28856   LOAD_GLOBAL                   126: getAccessToken
        28858   LOAD_CONST                    29: 1
        28860   COMPARE_OP                    2 (==)
        28862   POP_JUMP_IF_FALSE             14440 (to 28880)
        28866   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        28870   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        28874   COMPARE_OP                    1 (<=)
        28876   POP_JUMP_IF_TRUE              14456 (to 28912)
        28880   LOAD_GLOBAL                   126: getAccessToken
        28882   LOAD_CONST                    29: 1
        28884   COMPARE_OP                    3 (!=)
        28886   POP_JUMP_IF_FALSE             14473 (to 28946)
        28890   LOAD_NAME                     44: int
        28892   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        28894   LOAD_CONST                    292: -1
        28898   BINARY_SUBSCR                 
        28900   CALL_FUNCTION                 1
        28902   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        28906   COMPARE_OP                    1 (<=)
        28908   POP_JUMP_IF_FALSE             14473 (to 28946)
        28912   LOAD_GLOBAL                   76: read
        28914   LOAD_GLOBAL                   90: Send_Telegram
        28916   COMPARE_OP                    5 (>=)
        28918   POP_JUMP_IF_FALSE             14473 (to 28946)
        28922   LOAD_CONST                    415: ' King Stoploss triggered : Position change after MaxPositionChangeTime. Exiting trade for the day '
        28926   STORE_NAME                    65: strMsg
        28928   LOAD_NAME                     59: iLog
        28930   LOAD_NAME                     65: strMsg
        28932   LOAD_CONST                    42: 4
        28934   LOAD_CONST                    20: True
        28936   LOAD_CONST                    43: ('sendTeleMsg',)
        28938   CALL_FUNCTION_KW              3
        28940   POP_TOP                       
        28942   LOAD_CONST                    29: 1
        28944   STORE_GLOBAL                  80: ExitTradenow
        28946   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        28950   LOAD_CONST                    29: 1
        28952   COMPARE_OP                    2 (==)
        28954   POP_JUMP_IF_FALSE             15479 (to 30958)
        28958   LOAD_GLOBAL                   171: NULL + King_Candle_Max_SL
        28960   LOAD_CONST                    20: True
        28962   COMPARE_OP                    2 (==)
        28964   POP_JUMP_IF_FALSE             15479 (to 30958)
        28968   LOAD_NAME                     44: int
        28970   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        28972   LOAD_CONST                    292: -1
        28976   BINARY_SUBSCR                 
        28978   CALL_FUNCTION                 1
        28980   LOAD_GLOBAL                   269: NULL + partial_profit_booking_enable
        28984   COMPARE_OP                    0 (<)
        28986   POP_JUMP_IF_TRUE              14523 (to 29046)
        28990   LOAD_GLOBAL                   126: getAccessToken
        28992   LOAD_CONST                    29: 1
        28994   COMPARE_OP                    2 (==)
        28996   POP_JUMP_IF_FALSE             14507 (to 29014)
        29000   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        29004   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        29008   COMPARE_OP                    1 (<=)
        29010   POP_JUMP_IF_TRUE              14523 (to 29046)
        29014   LOAD_GLOBAL                   126: getAccessToken
        29016   LOAD_CONST                    29: 1
        29018   COMPARE_OP                    3 (!=)
        29020   POP_JUMP_IF_FALSE             15479 (to 30958)
        29024   LOAD_NAME                     44: int
        29026   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        29028   LOAD_CONST                    292: -1
        29032   BINARY_SUBSCR                 
        29034   CALL_FUNCTION                 1
        29036   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        29040   COMPARE_OP                    1 (<=)
        29042   POP_JUMP_IF_FALSE             15479 (to 30958)
        29046   LOAD_GLOBAL                   76: read
        29048   LOAD_GLOBAL                   90: Send_Telegram
        29050   COMPARE_OP                    0 (<)
        29052   POP_JUMP_IF_FALSE             15479 (to 30958)
        29056   LOAD_GLOBAL                   74: cfg
        29058   LOAD_GLOBAL                   162: Trade_Nifty
        29060   COMPARE_OP                    0 (<)
        29062   POP_JUMP_IF_FALSE             15479 (to 30958)
        29066   LOAD_NAME                     207: cur_min
        29068   STORE_NAME                    215: King_ST_min
        29070   LOAD_NAME                     44: int
        29072   LOAD_NAME                     91: float
        29074   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        29076   LOAD_CONST                    292: -1
        29080   BINARY_SUBSCR                 
        29082   CALL_FUNCTION                 1
        29084   CALL_FUNCTION                 1
        29086   LOAD_GLOBAL                   269: NULL + partial_profit_booking_enable
        29090   COMPARE_OP                    0 (<)
        29092   POP_JUMP_IF_FALSE             14580 (to 29160)
        29096   LOAD_CONST                    416: ' King Candle SL Hit LTP = '
        29100   LOAD_NAME                     44: int
        29102   LOAD_NAME                     91: float
        29104   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        29106   LOAD_CONST                    292: -1
        29110   BINARY_SUBSCR                 
        29112   CALL_FUNCTION                 1
        29114   CALL_FUNCTION                 1
        29116   FORMAT_VALUE                  0
        29118   LOAD_CONST                    417: ', lower than King SL= '
        29122   LOAD_NAME                     374: round
        29126   LOAD_GLOBAL                   269: NULL + partial_profit_booking_enable
        29130   LOAD_CONST                    29: 1
        29132   CALL_FUNCTION                 2
        29134   FORMAT_VALUE                  0
        29136   LOAD_CONST                    407: ' '
        29140   BUILD_STRING                  5
        29142   STORE_NAME                    65: strMsg
        29144   LOAD_NAME                     59: iLog
        29146   LOAD_NAME                     65: strMsg
        29148   LOAD_CONST                    52: 2
        29150   LOAD_CONST                    20: True
        29152   LOAD_CONST                    43: ('sendTeleMsg',)
        29154   CALL_FUNCTION_KW              3
        29156   POP_TOP                       
        29158   JUMP_FORWARD                  64 (to 29288)
        29160   LOAD_GLOBAL                   126: getAccessToken
        29162   LOAD_CONST                    29: 1
        29164   COMPARE_OP                    2 (==)
        29166   POP_JUMP_IF_FALSE             14613 (to 29226)
        29170   LOAD_CONST                    418: ' King Candle SuperTrend SL Hit Candle Close = '
        29174   LOAD_NAME                     44: int
        29176   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        29180   CALL_FUNCTION                 1
        29182   FORMAT_VALUE                  0
        29184   LOAD_CONST                    419: ', lower than King SuperTrend SL= '
        29188   LOAD_NAME                     374: round
        29192   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        29196   LOAD_CONST                    29: 1
        29198   CALL_FUNCTION                 2
        29200   FORMAT_VALUE                  0
        29202   LOAD_CONST                    407: ' '
        29206   BUILD_STRING                  5
        29208   STORE_NAME                    65: strMsg
        29210   LOAD_NAME                     59: iLog
        29212   LOAD_NAME                     65: strMsg
        29214   LOAD_CONST                    52: 2
        29216   LOAD_CONST                    20: True
        29218   LOAD_CONST                    43: ('sendTeleMsg',)
        29220   CALL_FUNCTION_KW              3
        29222   POP_TOP                       
        29224   JUMP_FORWARD                  31 (to 29288)
        29226   LOAD_CONST                    420: ' King Candle SuperTrend SL Hit LTP = '
        29230   LOAD_NAME                     44: int
        29232   LOAD_NAME                     91: float
        29234   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        29236   LOAD_CONST                    292: -1
        29240   BINARY_SUBSCR                 
        29242   CALL_FUNCTION                 1
        29244   CALL_FUNCTION                 1
        29246   FORMAT_VALUE                  0
        29248   LOAD_CONST                    419: ', lower than King SuperTrend SL= '
        29252   LOAD_NAME                     374: round
        29256   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        29260   LOAD_CONST                    29: 1
        29262   CALL_FUNCTION                 2
        29264   FORMAT_VALUE                  0
        29266   LOAD_CONST                    407: ' '
        29270   BUILD_STRING                  5
        29272   STORE_NAME                    65: strMsg
        29274   LOAD_NAME                     59: iLog
        29276   LOAD_NAME                     65: strMsg
        29278   LOAD_CONST                    52: 2
        29280   LOAD_CONST                    20: True
        29282   LOAD_CONST                    43: ('sendTeleMsg',)
        29284   CALL_FUNCTION_KW              3
        29286   POP_TOP                       
        29288   LOAD_GLOBAL                   78: get
        29290   LOAD_CONST                    29: 1
        29292   COMPARE_OP                    2 (==)
        29294   POP_JUMP_IF_FALSE             14894 (to 29788)
        29298   LOAD_GLOBAL                   247: NULL + ADX_Period
        29300   LOAD_CONST                    29: 1
        29302   COMPARE_OP                    2 (==)
        29304   POP_JUMP_IF_FALSE             14739 (to 29478)
        29308   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        29312   STORE_GLOBAL                  222: Last_Traded_CE_Price
        29314   LOAD_CONST                    421: '  Place SELL order for Closing Existing '
        29318   LOAD_GLOBAL                   381: NULL + df_king_cnt
        29322   FORMAT_VALUE                  0
        29324   LOAD_CONST                    349: ' CE at '
        29328   LOAD_GLOBAL                   222: entry_price
        29330   FORMAT_VALUE                  0
        29332   BUILD_STRING                  4
        29334   STORE_NAME                    65: strMsg
        29336   LOAD_NAME                     59: iLog
        29338   LOAD_NAME                     65: strMsg
        29340   LOAD_CONST                    288: 5
        29344   LOAD_CONST                    20: True
        29346   LOAD_CONST                    43: ('sendTeleMsg',)
        29348   CALL_FUNCTION_KW              3
        29350   POP_TOP                       
        29352   LOAD_GLOBAL                   74: cfg
        29354   LOAD_CONST                    29: 1
        29356   BINARY_ADD                    
        29358   STORE_GLOBAL                  74: order_count
        29360   LOAD_GLOBAL                   76: read
        29362   LOAD_NAME                     376: Symbol
        29366   LOAD_GLOBAL                   381: NULL + df_king_cnt
        29370   LOAD_CONST                    315: 'CE'
        29374   LOAD_CONST                    292: -1
        29378   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        29382   LOAD_GLOBAL                   222: entry_price
        29384   LOAD_CONST                    29: 1
        29386   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        29390   BINARY_MULTIPLY               
        29392   LOAD_GLOBAL                   222: entry_price
        29394   BINARY_MULTIPLY               
        29396   BUILD_LIST                    8
        29398   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        29400   LOAD_ATTR                     379: loc
        29404   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        29406   LOAD_NAME                     191: df_cols
        29408   BUILD_TUPLE                   2
        29410   STORE_SUBSCR                  
        29412   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        29414   LOAD_CONST                    29: 1
        29416   BINARY_ADD                    
        29418   STORE_GLOBAL                  190: df_king_cnt
        29420   LOAD_GLOBAL                   76: read
        29422   LOAD_GLOBAL                   360: PE_TGT_Triggered
        29426   LOAD_CONST                    0: 0
        29428   BINARY_SUBSCR                 
        29430   LOAD_GLOBAL                   360: PE_TGT_Triggered
        29434   LOAD_CONST                    29: 1
        29436   BINARY_SUBSCR                 
        29438   LOAD_CONST                    0: 0
        29440   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        29444   BINARY_MULTIPLY               
        29446   BUILD_LIST                    4
        29448   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        29450   LOAD_ATTR                     379: loc
        29454   LOAD_CONST                    0: 0
        29456   LOAD_NAME                     197: leg_cols
        29458   BUILD_TUPLE                   2
        29460   STORE_SUBSCR                  
        29462   LOAD_NAME                     24: pd
        29464   LOAD_METHOD                   380: concat
        29468   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        29470   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        29472   BUILD_LIST                    2
        29474   CALL_METHOD                   1
        29476   STORE_GLOBAL                  200: Current_legs
        29478   SETUP_FINALLY                 8 (to 29496)
        29480   LOAD_NAME                     331: get_option_tokens
        29484   LOAD_CONST                    315: 'CE'
        29488   CALL_FUNCTION                 1
        29490   POP_TOP                       
        29492   POP_BLOCK                     
        29494   JUMP_FORWARD                  60 (to 29616)
        29496   POP_TOP                       
        29498   POP_TOP                       
        29500   POP_TOP                       
        29502   LOAD_NAME                     2: time
        29504   LOAD_METHOD                   355: sleep
        29508   LOAD_CONST                    288: 5
        29512   CALL_METHOD                   1
        29514   POP_TOP                       
        29516   SETUP_FINALLY                 8 (to 29534)
        29518   LOAD_NAME                     331: get_option_tokens
        29522   LOAD_CONST                    315: 'CE'
        29526   CALL_FUNCTION                 1
        29528   POP_TOP                       
        29530   POP_BLOCK                     
        29532   JUMP_FORWARD                  40 (to 29614)
        29534   DUP_TOP                       
        29536   LOAD_NAME                     357: Exception
        29540   JUMP_IF_NOT_EXC_MATCH         14806 (to 29612)
        29544   POP_TOP                       
        29546   STORE_NAME                    358: ex
        29550   POP_TOP                       
        29552   SETUP_FINALLY                 23 (to 29600)
        29554   LOAD_NAME                     59: iLog
        29556   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        29560   LOAD_NAME                     343: str
        29564   LOAD_NAME                     358: ex
        29568   CALL_FUNCTION                 1
        29570   BINARY_ADD                    
        29572   LOAD_CONST                    271: 3
        29576   LOAD_CONST                    20: True
        29578   LOAD_CONST                    43: ('sendTeleMsg',)
        29580   CALL_FUNCTION_KW              3
        29582   POP_TOP                       
        29584   POP_BLOCK                     
        29586   POP_EXCEPT                    
        29588   LOAD_CONST                    1: None
        29590   STORE_NAME                    358: ex
        29594   DELETE_NAME                   358: ex
        29598   JUMP_FORWARD                  7 (to 29614)
        29600   LOAD_CONST                    1: None
        29602   STORE_NAME                    358: ex
        29606   DELETE_NAME                   358: ex
        29610   RERAISE                       1
        29612   RERAISE                       0
        29614   POP_EXCEPT                    
        29616   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        29620   STORE_GLOBAL                  222: Last_Traded_CE_Price
        29622   LOAD_CONST                    422: '  Place SELL order for new '
        29626   LOAD_GLOBAL                   381: NULL + df_king_cnt
        29630   FORMAT_VALUE                  0
        29632   LOAD_CONST                    349: ' CE at '
        29636   LOAD_GLOBAL                   222: entry_price
        29638   FORMAT_VALUE                  0
        29640   BUILD_STRING                  4
        29642   STORE_NAME                    65: strMsg
        29644   LOAD_NAME                     59: iLog
        29646   LOAD_NAME                     65: strMsg
        29648   LOAD_CONST                    288: 5
        29652   LOAD_CONST                    20: True
        29654   LOAD_CONST                    43: ('sendTeleMsg',)
        29656   CALL_FUNCTION_KW              3
        29658   POP_TOP                       
        29660   LOAD_GLOBAL                   74: cfg
        29662   LOAD_CONST                    29: 1
        29664   BINARY_ADD                    
        29666   STORE_GLOBAL                  74: order_count
        29668   LOAD_GLOBAL                   76: read
        29670   LOAD_NAME                     376: Symbol
        29674   LOAD_GLOBAL                   381: NULL + df_king_cnt
        29678   LOAD_CONST                    315: 'CE'
        29682   LOAD_CONST                    292: -1
        29686   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        29690   LOAD_GLOBAL                   222: entry_price
        29692   LOAD_CONST                    29: 1
        29694   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        29698   BINARY_MULTIPLY               
        29700   LOAD_GLOBAL                   222: entry_price
        29702   BINARY_MULTIPLY               
        29704   BUILD_LIST                    8
        29706   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        29708   LOAD_ATTR                     379: loc
        29712   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        29714   LOAD_NAME                     191: df_cols
        29716   BUILD_TUPLE                   2
        29718   STORE_SUBSCR                  
        29720   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        29722   LOAD_CONST                    29: 1
        29724   BINARY_ADD                    
        29726   STORE_GLOBAL                  190: df_king_cnt
        29728   LOAD_GLOBAL                   76: read
        29730   LOAD_GLOBAL                   360: PE_TGT_Triggered
        29734   LOAD_CONST                    0: 0
        29736   BINARY_SUBSCR                 
        29738   LOAD_GLOBAL                   360: PE_TGT_Triggered
        29742   LOAD_CONST                    29: 1
        29744   BINARY_SUBSCR                 
        29746   LOAD_CONST                    292: -1
        29750   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        29754   BINARY_MULTIPLY               
        29756   BUILD_LIST                    4
        29758   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        29760   LOAD_ATTR                     379: loc
        29764   LOAD_CONST                    0: 0
        29766   LOAD_NAME                     197: leg_cols
        29768   BUILD_TUPLE                   2
        29770   STORE_SUBSCR                  
        29772   LOAD_NAME                     24: pd
        29774   LOAD_METHOD                   380: concat
        29778   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        29780   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        29782   BUILD_LIST                    2
        29784   CALL_METHOD                   1
        29786   STORE_GLOBAL                  200: Current_legs
        29788   LOAD_GLOBAL                   78: get
        29790   LOAD_CONST                    0: 0
        29792   COMPARE_OP                    2 (==)
        29794   POP_JUMP_IF_FALSE             15468 (to 30936)
        29798   LOAD_GLOBAL                   247: NULL + ADX_Period
        29800   LOAD_CONST                    29: 1
        29802   COMPARE_OP                    2 (==)
        29804   POP_JUMP_IF_FALSE             15151 (to 30302)
        29808   LOAD_NAME                     308: place_order
        29812   LOAD_CONST                    337: 'S'
        29816   LOAD_GLOBAL                   360: PE_TGT_Triggered
        29820   LOAD_CONST                    52: 2
        29822   BINARY_SUBSCR                 
        29824   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        29828   CALL_FUNCTION                 3
        29830   STORE_GLOBAL                  383: order_id_CE
        29834   LOAD_GLOBAL                   74: cfg
        29836   LOAD_CONST                    29: 1
        29838   BINARY_ADD                    
        29840   STORE_GLOBAL                  74: order_count
        29842   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        29846   STORE_GLOBAL                  222: Last_Traded_CE_Price
        29848   LOAD_GLOBAL                   383: NULL + df_cols
        29852   LOAD_CONST                    319: 'norenordno'
        29856   BINARY_SUBSCR                 
        29858   STORE_NAME                    384: order_id
        29862   LOAD_NAME                     311: get_order_symbol
        29866   LOAD_NAME                     384: order_id
        29870   CALL_FUNCTION                 1
        29872   STORE_NAME                    376: Symbol
        29876   LOAD_GLOBAL                   383: NULL + df_cols
        29880   LOAD_CONST                    320: 'stat'
        29884   BINARY_SUBSCR                 
        29886   STORE_NAME                    385: Placed_Status
        29890   LOAD_NAME                     309: get_order_status
        29894   LOAD_NAME                     384: order_id
        29898   CALL_FUNCTION                 1
        29900   STORE_NAME                    386: Return_Status
        29904   LOAD_NAME                     310: get_order_price
        29908   LOAD_NAME                     384: order_id
        29912   CALL_FUNCTION                 1
        29914   STORE_NAME                    387: average_price
        29918   LOAD_NAME                     386: Return_Status
        29922   LOAD_METHOD                   352: upper
        29926   CALL_METHOD                   0
        29928   LOAD_CONST                    321: 'REJECTED'
        29932   COMPARE_OP                    2 (==)
        29934   POP_JUMP_IF_FALSE             15015 (to 30030)
        29938   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        29942   LOAD_NAME                     384: order_id
        29946   FORMAT_VALUE                  0
        29948   LOAD_CONST                    323: ', Ord_STS = '
        29952   LOAD_NAME                     385: Placed_Status
        29956   FORMAT_VALUE                  0
        29958   LOAD_CONST                    324: ', Ret_STS = '
        29962   LOAD_NAME                     386: Return_Status
        29966   FORMAT_VALUE                  0
        29968   LOAD_CONST                    333: '.'
        29972   BUILD_STRING                  7
        29974   STORE_NAME                    65: strMsg
        29976   LOAD_NAME                     59: iLog
        29978   LOAD_NAME                     65: strMsg
        29980   LOAD_CONST                    288: 5
        29984   LOAD_CONST                    20: True
        29986   LOAD_CONST                    43: ('sendTeleMsg',)
        29988   CALL_FUNCTION_KW              3
        29990   POP_TOP                       
        29992   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        29996   STORE_NAME                    65: strMsg
        29998   LOAD_NAME                     59: iLog
        30000   LOAD_NAME                     65: strMsg
        30002   LOAD_CONST                    42: 4
        30004   LOAD_CONST                    20: True
        30006   LOAD_CONST                    43: ('sendTeleMsg',)
        30008   CALL_FUNCTION_KW              3
        30010   POP_TOP                       
        30012   LOAD_NAME                     322: close_all_orders
        30016   CALL_FUNCTION                 0
        30018   POP_TOP                       
        30020   LOAD_NAME                     0: sys
        30022   LOAD_METHOD                   344: exit
        30026   CALL_METHOD                   0
        30028   POP_TOP                       
        30030   LOAD_NAME                     387: average_price
        30034   LOAD_CONST                    0: 0
        30036   COMPARE_OP                    4 (>)
        30038   POP_JUMP_IF_FALSE             15034 (to 30068)
        30042   LOAD_NAME                     386: Return_Status
        30046   LOAD_METHOD                   352: upper
        30050   CALL_METHOD                   0
        30052   LOAD_CONST                    327: 'COMPLETE'
        30056   COMPARE_OP                    2 (==)
        30058   POP_JUMP_IF_FALSE             15034 (to 30068)
        30062   LOAD_NAME                     387: average_price
        30066   STORE_GLOBAL                  222: Last_Traded_CE_Price
        30068   LOAD_GLOBAL                   76: read
        30070   LOAD_NAME                     376: Symbol
        30074   LOAD_GLOBAL                   381: NULL + df_king_cnt
        30078   LOAD_CONST                    315: 'CE'
        30082   LOAD_CONST                    292: -1
        30086   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30090   LOAD_GLOBAL                   222: entry_price
        30092   LOAD_CONST                    29: 1
        30094   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30098   BINARY_MULTIPLY               
        30100   LOAD_GLOBAL                   222: entry_price
        30102   BINARY_MULTIPLY               
        30104   BUILD_LIST                    8
        30106   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        30108   LOAD_ATTR                     379: loc
        30112   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        30114   LOAD_NAME                     191: df_cols
        30116   BUILD_TUPLE                   2
        30118   STORE_SUBSCR                  
        30120   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        30122   LOAD_CONST                    29: 1
        30124   BINARY_ADD                    
        30126   STORE_GLOBAL                  190: df_king_cnt
        30128   LOAD_CONST                    354: ' Placed CE Sell Market order for ATM Strike='
        30132   LOAD_GLOBAL                   381: NULL + df_king_cnt
        30136   FORMAT_VALUE                  0
        30138   LOAD_CONST                    353: ', ATM CE='
        30142   LOAD_NAME                     387: average_price
        30146   FORMAT_VALUE                  0
        30148   LOAD_CONST                    330: ', Qty ='
        30152   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30156   FORMAT_VALUE                  0
        30158   LOAD_CONST                    331: ', Ord_ID = '
        30162   LOAD_NAME                     384: order_id
        30166   FORMAT_VALUE                  0
        30168   LOAD_CONST                    323: ', Ord_STS = '
        30172   LOAD_NAME                     385: Placed_Status
        30176   FORMAT_VALUE                  0
        30178   LOAD_CONST                    324: ', Ret_STS = '
        30182   LOAD_NAME                     386: Return_Status
        30186   FORMAT_VALUE                  0
        30188   BUILD_STRING                  12
        30190   STORE_NAME                    65: strMsg
        30192   LOAD_NAME                     59: iLog
        30194   LOAD_NAME                     65: strMsg
        30196   LOAD_CONST                    288: 5
        30200   LOAD_CONST                    20: True
        30202   LOAD_CONST                    43: ('sendTeleMsg',)
        30204   CALL_FUNCTION_KW              3
        30206   POP_TOP                       
        30208   LOAD_NAME                     72: tl
        30210   LOAD_METHOD                   388: update_csv
        30214   LOAD_NAME                     376: Symbol
        30218   LOAD_CONST                    339: 'Sell'
        30222   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30226   LOAD_GLOBAL                   222: entry_price
        30228   LOAD_NAME                     384: order_id
        30232   LOAD_NAME                     385: Placed_Status
        30236   LOAD_NAME                     386: Return_Status
        30240   CALL_METHOD                   7
        30242   POP_TOP                       
        30244   LOAD_GLOBAL                   76: read
        30246   LOAD_GLOBAL                   360: PE_TGT_Triggered
        30250   LOAD_CONST                    0: 0
        30252   BINARY_SUBSCR                 
        30254   LOAD_GLOBAL                   360: PE_TGT_Triggered
        30258   LOAD_CONST                    29: 1
        30260   BINARY_SUBSCR                 
        30262   LOAD_CONST                    0: 0
        30264   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30268   BINARY_MULTIPLY               
        30270   BUILD_LIST                    4
        30272   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        30274   LOAD_ATTR                     379: loc
        30278   LOAD_CONST                    0: 0
        30280   LOAD_NAME                     197: leg_cols
        30282   BUILD_TUPLE                   2
        30284   STORE_SUBSCR                  
        30286   LOAD_NAME                     24: pd
        30288   LOAD_METHOD                   380: concat
        30292   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        30294   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        30296   BUILD_LIST                    2
        30298   CALL_METHOD                   1
        30300   STORE_GLOBAL                  200: Current_legs
        30302   SETUP_FINALLY                 8 (to 30320)
        30304   LOAD_NAME                     331: get_option_tokens
        30308   LOAD_CONST                    315: 'CE'
        30312   CALL_FUNCTION                 1
        30314   POP_TOP                       
        30316   POP_BLOCK                     
        30318   JUMP_FORWARD                  60 (to 30440)
        30320   POP_TOP                       
        30322   POP_TOP                       
        30324   POP_TOP                       
        30326   LOAD_NAME                     2: time
        30328   LOAD_METHOD                   355: sleep
        30332   LOAD_CONST                    288: 5
        30336   CALL_METHOD                   1
        30338   POP_TOP                       
        30340   SETUP_FINALLY                 8 (to 30358)
        30342   LOAD_NAME                     331: get_option_tokens
        30346   LOAD_CONST                    315: 'CE'
        30350   CALL_FUNCTION                 1
        30352   POP_TOP                       
        30354   POP_BLOCK                     
        30356   JUMP_FORWARD                  40 (to 30438)
        30358   DUP_TOP                       
        30360   LOAD_NAME                     357: Exception
        30364   JUMP_IF_NOT_EXC_MATCH         15218 (to 30436)
        30368   POP_TOP                       
        30370   STORE_NAME                    358: ex
        30374   POP_TOP                       
        30376   SETUP_FINALLY                 23 (to 30424)
        30378   LOAD_NAME                     59: iLog
        30380   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        30384   LOAD_NAME                     343: str
        30388   LOAD_NAME                     358: ex
        30392   CALL_FUNCTION                 1
        30394   BINARY_ADD                    
        30396   LOAD_CONST                    271: 3
        30400   LOAD_CONST                    20: True
        30402   LOAD_CONST                    43: ('sendTeleMsg',)
        30404   CALL_FUNCTION_KW              3
        30406   POP_TOP                       
        30408   POP_BLOCK                     
        30410   POP_EXCEPT                    
        30412   LOAD_CONST                    1: None
        30414   STORE_NAME                    358: ex
        30418   DELETE_NAME                   358: ex
        30422   JUMP_FORWARD                  7 (to 30438)
        30424   LOAD_CONST                    1: None
        30426   STORE_NAME                    358: ex
        30430   DELETE_NAME                   358: ex
        30434   RERAISE                       1
        30436   RERAISE                       0
        30438   POP_EXCEPT                    
        30440   LOAD_NAME                     308: place_order
        30444   LOAD_CONST                    337: 'S'
        30448   LOAD_GLOBAL                   360: PE_TGT_Triggered
        30452   LOAD_CONST                    52: 2
        30454   BINARY_SUBSCR                 
        30456   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30460   CALL_FUNCTION                 3
        30462   STORE_NAME                    394: order_id_CE1
        30466   LOAD_GLOBAL                   74: cfg
        30468   LOAD_CONST                    29: 1
        30470   BINARY_ADD                    
        30472   STORE_GLOBAL                  74: order_count
        30474   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        30478   STORE_GLOBAL                  222: Last_Traded_CE_Price
        30480   LOAD_NAME                     394: order_id_CE1
        30484   LOAD_CONST                    319: 'norenordno'
        30488   BINARY_SUBSCR                 
        30490   STORE_NAME                    384: order_id
        30494   LOAD_NAME                     311: get_order_symbol
        30498   LOAD_NAME                     384: order_id
        30502   CALL_FUNCTION                 1
        30504   STORE_NAME                    376: Symbol
        30508   LOAD_NAME                     394: order_id_CE1
        30512   LOAD_CONST                    320: 'stat'
        30516   BINARY_SUBSCR                 
        30518   STORE_NAME                    385: Placed_Status
        30522   LOAD_NAME                     309: get_order_status
        30526   LOAD_NAME                     384: order_id
        30530   CALL_FUNCTION                 1
        30532   STORE_NAME                    386: Return_Status
        30536   LOAD_NAME                     310: get_order_price
        30540   LOAD_NAME                     384: order_id
        30544   CALL_FUNCTION                 1
        30546   STORE_NAME                    387: average_price
        30550   LOAD_NAME                     386: Return_Status
        30554   LOAD_METHOD                   352: upper
        30558   CALL_METHOD                   0
        30560   LOAD_CONST                    321: 'REJECTED'
        30564   COMPARE_OP                    2 (==)
        30566   POP_JUMP_IF_FALSE             15331 (to 30662)
        30570   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        30574   LOAD_NAME                     384: order_id
        30578   FORMAT_VALUE                  0
        30580   LOAD_CONST                    323: ', Ord_STS = '
        30584   LOAD_NAME                     385: Placed_Status
        30588   FORMAT_VALUE                  0
        30590   LOAD_CONST                    324: ', Ret_STS = '
        30594   LOAD_NAME                     386: Return_Status
        30598   FORMAT_VALUE                  0
        30600   LOAD_CONST                    333: '.'
        30604   BUILD_STRING                  7
        30606   STORE_NAME                    65: strMsg
        30608   LOAD_NAME                     59: iLog
        30610   LOAD_NAME                     65: strMsg
        30612   LOAD_CONST                    288: 5
        30616   LOAD_CONST                    20: True
        30618   LOAD_CONST                    43: ('sendTeleMsg',)
        30620   CALL_FUNCTION_KW              3
        30622   POP_TOP                       
        30624   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        30628   STORE_NAME                    65: strMsg
        30630   LOAD_NAME                     59: iLog
        30632   LOAD_NAME                     65: strMsg
        30634   LOAD_CONST                    42: 4
        30636   LOAD_CONST                    20: True
        30638   LOAD_CONST                    43: ('sendTeleMsg',)
        30640   CALL_FUNCTION_KW              3
        30642   POP_TOP                       
        30644   LOAD_NAME                     322: close_all_orders
        30648   CALL_FUNCTION                 0
        30650   POP_TOP                       
        30652   LOAD_NAME                     0: sys
        30654   LOAD_METHOD                   344: exit
        30658   CALL_METHOD                   0
        30660   POP_TOP                       
        30662   LOAD_NAME                     387: average_price
        30666   LOAD_CONST                    0: 0
        30668   COMPARE_OP                    4 (>)
        30670   POP_JUMP_IF_FALSE             15350 (to 30700)
        30674   LOAD_NAME                     386: Return_Status
        30678   LOAD_METHOD                   352: upper
        30682   CALL_METHOD                   0
        30684   LOAD_CONST                    327: 'COMPLETE'
        30688   COMPARE_OP                    2 (==)
        30690   POP_JUMP_IF_FALSE             15350 (to 30700)
        30694   LOAD_NAME                     387: average_price
        30698   STORE_GLOBAL                  222: Last_Traded_CE_Price
        30700   LOAD_GLOBAL                   76: read
        30702   LOAD_NAME                     376: Symbol
        30706   LOAD_GLOBAL                   381: NULL + df_king_cnt
        30710   LOAD_CONST                    315: 'CE'
        30714   LOAD_CONST                    292: -1
        30718   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30722   LOAD_GLOBAL                   222: entry_price
        30724   LOAD_CONST                    29: 1
        30726   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30730   BINARY_MULTIPLY               
        30732   LOAD_GLOBAL                   222: entry_price
        30734   BINARY_MULTIPLY               
        30736   BUILD_LIST                    8
        30738   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        30740   LOAD_ATTR                     379: loc
        30744   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        30746   LOAD_NAME                     191: df_cols
        30748   BUILD_TUPLE                   2
        30750   STORE_SUBSCR                  
        30752   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        30754   LOAD_CONST                    29: 1
        30756   BINARY_ADD                    
        30758   STORE_GLOBAL                  190: df_king_cnt
        30760   LOAD_CONST                    354: ' Placed CE Sell Market order for ATM Strike='
        30764   LOAD_GLOBAL                   381: NULL + df_king_cnt
        30768   FORMAT_VALUE                  0
        30770   LOAD_CONST                    353: ', ATM CE='
        30774   LOAD_NAME                     387: average_price
        30778   FORMAT_VALUE                  0
        30780   LOAD_CONST                    330: ', Qty ='
        30784   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30788   FORMAT_VALUE                  0
        30790   LOAD_CONST                    331: ', Ord_ID = '
        30794   LOAD_NAME                     384: order_id
        30798   FORMAT_VALUE                  0
        30800   LOAD_CONST                    323: ', Ord_STS = '
        30804   LOAD_NAME                     385: Placed_Status
        30808   FORMAT_VALUE                  0
        30810   LOAD_CONST                    324: ', Ret_STS = '
        30814   LOAD_NAME                     386: Return_Status
        30818   FORMAT_VALUE                  0
        30820   BUILD_STRING                  12
        30822   STORE_NAME                    65: strMsg
        30824   LOAD_NAME                     59: iLog
        30826   LOAD_NAME                     65: strMsg
        30828   LOAD_CONST                    288: 5
        30832   LOAD_CONST                    20: True
        30834   LOAD_CONST                    43: ('sendTeleMsg',)
        30836   CALL_FUNCTION_KW              3
        30838   POP_TOP                       
        30840   LOAD_NAME                     72: tl
        30842   LOAD_METHOD                   388: update_csv
        30846   LOAD_NAME                     376: Symbol
        30850   LOAD_CONST                    339: 'Sell'
        30854   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30858   LOAD_GLOBAL                   222: entry_price
        30860   LOAD_NAME                     384: order_id
        30864   LOAD_NAME                     385: Placed_Status
        30868   LOAD_NAME                     386: Return_Status
        30872   CALL_METHOD                   7
        30874   POP_TOP                       
        30876   LOAD_GLOBAL                   76: read
        30878   LOAD_GLOBAL                   360: PE_TGT_Triggered
        30882   LOAD_CONST                    0: 0
        30884   BINARY_SUBSCR                 
        30886   LOAD_GLOBAL                   360: PE_TGT_Triggered
        30890   LOAD_CONST                    29: 1
        30892   BINARY_SUBSCR                 
        30894   LOAD_CONST                    292: -1
        30898   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        30902   BINARY_MULTIPLY               
        30904   BUILD_LIST                    4
        30906   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        30908   LOAD_ATTR                     379: loc
        30912   LOAD_CONST                    0: 0
        30914   LOAD_NAME                     197: leg_cols
        30916   BUILD_TUPLE                   2
        30918   STORE_SUBSCR                  
        30920   LOAD_NAME                     24: pd
        30922   LOAD_METHOD                   380: concat
        30926   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        30928   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        30930   BUILD_LIST                    2
        30932   CALL_METHOD                   1
        30934   STORE_GLOBAL                  200: Current_legs
        30936   LOAD_CONST                    30: False
        30938   STORE_GLOBAL                  171: King_Order_Placed
        30940   LOAD_CONST                    0: 0
        30942   STORE_GLOBAL                  296: K_Direction
        30946   LOAD_NAME                     297: K_Direction_Change_Count
        30950   LOAD_CONST                    29: 1
        30952   BINARY_ADD                    
        30954   STORE_NAME                    297: K_Direction_Change_Count
        30958   LOAD_NAME                     44: int
        30960   LOAD_NAME                     21: datetime
        30962   LOAD_ATTR                     21: datetime
        30964   LOAD_METHOD                   51: now
        30966   CALL_METHOD                   0
        30968   LOAD_METHOD                   52: strftime
        30970   LOAD_CONST                    50: '%H%M'
        30972   CALL_METHOD                   1
        30974   CALL_FUNCTION                 1
        30976   STORE_GLOBAL                  76: cur_HHMM
        30978   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        30982   LOAD_CONST                    292: -1
        30986   COMPARE_OP                    2 (==)
        30988   POP_JUMP_IF_FALSE             15557 (to 31114)
        30992   LOAD_GLOBAL                   172: time_offset_sec
        30994   LOAD_CONST                    20: True
        30996   COMPARE_OP                    2 (==)
        30998   POP_JUMP_IF_FALSE             15557 (to 31114)
        31002   LOAD_NAME                     44: int
        31004   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31006   LOAD_CONST                    292: -1
        31010   BINARY_SUBSCR                 
        31012   CALL_FUNCTION                 1
        31014   LOAD_GLOBAL                   286: max_entry_time_exit
        31018   COMPARE_OP                    4 (>)
        31020   POP_JUMP_IF_TRUE              15540 (to 31080)
        31024   LOAD_GLOBAL                   126: getAccessToken
        31026   LOAD_CONST                    29: 1
        31028   COMPARE_OP                    2 (==)
        31030   POP_JUMP_IF_FALSE             15524 (to 31048)
        31034   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        31038   LOAD_GLOBAL                   294: hedge_buy_price
        31042   COMPARE_OP                    5 (>=)
        31044   POP_JUMP_IF_TRUE              15540 (to 31080)
        31048   LOAD_GLOBAL                   126: getAccessToken
        31050   LOAD_CONST                    29: 1
        31052   COMPARE_OP                    3 (!=)
        31054   POP_JUMP_IF_FALSE             15557 (to 31114)
        31058   LOAD_NAME                     44: int
        31060   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31062   LOAD_CONST                    292: -1
        31066   BINARY_SUBSCR                 
        31068   CALL_FUNCTION                 1
        31070   LOAD_GLOBAL                   294: hedge_buy_price
        31074   COMPARE_OP                    5 (>=)
        31076   POP_JUMP_IF_FALSE             15557 (to 31114)
        31080   LOAD_GLOBAL                   74: cfg
        31082   LOAD_GLOBAL                   162: Trade_Nifty
        31084   COMPARE_OP                    5 (>=)
        31086   POP_JUMP_IF_FALSE             15557 (to 31114)
        31090   LOAD_CONST                    423: ' Queen Stoploss triggered : Max order_limit_per_day Reached. Exiting trade for the day '
        31094   STORE_NAME                    65: strMsg
        31096   LOAD_NAME                     59: iLog
        31098   LOAD_NAME                     65: strMsg
        31100   LOAD_CONST                    42: 4
        31102   LOAD_CONST                    20: True
        31104   LOAD_CONST                    43: ('sendTeleMsg',)
        31106   CALL_FUNCTION_KW              3
        31108   POP_TOP                       
        31110   LOAD_CONST                    29: 1
        31112   STORE_GLOBAL                  80: ExitTradenow
        31114   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        31118   LOAD_CONST                    292: -1
        31122   COMPARE_OP                    2 (==)
        31124   POP_JUMP_IF_FALSE             15625 (to 31250)
        31128   LOAD_GLOBAL                   172: time_offset_sec
        31130   LOAD_CONST                    20: True
        31132   COMPARE_OP                    2 (==)
        31134   POP_JUMP_IF_FALSE             15625 (to 31250)
        31138   LOAD_NAME                     44: int
        31140   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31142   LOAD_CONST                    292: -1
        31146   BINARY_SUBSCR                 
        31148   CALL_FUNCTION                 1
        31150   LOAD_GLOBAL                   286: max_entry_time_exit
        31154   COMPARE_OP                    4 (>)
        31156   POP_JUMP_IF_TRUE              15608 (to 31216)
        31160   LOAD_GLOBAL                   126: getAccessToken
        31162   LOAD_CONST                    29: 1
        31164   COMPARE_OP                    2 (==)
        31166   POP_JUMP_IF_FALSE             15592 (to 31184)
        31170   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        31174   LOAD_GLOBAL                   294: hedge_buy_price
        31178   COMPARE_OP                    5 (>=)
        31180   POP_JUMP_IF_TRUE              15608 (to 31216)
        31184   LOAD_GLOBAL                   126: getAccessToken
        31186   LOAD_CONST                    29: 1
        31188   COMPARE_OP                    3 (!=)
        31190   POP_JUMP_IF_FALSE             15625 (to 31250)
        31194   LOAD_NAME                     44: int
        31196   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31198   LOAD_CONST                    292: -1
        31202   BINARY_SUBSCR                 
        31204   CALL_FUNCTION                 1
        31206   LOAD_GLOBAL                   294: hedge_buy_price
        31210   COMPARE_OP                    5 (>=)
        31212   POP_JUMP_IF_FALSE             15625 (to 31250)
        31216   LOAD_GLOBAL                   76: read
        31218   LOAD_GLOBAL                   90: Send_Telegram
        31220   COMPARE_OP                    5 (>=)
        31222   POP_JUMP_IF_FALSE             15625 (to 31250)
        31226   LOAD_CONST                    424: ' Queen Stoploss triggered : Position change after MaxPositionChangeTime. Exiting trade for the day '
        31230   STORE_NAME                    65: strMsg
        31232   LOAD_NAME                     59: iLog
        31234   LOAD_NAME                     65: strMsg
        31236   LOAD_CONST                    42: 4
        31238   LOAD_CONST                    20: True
        31240   LOAD_CONST                    43: ('sendTeleMsg',)
        31242   CALL_FUNCTION_KW              3
        31244   POP_TOP                       
        31246   LOAD_CONST                    29: 1
        31248   STORE_GLOBAL                  80: ExitTradenow
        31250   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        31254   LOAD_CONST                    292: -1
        31258   COMPARE_OP                    2 (==)
        31260   POP_JUMP_IF_FALSE             16634 (to 33268)
        31264   LOAD_GLOBAL                   172: time_offset_sec
        31266   LOAD_CONST                    20: True
        31268   COMPARE_OP                    2 (==)
        31270   POP_JUMP_IF_FALSE             16634 (to 33268)
        31274   LOAD_NAME                     44: int
        31276   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31278   LOAD_CONST                    292: -1
        31282   BINARY_SUBSCR                 
        31284   CALL_FUNCTION                 1
        31286   LOAD_GLOBAL                   286: max_entry_time_exit
        31290   COMPARE_OP                    4 (>)
        31292   POP_JUMP_IF_TRUE              15676 (to 31352)
        31296   LOAD_GLOBAL                   126: getAccessToken
        31298   LOAD_CONST                    29: 1
        31300   COMPARE_OP                    2 (==)
        31302   POP_JUMP_IF_FALSE             15660 (to 31320)
        31306   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        31310   LOAD_GLOBAL                   294: hedge_buy_price
        31314   COMPARE_OP                    5 (>=)
        31316   POP_JUMP_IF_TRUE              15676 (to 31352)
        31320   LOAD_GLOBAL                   126: getAccessToken
        31322   LOAD_CONST                    29: 1
        31324   COMPARE_OP                    3 (!=)
        31326   POP_JUMP_IF_FALSE             16634 (to 33268)
        31330   LOAD_NAME                     44: int
        31332   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31334   LOAD_CONST                    292: -1
        31338   BINARY_SUBSCR                 
        31340   CALL_FUNCTION                 1
        31342   LOAD_GLOBAL                   294: hedge_buy_price
        31346   COMPARE_OP                    5 (>=)
        31348   POP_JUMP_IF_FALSE             16634 (to 33268)
        31352   LOAD_GLOBAL                   76: read
        31354   LOAD_GLOBAL                   90: Send_Telegram
        31356   COMPARE_OP                    0 (<)
        31358   POP_JUMP_IF_FALSE             16634 (to 33268)
        31362   LOAD_GLOBAL                   74: cfg
        31364   LOAD_GLOBAL                   162: Trade_Nifty
        31366   COMPARE_OP                    0 (<)
        31368   POP_JUMP_IF_FALSE             16634 (to 33268)
        31372   LOAD_NAME                     44: int
        31374   LOAD_NAME                     91: float
        31376   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31378   LOAD_CONST                    292: -1
        31382   BINARY_SUBSCR                 
        31384   CALL_FUNCTION                 1
        31386   CALL_FUNCTION                 1
        31388   LOAD_GLOBAL                   286: max_entry_time_exit
        31392   COMPARE_OP                    4 (>)
        31394   POP_JUMP_IF_FALSE             15731 (to 31462)
        31398   LOAD_CONST                    425: ' Queen Candle SL Hit LTP = '
        31402   LOAD_NAME                     44: int
        31404   LOAD_NAME                     91: float
        31406   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31408   LOAD_CONST                    292: -1
        31412   BINARY_SUBSCR                 
        31414   CALL_FUNCTION                 1
        31416   CALL_FUNCTION                 1
        31418   FORMAT_VALUE                  0
        31420   LOAD_CONST                    426: ', higher than Queen SL= '
        31424   LOAD_NAME                     374: round
        31428   LOAD_GLOBAL                   286: max_entry_time_exit
        31432   LOAD_CONST                    29: 1
        31434   CALL_FUNCTION                 2
        31436   FORMAT_VALUE                  0
        31438   LOAD_CONST                    407: ' '
        31442   BUILD_STRING                  5
        31444   STORE_NAME                    65: strMsg
        31446   LOAD_NAME                     59: iLog
        31448   LOAD_NAME                     65: strMsg
        31450   LOAD_CONST                    52: 2
        31452   LOAD_CONST                    20: True
        31454   LOAD_CONST                    43: ('sendTeleMsg',)
        31456   CALL_FUNCTION_KW              3
        31458   POP_TOP                       
        31460   JUMP_FORWARD                  64 (to 31590)
        31462   LOAD_GLOBAL                   126: getAccessToken
        31464   LOAD_CONST                    29: 1
        31466   COMPARE_OP                    2 (==)
        31468   POP_JUMP_IF_FALSE             15764 (to 31528)
        31472   LOAD_CONST                    427: ' Queen Candle SuperTrend SL Hit Candle Close = '
        31476   LOAD_NAME                     44: int
        31478   LOAD_GLOBAL                   295: NULL + hedge_buy_price
        31482   CALL_FUNCTION                 1
        31484   FORMAT_VALUE                  0
        31486   LOAD_CONST                    428: ', higher than Queen SuperTrend SL= '
        31490   LOAD_NAME                     374: round
        31494   LOAD_GLOBAL                   294: hedge_buy_price
        31498   LOAD_CONST                    29: 1
        31500   CALL_FUNCTION                 2
        31502   FORMAT_VALUE                  0
        31504   LOAD_CONST                    407: ' '
        31508   BUILD_STRING                  5
        31510   STORE_NAME                    65: strMsg
        31512   LOAD_NAME                     59: iLog
        31514   LOAD_NAME                     65: strMsg
        31516   LOAD_CONST                    52: 2
        31518   LOAD_CONST                    20: True
        31520   LOAD_CONST                    43: ('sendTeleMsg',)
        31522   CALL_FUNCTION_KW              3
        31524   POP_TOP                       
        31526   JUMP_FORWARD                  31 (to 31590)
        31528   LOAD_CONST                    429: ' Queen Candle SuperTrend SL LTP = '
        31532   LOAD_NAME                     44: int
        31534   LOAD_NAME                     91: float
        31536   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        31538   LOAD_CONST                    292: -1
        31542   BINARY_SUBSCR                 
        31544   CALL_FUNCTION                 1
        31546   CALL_FUNCTION                 1
        31548   FORMAT_VALUE                  0
        31550   LOAD_CONST                    428: ', higher than Queen SuperTrend SL= '
        31554   LOAD_NAME                     374: round
        31558   LOAD_GLOBAL                   294: hedge_buy_price
        31562   LOAD_CONST                    29: 1
        31564   CALL_FUNCTION                 2
        31566   FORMAT_VALUE                  0
        31568   LOAD_CONST                    407: ' '
        31572   BUILD_STRING                  5
        31574   STORE_NAME                    65: strMsg
        31576   LOAD_NAME                     59: iLog
        31578   LOAD_NAME                     65: strMsg
        31580   LOAD_CONST                    52: 2
        31582   LOAD_CONST                    20: True
        31584   LOAD_CONST                    43: ('sendTeleMsg',)
        31586   CALL_FUNCTION_KW              3
        31588   POP_TOP                       
        31590   LOAD_GLOBAL                   78: get
        31592   LOAD_CONST                    29: 1
        31594   COMPARE_OP                    2 (==)
        31596   POP_JUMP_IF_FALSE             16045 (to 32090)
        31600   LOAD_GLOBAL                   247: NULL + ADX_Period
        31602   LOAD_CONST                    29: 1
        31604   COMPARE_OP                    2 (==)
        31606   POP_JUMP_IF_FALSE             15890 (to 31780)
        31610   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        31614   STORE_GLOBAL                  221: Last_Traded_PE_Price
        31616   LOAD_CONST                    430: '  Place Sell order for Closing Existing '
        31620   LOAD_GLOBAL                   382: df_cols
        31624   FORMAT_VALUE                  0
        31626   LOAD_CONST                    363: ' PE at '
        31630   LOAD_GLOBAL                   221: NULL + strike_offset
        31632   FORMAT_VALUE                  0
        31634   BUILD_STRING                  4
        31636   STORE_NAME                    65: strMsg
        31638   LOAD_NAME                     59: iLog
        31640   LOAD_NAME                     65: strMsg
        31642   LOAD_CONST                    288: 5
        31646   LOAD_CONST                    20: True
        31648   LOAD_CONST                    43: ('sendTeleMsg',)
        31650   CALL_FUNCTION_KW              3
        31652   POP_TOP                       
        31654   LOAD_GLOBAL                   74: cfg
        31656   LOAD_CONST                    29: 1
        31658   BINARY_ADD                    
        31660   STORE_GLOBAL                  74: order_count
        31662   LOAD_GLOBAL                   76: read
        31664   LOAD_NAME                     376: Symbol
        31668   LOAD_GLOBAL                   382: df_cols
        31672   LOAD_CONST                    316: 'PE'
        31676   LOAD_CONST                    292: -1
        31680   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        31684   LOAD_GLOBAL                   221: NULL + strike_offset
        31686   LOAD_CONST                    29: 1
        31688   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        31692   BINARY_MULTIPLY               
        31694   LOAD_GLOBAL                   221: NULL + strike_offset
        31696   BINARY_MULTIPLY               
        31698   BUILD_LIST                    8
        31700   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        31702   LOAD_ATTR                     379: loc
        31706   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        31708   LOAD_NAME                     191: df_cols
        31710   BUILD_TUPLE                   2
        31712   STORE_SUBSCR                  
        31714   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        31716   LOAD_CONST                    29: 1
        31718   BINARY_ADD                    
        31720   STORE_GLOBAL                  190: df_king_cnt
        31722   LOAD_GLOBAL                   76: read
        31724   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        31728   LOAD_CONST                    0: 0
        31730   BINARY_SUBSCR                 
        31732   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        31736   LOAD_CONST                    29: 1
        31738   BINARY_SUBSCR                 
        31740   LOAD_CONST                    0: 0
        31742   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        31746   BINARY_MULTIPLY               
        31748   BUILD_LIST                    4
        31750   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        31752   LOAD_ATTR                     379: loc
        31756   LOAD_CONST                    0: 0
        31758   LOAD_NAME                     197: leg_cols
        31760   BUILD_TUPLE                   2
        31762   STORE_SUBSCR                  
        31764   LOAD_NAME                     24: pd
        31766   LOAD_METHOD                   380: concat
        31770   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        31772   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        31774   BUILD_LIST                    2
        31776   CALL_METHOD                   1
        31778   STORE_GLOBAL                  200: Current_legs
        31780   SETUP_FINALLY                 8 (to 31798)
        31782   LOAD_NAME                     331: get_option_tokens
        31786   LOAD_CONST                    316: 'PE'
        31790   CALL_FUNCTION                 1
        31792   POP_TOP                       
        31794   POP_BLOCK                     
        31796   JUMP_FORWARD                  60 (to 31918)
        31798   POP_TOP                       
        31800   POP_TOP                       
        31802   POP_TOP                       
        31804   LOAD_NAME                     2: time
        31806   LOAD_METHOD                   355: sleep
        31810   LOAD_CONST                    288: 5
        31814   CALL_METHOD                   1
        31816   POP_TOP                       
        31818   SETUP_FINALLY                 8 (to 31836)
        31820   LOAD_NAME                     331: get_option_tokens
        31824   LOAD_CONST                    316: 'PE'
        31828   CALL_FUNCTION                 1
        31830   POP_TOP                       
        31832   POP_BLOCK                     
        31834   JUMP_FORWARD                  40 (to 31916)
        31836   DUP_TOP                       
        31838   LOAD_NAME                     357: Exception
        31842   JUMP_IF_NOT_EXC_MATCH         15957 (to 31914)
        31846   POP_TOP                       
        31848   STORE_NAME                    358: ex
        31852   POP_TOP                       
        31854   SETUP_FINALLY                 23 (to 31902)
        31856   LOAD_NAME                     59: iLog
        31858   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        31862   LOAD_NAME                     343: str
        31866   LOAD_NAME                     358: ex
        31870   CALL_FUNCTION                 1
        31872   BINARY_ADD                    
        31874   LOAD_CONST                    271: 3
        31878   LOAD_CONST                    20: True
        31880   LOAD_CONST                    43: ('sendTeleMsg',)
        31882   CALL_FUNCTION_KW              3
        31884   POP_TOP                       
        31886   POP_BLOCK                     
        31888   POP_EXCEPT                    
        31890   LOAD_CONST                    1: None
        31892   STORE_NAME                    358: ex
        31896   DELETE_NAME                   358: ex
        31900   JUMP_FORWARD                  7 (to 31916)
        31902   LOAD_CONST                    1: None
        31904   STORE_NAME                    358: ex
        31908   DELETE_NAME                   358: ex
        31912   RERAISE                       1
        31914   RERAISE                       0
        31916   POP_EXCEPT                    
        31918   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        31922   STORE_GLOBAL                  221: Last_Traded_PE_Price
        31924   LOAD_CONST                    351: '  Place SELL order for new  '
        31928   LOAD_GLOBAL                   382: df_cols
        31932   FORMAT_VALUE                  0
        31934   LOAD_CONST                    363: ' PE at '
        31938   LOAD_GLOBAL                   221: NULL + strike_offset
        31940   FORMAT_VALUE                  0
        31942   BUILD_STRING                  4
        31944   STORE_NAME                    65: strMsg
        31946   LOAD_NAME                     59: iLog
        31948   LOAD_NAME                     65: strMsg
        31950   LOAD_CONST                    288: 5
        31954   LOAD_CONST                    20: True
        31956   LOAD_CONST                    43: ('sendTeleMsg',)
        31958   CALL_FUNCTION_KW              3
        31960   POP_TOP                       
        31962   LOAD_GLOBAL                   74: cfg
        31964   LOAD_CONST                    29: 1
        31966   BINARY_ADD                    
        31968   STORE_GLOBAL                  74: order_count
        31970   LOAD_GLOBAL                   76: read
        31972   LOAD_NAME                     376: Symbol
        31976   LOAD_GLOBAL                   382: df_cols
        31980   LOAD_CONST                    316: 'PE'
        31984   LOAD_CONST                    292: -1
        31988   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        31992   LOAD_GLOBAL                   221: NULL + strike_offset
        31994   LOAD_CONST                    29: 1
        31996   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32000   BINARY_MULTIPLY               
        32002   LOAD_GLOBAL                   221: NULL + strike_offset
        32004   BINARY_MULTIPLY               
        32006   BUILD_LIST                    8
        32008   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        32010   LOAD_ATTR                     379: loc
        32014   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        32016   LOAD_NAME                     191: df_cols
        32018   BUILD_TUPLE                   2
        32020   STORE_SUBSCR                  
        32022   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        32024   LOAD_CONST                    29: 1
        32026   BINARY_ADD                    
        32028   STORE_GLOBAL                  190: df_king_cnt
        32030   LOAD_GLOBAL                   76: read
        32032   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        32036   LOAD_CONST                    0: 0
        32038   BINARY_SUBSCR                 
        32040   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        32044   LOAD_CONST                    29: 1
        32046   BINARY_SUBSCR                 
        32048   LOAD_CONST                    292: -1
        32052   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32056   BINARY_MULTIPLY               
        32058   BUILD_LIST                    4
        32060   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        32062   LOAD_ATTR                     379: loc
        32066   LOAD_CONST                    0: 0
        32068   LOAD_NAME                     197: leg_cols
        32070   BUILD_TUPLE                   2
        32072   STORE_SUBSCR                  
        32074   LOAD_NAME                     24: pd
        32076   LOAD_METHOD                   380: concat
        32080   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        32082   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        32084   BUILD_LIST                    2
        32086   CALL_METHOD                   1
        32088   STORE_GLOBAL                  200: Current_legs
        32090   LOAD_GLOBAL                   78: get
        32092   LOAD_CONST                    0: 0
        32094   COMPARE_OP                    2 (==)
        32096   POP_JUMP_IF_FALSE             16623 (to 33246)
        32100   LOAD_GLOBAL                   247: NULL + ADX_Period
        32102   LOAD_CONST                    29: 1
        32104   COMPARE_OP                    2 (==)
        32106   POP_JUMP_IF_FALSE             16304 (to 32608)
        32110   LOAD_NAME                     308: place_order
        32114   LOAD_CONST                    337: 'S'
        32118   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        32122   LOAD_CONST                    52: 2
        32124   BINARY_SUBSCR                 
        32126   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32130   CALL_FUNCTION                 3
        32132   STORE_GLOBAL                  389: order_id_PE
        32136   LOAD_GLOBAL                   74: cfg
        32138   LOAD_CONST                    29: 1
        32140   BINARY_ADD                    
        32142   STORE_GLOBAL                  74: order_count
        32144   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        32148   STORE_GLOBAL                  221: Last_Traded_PE_Price
        32150   LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        32154   LOAD_CONST                    319: 'norenordno'
        32158   BINARY_SUBSCR                 
        32160   STORE_NAME                    384: order_id
        32164   LOAD_NAME                     311: get_order_symbol
        32168   LOAD_NAME                     384: order_id
        32172   CALL_FUNCTION                 1
        32174   STORE_NAME                    376: Symbol
        32178   LOAD_GLOBAL                   389: NULL + df_runtime_cnt
        32182   LOAD_CONST                    320: 'stat'
        32186   BINARY_SUBSCR                 
        32188   STORE_NAME                    385: Placed_Status
        32192   LOAD_NAME                     309: get_order_status
        32196   LOAD_NAME                     384: order_id
        32200   CALL_FUNCTION                 1
        32202   STORE_NAME                    386: Return_Status
        32206   LOAD_NAME                     310: get_order_price
        32210   LOAD_NAME                     384: order_id
        32214   CALL_FUNCTION                 1
        32216   STORE_NAME                    387: average_price
        32220   LOAD_NAME                     386: Return_Status
        32224   LOAD_METHOD                   352: upper
        32228   CALL_METHOD                   0
        32230   LOAD_CONST                    321: 'REJECTED'
        32234   COMPARE_OP                    2 (==)
        32236   POP_JUMP_IF_FALSE             16166 (to 32332)
        32240   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        32244   LOAD_NAME                     384: order_id
        32248   FORMAT_VALUE                  0
        32250   LOAD_CONST                    323: ', Ord_STS = '
        32254   LOAD_NAME                     385: Placed_Status
        32258   FORMAT_VALUE                  0
        32260   LOAD_CONST                    324: ', Ret_STS = '
        32264   LOAD_NAME                     386: Return_Status
        32268   FORMAT_VALUE                  0
        32270   LOAD_CONST                    333: '.'
        32274   BUILD_STRING                  7
        32276   STORE_NAME                    65: strMsg
        32278   LOAD_NAME                     59: iLog
        32280   LOAD_NAME                     65: strMsg
        32282   LOAD_CONST                    288: 5
        32286   LOAD_CONST                    20: True
        32288   LOAD_CONST                    43: ('sendTeleMsg',)
        32290   CALL_FUNCTION_KW              3
        32292   POP_TOP                       
        32294   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        32298   STORE_NAME                    65: strMsg
        32300   LOAD_NAME                     59: iLog
        32302   LOAD_NAME                     65: strMsg
        32304   LOAD_CONST                    42: 4
        32306   LOAD_CONST                    20: True
        32308   LOAD_CONST                    43: ('sendTeleMsg',)
        32310   CALL_FUNCTION_KW              3
        32312   POP_TOP                       
        32314   LOAD_NAME                     322: close_all_orders
        32318   CALL_FUNCTION                 0
        32320   POP_TOP                       
        32322   LOAD_NAME                     0: sys
        32324   LOAD_METHOD                   344: exit
        32328   CALL_METHOD                   0
        32330   POP_TOP                       
        32332   LOAD_NAME                     387: average_price
        32336   LOAD_CONST                    0: 0
        32338   COMPARE_OP                    4 (>)
        32340   POP_JUMP_IF_FALSE             16185 (to 32370)
        32344   LOAD_NAME                     386: Return_Status
        32348   LOAD_METHOD                   352: upper
        32352   CALL_METHOD                   0
        32354   LOAD_CONST                    327: 'COMPLETE'
        32358   COMPARE_OP                    2 (==)
        32360   POP_JUMP_IF_FALSE             16185 (to 32370)
        32364   LOAD_NAME                     387: average_price
        32368   STORE_GLOBAL                  221: Last_Traded_PE_Price
        32370   LOAD_GLOBAL                   76: read
        32372   LOAD_NAME                     376: Symbol
        32376   LOAD_GLOBAL                   382: df_cols
        32380   LOAD_CONST                    316: 'PE'
        32384   LOAD_CONST                    292: -1
        32388   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32392   LOAD_GLOBAL                   221: NULL + strike_offset
        32394   LOAD_CONST                    29: 1
        32396   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32400   BINARY_MULTIPLY               
        32402   LOAD_GLOBAL                   221: NULL + strike_offset
        32404   BINARY_MULTIPLY               
        32406   BUILD_LIST                    8
        32408   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        32410   LOAD_ATTR                     379: loc
        32414   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        32416   LOAD_NAME                     191: df_cols
        32418   BUILD_TUPLE                   2
        32420   STORE_SUBSCR                  
        32422   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        32424   LOAD_CONST                    29: 1
        32426   BINARY_ADD                    
        32428   STORE_GLOBAL                  190: df_king_cnt
        32430   LOAD_CONST                    20: True
        32432   STORE_GLOBAL                  170: First_Straddle
        32434   LOAD_CONST                    367: ' Placed PE Sell Market order for ATM Strike='
        32438   LOAD_GLOBAL                   382: df_cols
        32442   FORMAT_VALUE                  0
        32444   LOAD_CONST                    366: ', ATM PE='
        32448   LOAD_NAME                     387: average_price
        32452   FORMAT_VALUE                  0
        32454   LOAD_CONST                    330: ', Qty ='
        32458   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32462   FORMAT_VALUE                  0
        32464   LOAD_CONST                    331: ', Ord_ID = '
        32468   LOAD_NAME                     384: order_id
        32472   FORMAT_VALUE                  0
        32474   LOAD_CONST                    323: ', Ord_STS = '
        32478   LOAD_NAME                     385: Placed_Status
        32482   FORMAT_VALUE                  0
        32484   LOAD_CONST                    324: ', Ret_STS = '
        32488   LOAD_NAME                     386: Return_Status
        32492   FORMAT_VALUE                  0
        32494   BUILD_STRING                  12
        32496   STORE_NAME                    65: strMsg
        32498   LOAD_NAME                     59: iLog
        32500   LOAD_NAME                     65: strMsg
        32502   LOAD_CONST                    288: 5
        32506   LOAD_CONST                    20: True
        32508   LOAD_CONST                    43: ('sendTeleMsg',)
        32510   CALL_FUNCTION_KW              3
        32512   POP_TOP                       
        32514   LOAD_NAME                     72: tl
        32516   LOAD_METHOD                   388: update_csv
        32520   LOAD_NAME                     376: Symbol
        32524   LOAD_CONST                    339: 'Sell'
        32528   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32532   LOAD_GLOBAL                   221: NULL + strike_offset
        32534   LOAD_NAME                     384: order_id
        32538   LOAD_NAME                     385: Placed_Status
        32542   LOAD_NAME                     386: Return_Status
        32546   CALL_METHOD                   7
        32548   POP_TOP                       
        32550   LOAD_GLOBAL                   76: read
        32552   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        32556   LOAD_CONST                    0: 0
        32558   BINARY_SUBSCR                 
        32560   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        32564   LOAD_CONST                    29: 1
        32566   BINARY_SUBSCR                 
        32568   LOAD_CONST                    0: 0
        32570   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32574   BINARY_MULTIPLY               
        32576   BUILD_LIST                    4
        32578   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        32580   LOAD_ATTR                     379: loc
        32584   LOAD_CONST                    0: 0
        32586   LOAD_NAME                     197: leg_cols
        32588   BUILD_TUPLE                   2
        32590   STORE_SUBSCR                  
        32592   LOAD_NAME                     24: pd
        32594   LOAD_METHOD                   380: concat
        32598   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        32600   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        32602   BUILD_LIST                    2
        32604   CALL_METHOD                   1
        32606   STORE_GLOBAL                  200: Current_legs
        32608   SETUP_FINALLY                 8 (to 32626)
        32610   LOAD_NAME                     331: get_option_tokens
        32614   LOAD_CONST                    316: 'PE'
        32618   CALL_FUNCTION                 1
        32620   POP_TOP                       
        32622   POP_BLOCK                     
        32624   JUMP_FORWARD                  60 (to 32746)
        32626   POP_TOP                       
        32628   POP_TOP                       
        32630   POP_TOP                       
        32632   LOAD_NAME                     2: time
        32634   LOAD_METHOD                   355: sleep
        32638   LOAD_CONST                    288: 5
        32642   CALL_METHOD                   1
        32644   POP_TOP                       
        32646   SETUP_FINALLY                 8 (to 32664)
        32648   LOAD_NAME                     331: get_option_tokens
        32652   LOAD_CONST                    316: 'PE'
        32656   CALL_FUNCTION                 1
        32658   POP_TOP                       
        32660   POP_BLOCK                     
        32662   JUMP_FORWARD                  40 (to 32744)
        32664   DUP_TOP                       
        32666   LOAD_NAME                     357: Exception
        32670   JUMP_IF_NOT_EXC_MATCH         16371 (to 32742)
        32674   POP_TOP                       
        32676   STORE_NAME                    358: ex
        32680   POP_TOP                       
        32682   SETUP_FINALLY                 23 (to 32730)
        32684   LOAD_NAME                     59: iLog
        32686   LOAD_CONST                    289: ' get_option_tokens(): Exception='
        32690   LOAD_NAME                     343: str
        32694   LOAD_NAME                     358: ex
        32698   CALL_FUNCTION                 1
        32700   BINARY_ADD                    
        32702   LOAD_CONST                    271: 3
        32706   LOAD_CONST                    20: True
        32708   LOAD_CONST                    43: ('sendTeleMsg',)
        32710   CALL_FUNCTION_KW              3
        32712   POP_TOP                       
        32714   POP_BLOCK                     
        32716   POP_EXCEPT                    
        32718   LOAD_CONST                    1: None
        32720   STORE_NAME                    358: ex
        32724   DELETE_NAME                   358: ex
        32728   JUMP_FORWARD                  7 (to 32744)
        32730   LOAD_CONST                    1: None
        32732   STORE_NAME                    358: ex
        32736   DELETE_NAME                   358: ex
        32740   RERAISE                       1
        32742   RERAISE                       0
        32744   POP_EXCEPT                    
        32746   LOAD_NAME                     308: place_order
        32750   LOAD_CONST                    337: 'S'
        32754   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        32758   LOAD_CONST                    52: 2
        32760   BINARY_SUBSCR                 
        32762   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        32766   CALL_FUNCTION                 3
        32768   STORE_NAME                    395: order_id_PE1
        32772   LOAD_GLOBAL                   74: cfg
        32774   LOAD_CONST                    29: 1
        32776   BINARY_ADD                    
        32778   STORE_GLOBAL                  74: order_count
        32780   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        32784   STORE_GLOBAL                  221: Last_Traded_PE_Price
        32786   LOAD_NAME                     395: order_id_PE1
        32790   LOAD_CONST                    319: 'norenordno'
        32794   BINARY_SUBSCR                 
        32796   STORE_NAME                    384: order_id
        32800   LOAD_NAME                     311: get_order_symbol
        32804   LOAD_NAME                     384: order_id
        32808   CALL_FUNCTION                 1
        32810   STORE_NAME                    376: Symbol
        32814   LOAD_NAME                     395: order_id_PE1
        32818   LOAD_CONST                    320: 'stat'
        32822   BINARY_SUBSCR                 
        32824   STORE_NAME                    385: Placed_Status
        32828   LOAD_NAME                     309: get_order_status
        32832   LOAD_NAME                     384: order_id
        32836   CALL_FUNCTION                 1
        32838   STORE_NAME                    386: Return_Status
        32842   LOAD_NAME                     310: get_order_price
        32846   LOAD_NAME                     384: order_id
        32850   CALL_FUNCTION                 1
        32852   STORE_NAME                    387: average_price
        32856   LOAD_NAME                     386: Return_Status
        32860   LOAD_METHOD                   352: upper
        32864   CALL_METHOD                   0
        32866   LOAD_CONST                    321: 'REJECTED'
        32870   COMPARE_OP                    2 (==)
        32872   POP_JUMP_IF_FALSE             16484 (to 32968)
        32876   LOAD_CONST                    322: ' Error in Order Placement Ord_ID = '
        32880   LOAD_NAME                     384: order_id
        32884   FORMAT_VALUE                  0
        32886   LOAD_CONST                    323: ', Ord_STS = '
        32890   LOAD_NAME                     385: Placed_Status
        32894   FORMAT_VALUE                  0
        32896   LOAD_CONST                    324: ', Ret_STS = '
        32900   LOAD_NAME                     386: Return_Status
        32904   FORMAT_VALUE                  0
        32906   LOAD_CONST                    333: '.'
        32910   BUILD_STRING                  7
        32912   STORE_NAME                    65: strMsg
        32914   LOAD_NAME                     59: iLog
        32916   LOAD_NAME                     65: strMsg
        32918   LOAD_CONST                    288: 5
        32922   LOAD_CONST                    20: True
        32924   LOAD_CONST                    43: ('sendTeleMsg',)
        32926   CALL_FUNCTION_KW              3
        32928   POP_TOP                       
        32930   LOAD_CONST                    334: ' Closing Open Positions and Exiting Algo.Cross Check for any Open positions'
        32934   STORE_NAME                    65: strMsg
        32936   LOAD_NAME                     59: iLog
        32938   LOAD_NAME                     65: strMsg
        32940   LOAD_CONST                    42: 4
        32942   LOAD_CONST                    20: True
        32944   LOAD_CONST                    43: ('sendTeleMsg',)
        32946   CALL_FUNCTION_KW              3
        32948   POP_TOP                       
        32950   LOAD_NAME                     322: close_all_orders
        32954   CALL_FUNCTION                 0
        32956   POP_TOP                       
        32958   LOAD_NAME                     0: sys
        32960   LOAD_METHOD                   344: exit
        32964   CALL_METHOD                   0
        32966   POP_TOP                       
        32968   LOAD_NAME                     387: average_price
        32972   LOAD_CONST                    0: 0
        32974   COMPARE_OP                    4 (>)
        32976   POP_JUMP_IF_FALSE             16503 (to 33006)
        32980   LOAD_NAME                     386: Return_Status
        32984   LOAD_METHOD                   352: upper
        32988   CALL_METHOD                   0
        32990   LOAD_CONST                    327: 'COMPLETE'
        32994   COMPARE_OP                    2 (==)
        32996   POP_JUMP_IF_FALSE             16503 (to 33006)
        33000   LOAD_NAME                     387: average_price
        33004   STORE_GLOBAL                  221: Last_Traded_PE_Price
        33006   LOAD_GLOBAL                   76: read
        33008   LOAD_NAME                     376: Symbol
        33012   LOAD_GLOBAL                   382: df_cols
        33016   LOAD_CONST                    316: 'PE'
        33020   LOAD_CONST                    292: -1
        33024   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        33028   LOAD_GLOBAL                   221: NULL + strike_offset
        33030   LOAD_CONST                    29: 1
        33032   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        33036   BINARY_MULTIPLY               
        33038   LOAD_GLOBAL                   221: NULL + strike_offset
        33040   BINARY_MULTIPLY               
        33042   BUILD_LIST                    8
        33044   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        33046   LOAD_ATTR                     379: loc
        33050   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        33052   LOAD_NAME                     191: df_cols
        33054   BUILD_TUPLE                   2
        33056   STORE_SUBSCR                  
        33058   LOAD_GLOBAL                   190: expiry_Perlot_MTM_Target
        33060   LOAD_CONST                    29: 1
        33062   BINARY_ADD                    
        33064   STORE_GLOBAL                  190: df_king_cnt
        33066   LOAD_CONST                    20: True
        33068   STORE_GLOBAL                  170: First_Straddle
        33070   LOAD_CONST                    367: ' Placed PE Sell Market order for ATM Strike='
        33074   LOAD_GLOBAL                   382: df_cols
        33078   FORMAT_VALUE                  0
        33080   LOAD_CONST                    366: ', ATM PE='
        33084   LOAD_NAME                     387: average_price
        33088   FORMAT_VALUE                  0
        33090   LOAD_CONST                    330: ', Qty ='
        33094   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        33098   FORMAT_VALUE                  0
        33100   LOAD_CONST                    331: ', Ord_ID = '
        33104   LOAD_NAME                     384: order_id
        33108   FORMAT_VALUE                  0
        33110   LOAD_CONST                    323: ', Ord_STS = '
        33114   LOAD_NAME                     385: Placed_Status
        33118   FORMAT_VALUE                  0
        33120   LOAD_CONST                    324: ', Ret_STS = '
        33124   LOAD_NAME                     386: Return_Status
        33128   FORMAT_VALUE                  0
        33130   BUILD_STRING                  12
        33132   STORE_NAME                    65: strMsg
        33134   LOAD_NAME                     59: iLog
        33136   LOAD_NAME                     65: strMsg
        33138   LOAD_CONST                    288: 5
        33142   LOAD_CONST                    20: True
        33144   LOAD_CONST                    43: ('sendTeleMsg',)
        33146   CALL_FUNCTION_KW              3
        33148   POP_TOP                       
        33150   LOAD_NAME                     72: tl
        33152   LOAD_METHOD                   388: update_csv
        33156   LOAD_NAME                     376: Symbol
        33160   LOAD_CONST                    339: 'Sell'
        33164   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        33168   LOAD_GLOBAL                   221: NULL + strike_offset
        33170   LOAD_NAME                     384: order_id
        33174   LOAD_NAME                     385: Placed_Status
        33178   LOAD_NAME                     386: Return_Status
        33182   CALL_METHOD                   7
        33184   POP_TOP                       
        33186   LOAD_GLOBAL                   76: read
        33188   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        33192   LOAD_CONST                    0: 0
        33194   BINARY_SUBSCR                 
        33196   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        33200   LOAD_CONST                    29: 1
        33202   BINARY_SUBSCR                 
        33204   LOAD_CONST                    292: -1
        33208   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        33212   BINARY_MULTIPLY               
        33214   BUILD_LIST                    4
        33216   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        33218   LOAD_ATTR                     379: loc
        33222   LOAD_CONST                    0: 0
        33224   LOAD_NAME                     197: leg_cols
        33226   BUILD_TUPLE                   2
        33228   STORE_SUBSCR                  
        33230   LOAD_NAME                     24: pd
        33232   LOAD_METHOD                   380: concat
        33236   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        33238   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        33240   BUILD_LIST                    2
        33242   CALL_METHOD                   1
        33244   STORE_GLOBAL                  200: Current_legs
        33246   LOAD_CONST                    30: False
        33248   STORE_GLOBAL                  172: Queen_Order_Placed
        33250   LOAD_CONST                    0: 0
        33252   STORE_GLOBAL                  296: K_Direction
        33256   LOAD_NAME                     297: K_Direction_Change_Count
        33260   LOAD_CONST                    29: 1
        33262   BINARY_ADD                    
        33264   STORE_NAME                    297: K_Direction_Change_Count
        33268   LOAD_GLOBAL                   200: normal_StikeAdj_SLPer
        33270   LOAD_METHOD                   400: to_csv
        33274   LOAD_CONST                    26: './log/'
        33276   LOAD_GLOBAL                   46: pandas
        33278   BINARY_ADD                    
        33280   LOAD_CONST                    375: '_Current_legs.txt'
        33284   BINARY_ADD                    
        33286   CALL_METHOD                   1
        33288   POP_TOP                       
        33290   LOAD_GLOBAL                   144: tl
        33292   LOAD_CONST                    29: 1
        33294   COMPARE_OP                    2 (==)
        33296   POP_JUMP_IF_FALSE             16661 (to 33322)
        33300   LOAD_GLOBAL                   203: NULL + normal_StikeAdj_TgtPer
        33302   LOAD_METHOD                   400: to_csv
        33306   LOAD_CONST                    26: './log/'
        33308   LOAD_GLOBAL                   46: pandas
        33310   BINARY_ADD                    
        33312   LOAD_CONST                    376: '_Current_legs_hedge.txt'
        33316   BINARY_ADD                    
        33318   CALL_METHOD                   1
        33320   POP_TOP                       
        33322   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        33324   LOAD_CONST                    341: 'NQ'
        33328   BINARY_SUBSCR                 
        33330   LOAD_METHOD                   390: sum
        33334   CALL_METHOD                   0
        33336   LOAD_CONST                    0: 0
        33338   COMPARE_OP                    3 (!=)
        33340   POP_JUMP_IF_FALSE             16889 (to 33778)
        33344   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33348   LOAD_NAME                     185: CE_LTP_old
        33350   COMPARE_OP                    2 (==)
        33352   POP_JUMP_IF_FALSE             16683 (to 33366)
        33356   LOAD_NAME                     183: CE_LTP_Update_Count
        33358   LOAD_CONST                    29: 1
        33360   BINARY_ADD                    
        33362   STORE_NAME                    183: CE_LTP_Update_Count
        33364   JUMP_FORWARD                  2 (to 33370)
        33366   LOAD_CONST                    0: 0
        33368   STORE_NAME                    183: CE_LTP_Update_Count
        33370   LOAD_NAME                     183: CE_LTP_Update_Count
        33372   LOAD_CONST                    431: 30
        33376   COMPARE_OP                    2 (==)
        33378   POP_JUMP_IF_FALSE             16712 (to 33424)
        33382   LOAD_CONST                    407: ' '
        33386   LOAD_GLOBAL                   381: NULL + df_king_cnt
        33390   FORMAT_VALUE                  0
        33392   LOAD_CONST                    432: ' CE LTP '
        33396   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33400   FORMAT_VALUE                  0
        33402   LOAD_CONST                    433: ' not updating for 1 Mins:'
        33406   BUILD_STRING                  5
        33408   STORE_NAME                    65: strMsg
        33410   LOAD_NAME                     59: iLog
        33412   LOAD_NAME                     65: strMsg
        33414   LOAD_CONST                    42: 4
        33416   LOAD_CONST                    20: True
        33418   LOAD_CONST                    43: ('sendTeleMsg',)
        33420   CALL_FUNCTION_KW              3
        33422   POP_TOP                       
        33424   LOAD_NAME                     183: CE_LTP_Update_Count
        33426   LOAD_CONST                    434: 60
        33430   COMPARE_OP                    2 (==)
        33432   POP_JUMP_IF_FALSE             16739 (to 33478)
        33436   LOAD_CONST                    407: ' '
        33440   LOAD_GLOBAL                   381: NULL + df_king_cnt
        33444   FORMAT_VALUE                  0
        33446   LOAD_CONST                    432: ' CE LTP '
        33450   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33454   FORMAT_VALUE                  0
        33456   LOAD_CONST                    435: ' not updating for 2 Mins:'
        33460   BUILD_STRING                  5
        33462   STORE_NAME                    65: strMsg
        33464   LOAD_NAME                     59: iLog
        33466   LOAD_NAME                     65: strMsg
        33468   LOAD_CONST                    42: 4
        33470   LOAD_CONST                    20: True
        33472   LOAD_CONST                    43: ('sendTeleMsg',)
        33474   CALL_FUNCTION_KW              3
        33476   POP_TOP                       
        33478   LOAD_NAME                     183: CE_LTP_Update_Count
        33480   LOAD_CONST                    436: 90
        33484   COMPARE_OP                    2 (==)
        33486   POP_JUMP_IF_FALSE             16766 (to 33532)
        33490   LOAD_CONST                    407: ' '
        33494   LOAD_GLOBAL                   381: NULL + df_king_cnt
        33498   FORMAT_VALUE                  0
        33500   LOAD_CONST                    432: ' CE LTP '
        33504   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33508   FORMAT_VALUE                  0
        33510   LOAD_CONST                    437: ' not updating for 3 Mins:'
        33514   BUILD_STRING                  5
        33516   STORE_NAME                    65: strMsg
        33518   LOAD_NAME                     59: iLog
        33520   LOAD_NAME                     65: strMsg
        33522   LOAD_CONST                    42: 4
        33524   LOAD_CONST                    20: True
        33526   LOAD_CONST                    43: ('sendTeleMsg',)
        33528   CALL_FUNCTION_KW              3
        33530   POP_TOP                       
        33532   LOAD_NAME                     183: CE_LTP_Update_Count
        33534   LOAD_CONST                    438: 120
        33538   COMPARE_OP                    2 (==)
        33540   POP_JUMP_IF_FALSE             16793 (to 33586)
        33544   LOAD_CONST                    407: ' '
        33548   LOAD_GLOBAL                   381: NULL + df_king_cnt
        33552   FORMAT_VALUE                  0
        33554   LOAD_CONST                    432: ' CE LTP '
        33558   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33562   FORMAT_VALUE                  0
        33564   LOAD_CONST                    439: ' not updating for 4 Mins:'
        33568   BUILD_STRING                  5
        33570   STORE_NAME                    65: strMsg
        33572   LOAD_NAME                     59: iLog
        33574   LOAD_NAME                     65: strMsg
        33576   LOAD_CONST                    42: 4
        33578   LOAD_CONST                    20: True
        33580   LOAD_CONST                    43: ('sendTeleMsg',)
        33582   CALL_FUNCTION_KW              3
        33584   POP_TOP                       
        33586   LOAD_NAME                     183: CE_LTP_Update_Count
        33588   LOAD_CONST                    440: 150
        33592   COMPARE_OP                    2 (==)
        33594   POP_JUMP_IF_FALSE             16820 (to 33640)
        33598   LOAD_CONST                    407: ' '
        33602   LOAD_GLOBAL                   381: NULL + df_king_cnt
        33606   FORMAT_VALUE                  0
        33608   LOAD_CONST                    432: ' CE LTP '
        33612   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33616   FORMAT_VALUE                  0
        33618   LOAD_CONST                    441: ' not updating for more than 5 Mins: Consider exiting Algo manually'
        33622   BUILD_STRING                  5
        33624   STORE_NAME                    65: strMsg
        33626   LOAD_NAME                     59: iLog
        33628   LOAD_NAME                     65: strMsg
        33630   LOAD_CONST                    42: 4
        33632   LOAD_CONST                    20: True
        33634   LOAD_CONST                    43: ('sendTeleMsg',)
        33636   CALL_FUNCTION_KW              3
        33638   POP_TOP                       
        33640   LOAD_NAME                     183: CE_LTP_Update_Count
        33642   LOAD_CONST                    442: 300
        33646   COMPARE_OP                    2 (==)
        33648   POP_JUMP_IF_FALSE             16847 (to 33694)
        33652   LOAD_CONST                    407: ' '
        33656   LOAD_GLOBAL                   381: NULL + df_king_cnt
        33660   FORMAT_VALUE                  0
        33662   LOAD_CONST                    432: ' CE LTP '
        33666   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33670   FORMAT_VALUE                  0
        33672   LOAD_CONST                    443: ' not updating for more than 10 Mins: Consider exiting Algo manually'
        33676   BUILD_STRING                  5
        33678   STORE_NAME                    65: strMsg
        33680   LOAD_NAME                     59: iLog
        33682   LOAD_NAME                     65: strMsg
        33684   LOAD_CONST                    42: 4
        33686   LOAD_CONST                    20: True
        33688   LOAD_CONST                    43: ('sendTeleMsg',)
        33690   CALL_FUNCTION_KW              3
        33692   POP_TOP                       
        33694   LOAD_NAME                     183: CE_LTP_Update_Count
        33696   LOAD_GLOBAL                   164: Trade_BankNifty
        33698   LOAD_CONST                    52: 2
        33700   BINARY_TRUE_DIVIDE            
        33702   COMPARE_OP                    5 (>=)
        33704   POP_JUMP_IF_FALSE             16886 (to 33772)
        33708   LOAD_GLOBAL                   163: NULL + Trade_Nifty
        33710   LOAD_CONST                    29: 1
        33712   COMPARE_OP                    2 (==)
        33714   POP_JUMP_IF_FALSE             16886 (to 33772)
        33718   LOAD_CONST                    407: ' '
        33722   LOAD_GLOBAL                   381: NULL + df_king_cnt
        33726   FORMAT_VALUE                  0
        33728   LOAD_CONST                    432: ' CE LTP '
        33732   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33736   FORMAT_VALUE                  0
        33738   LOAD_CONST                    444: ' not updating for '
        33742   LOAD_GLOBAL                   164: Trade_BankNifty
        33744   FORMAT_VALUE                  0
        33746   LOAD_CONST                    445: ' Secs: ExitTradenow Triggered : closing all Trades'
        33750   BUILD_STRING                  7
        33752   STORE_NAME                    65: strMsg
        33754   LOAD_NAME                     59: iLog
        33756   LOAD_NAME                     65: strMsg
        33758   LOAD_CONST                    42: 4
        33760   LOAD_CONST                    20: True
        33762   LOAD_CONST                    43: ('sendTeleMsg',)
        33764   CALL_FUNCTION_KW              3
        33766   POP_TOP                       
        33768   LOAD_CONST                    29: 1
        33770   STORE_GLOBAL                  80: ExitTradenow
        33772   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        33776   STORE_NAME                    185: CE_LTP_old
        33778   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        33780   LOAD_CONST                    341: 'NQ'
        33784   BINARY_SUBSCR                 
        33786   LOAD_METHOD                   390: sum
        33790   CALL_METHOD                   0
        33792   LOAD_CONST                    0: 0
        33794   COMPARE_OP                    3 (!=)
        33796   POP_JUMP_IF_FALSE             17117 (to 34234)
        33800   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        33804   LOAD_NAME                     186: PE_LTP_old
        33806   COMPARE_OP                    2 (==)
        33808   POP_JUMP_IF_FALSE             16911 (to 33822)
        33812   LOAD_NAME                     184: PE_LTP_Update_Count
        33814   LOAD_CONST                    29: 1
        33816   BINARY_ADD                    
        33818   STORE_NAME                    184: PE_LTP_Update_Count
        33820   JUMP_FORWARD                  2 (to 33826)
        33822   LOAD_CONST                    0: 0
        33824   STORE_NAME                    184: PE_LTP_Update_Count
        33826   LOAD_NAME                     184: PE_LTP_Update_Count
        33828   LOAD_CONST                    431: 30
        33832   COMPARE_OP                    2 (==)
        33834   POP_JUMP_IF_FALSE             16940 (to 33880)
        33838   LOAD_CONST                    407: ' '
        33842   LOAD_GLOBAL                   382: df_cols
        33846   FORMAT_VALUE                  0
        33848   LOAD_CONST                    446: ' PE LTP '
        33852   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        33856   FORMAT_VALUE                  0
        33858   LOAD_CONST                    433: ' not updating for 1 Mins:'
        33862   BUILD_STRING                  5
        33864   STORE_NAME                    65: strMsg
        33866   LOAD_NAME                     59: iLog
        33868   LOAD_NAME                     65: strMsg
        33870   LOAD_CONST                    42: 4
        33872   LOAD_CONST                    20: True
        33874   LOAD_CONST                    43: ('sendTeleMsg',)
        33876   CALL_FUNCTION_KW              3
        33878   POP_TOP                       
        33880   LOAD_NAME                     184: PE_LTP_Update_Count
        33882   LOAD_CONST                    434: 60
        33886   COMPARE_OP                    2 (==)
        33888   POP_JUMP_IF_FALSE             16967 (to 33934)
        33892   LOAD_CONST                    407: ' '
        33896   LOAD_GLOBAL                   382: df_cols
        33900   FORMAT_VALUE                  0
        33902   LOAD_CONST                    446: ' PE LTP '
        33906   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        33910   FORMAT_VALUE                  0
        33912   LOAD_CONST                    435: ' not updating for 2 Mins:'
        33916   BUILD_STRING                  5
        33918   STORE_NAME                    65: strMsg
        33920   LOAD_NAME                     59: iLog
        33922   LOAD_NAME                     65: strMsg
        33924   LOAD_CONST                    42: 4
        33926   LOAD_CONST                    20: True
        33928   LOAD_CONST                    43: ('sendTeleMsg',)
        33930   CALL_FUNCTION_KW              3
        33932   POP_TOP                       
        33934   LOAD_NAME                     184: PE_LTP_Update_Count
        33936   LOAD_CONST                    436: 90
        33940   COMPARE_OP                    2 (==)
        33942   POP_JUMP_IF_FALSE             16994 (to 33988)
        33946   LOAD_CONST                    407: ' '
        33950   LOAD_GLOBAL                   382: df_cols
        33954   FORMAT_VALUE                  0
        33956   LOAD_CONST                    446: ' PE LTP '
        33960   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        33964   FORMAT_VALUE                  0
        33966   LOAD_CONST                    437: ' not updating for 3 Mins:'
        33970   BUILD_STRING                  5
        33972   STORE_NAME                    65: strMsg
        33974   LOAD_NAME                     59: iLog
        33976   LOAD_NAME                     65: strMsg
        33978   LOAD_CONST                    42: 4
        33980   LOAD_CONST                    20: True
        33982   LOAD_CONST                    43: ('sendTeleMsg',)
        33984   CALL_FUNCTION_KW              3
        33986   POP_TOP                       
        33988   LOAD_NAME                     184: PE_LTP_Update_Count
        33990   LOAD_CONST                    438: 120
        33994   COMPARE_OP                    2 (==)
        33996   POP_JUMP_IF_FALSE             17021 (to 34042)
        34000   LOAD_CONST                    407: ' '
        34004   LOAD_GLOBAL                   382: df_cols
        34008   FORMAT_VALUE                  0
        34010   LOAD_CONST                    446: ' PE LTP '
        34014   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        34018   FORMAT_VALUE                  0
        34020   LOAD_CONST                    439: ' not updating for 4 Mins:'
        34024   BUILD_STRING                  5
        34026   STORE_NAME                    65: strMsg
        34028   LOAD_NAME                     59: iLog
        34030   LOAD_NAME                     65: strMsg
        34032   LOAD_CONST                    42: 4
        34034   LOAD_CONST                    20: True
        34036   LOAD_CONST                    43: ('sendTeleMsg',)
        34038   CALL_FUNCTION_KW              3
        34040   POP_TOP                       
        34042   LOAD_NAME                     184: PE_LTP_Update_Count
        34044   LOAD_CONST                    440: 150
        34048   COMPARE_OP                    2 (==)
        34050   POP_JUMP_IF_FALSE             17048 (to 34096)
        34054   LOAD_CONST                    407: ' '
        34058   LOAD_GLOBAL                   382: df_cols
        34062   FORMAT_VALUE                  0
        34064   LOAD_CONST                    446: ' PE LTP '
        34068   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        34072   FORMAT_VALUE                  0
        34074   LOAD_CONST                    441: ' not updating for more than 5 Mins: Consider exiting Algo manually'
        34078   BUILD_STRING                  5
        34080   STORE_NAME                    65: strMsg
        34082   LOAD_NAME                     59: iLog
        34084   LOAD_NAME                     65: strMsg
        34086   LOAD_CONST                    42: 4
        34088   LOAD_CONST                    20: True
        34090   LOAD_CONST                    43: ('sendTeleMsg',)
        34092   CALL_FUNCTION_KW              3
        34094   POP_TOP                       
        34096   LOAD_NAME                     184: PE_LTP_Update_Count
        34098   LOAD_CONST                    442: 300
        34102   COMPARE_OP                    2 (==)
        34104   POP_JUMP_IF_FALSE             17075 (to 34150)
        34108   LOAD_CONST                    407: ' '
        34112   LOAD_GLOBAL                   382: df_cols
        34116   FORMAT_VALUE                  0
        34118   LOAD_CONST                    446: ' PE LTP '
        34122   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        34126   FORMAT_VALUE                  0
        34128   LOAD_CONST                    443: ' not updating for more than 10 Mins: Consider exiting Algo manually'
        34132   BUILD_STRING                  5
        34134   STORE_NAME                    65: strMsg
        34136   LOAD_NAME                     59: iLog
        34138   LOAD_NAME                     65: strMsg
        34140   LOAD_CONST                    42: 4
        34142   LOAD_CONST                    20: True
        34144   LOAD_CONST                    43: ('sendTeleMsg',)
        34146   CALL_FUNCTION_KW              3
        34148   POP_TOP                       
        34150   LOAD_NAME                     184: PE_LTP_Update_Count
        34152   LOAD_GLOBAL                   164: Trade_BankNifty
        34154   LOAD_CONST                    52: 2
        34156   BINARY_TRUE_DIVIDE            
        34158   COMPARE_OP                    5 (>=)
        34160   POP_JUMP_IF_FALSE             17114 (to 34228)
        34164   LOAD_GLOBAL                   163: NULL + Trade_Nifty
        34166   LOAD_CONST                    29: 1
        34168   COMPARE_OP                    2 (==)
        34170   POP_JUMP_IF_FALSE             17114 (to 34228)
        34174   LOAD_CONST                    407: ' '
        34178   LOAD_GLOBAL                   382: df_cols
        34182   FORMAT_VALUE                  0
        34184   LOAD_CONST                    446: ' PE LTP '
        34188   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        34192   FORMAT_VALUE                  0
        34194   LOAD_CONST                    444: ' not updating for '
        34198   LOAD_GLOBAL                   164: Trade_BankNifty
        34200   FORMAT_VALUE                  0
        34202   LOAD_CONST                    445: ' Secs: ExitTradenow Triggered : closing all Trades'
        34206   BUILD_STRING                  7
        34208   STORE_NAME                    65: strMsg
        34210   LOAD_NAME                     59: iLog
        34212   LOAD_NAME                     65: strMsg
        34214   LOAD_CONST                    42: 4
        34216   LOAD_CONST                    20: True
        34218   LOAD_CONST                    43: ('sendTeleMsg',)
        34220   CALL_FUNCTION_KW              3
        34222   POP_TOP                       
        34224   LOAD_CONST                    29: 1
        34226   STORE_GLOBAL                  80: ExitTradenow
        34228   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        34232   STORE_NAME                    186: PE_LTP_old
        34234   LOAD_NAME                     44: int
        34236   LOAD_NAME                     21: datetime
        34238   LOAD_ATTR                     21: datetime
        34240   LOAD_METHOD                   51: now
        34242   CALL_METHOD                   0
        34244   LOAD_METHOD                   52: strftime
        34246   LOAD_CONST                    50: '%H%M'
        34248   CALL_METHOD                   1
        34250   CALL_FUNCTION                 1
        34252   STORE_GLOBAL                  76: cur_HHMM
        34254   LOAD_NAME                     44: int
        34256   LOAD_NAME                     21: datetime
        34258   LOAD_ATTR                     21: datetime
        34260   LOAD_METHOD                   51: now
        34262   CALL_METHOD                   0
        34264   LOAD_METHOD                   52: strftime
        34266   LOAD_CONST                    291: '%H%M%S'
        34270   CALL_METHOD                   1
        34272   CALL_FUNCTION                 1
        34274   STORE_GLOBAL                  368: cur_HHMMSS
        34278   LOAD_GLOBAL                   80: strAdminChatID
        34280   LOAD_CONST                    29: 1
        34282   COMPARE_OP                    2 (==)
        34284   POP_JUMP_IF_TRUE              17149 (to 34298)
        34288   LOAD_GLOBAL                   77: NULL + read
        34290   LOAD_CONST                    29: 1
        34292   COMPARE_OP                    3 (!=)
        34294   POP_JUMP_IF_FALSE             17514 (to 35028)
        34298   LOAD_GLOBAL                   236: expiry_Perlot_MTM_lock_profit
        34300   POP_JUMP_IF_TRUE              17392 (to 34784)
        34304   LOAD_GLOBAL                   78: get
        34306   LOAD_CONST                    0: 0
        34308   COMPARE_OP                    2 (==)
        34310   POP_JUMP_IF_FALSE             17161 (to 34322)
        34314   LOAD_NAME                     322: close_all_orders
        34318   CALL_FUNCTION                 0
        34320   POP_TOP                       
        34322   LOAD_GLOBAL                   78: get
        34324   LOAD_CONST                    29: 1
        34326   COMPARE_OP                    2 (==)
        34328   POP_JUMP_IF_FALSE             17380 (to 34760)
        34332   LOAD_GLOBAL                   76: read
        34334   LOAD_GLOBAL                   360: PE_TGT_Triggered
        34338   LOAD_CONST                    0: 0
        34340   BINARY_SUBSCR                 
        34342   LOAD_GLOBAL                   360: PE_TGT_Triggered
        34346   LOAD_CONST                    29: 1
        34348   BINARY_SUBSCR                 
        34350   LOAD_CONST                    0: 0
        34352   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        34356   BINARY_MULTIPLY               
        34358   BUILD_LIST                    4
        34360   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        34362   LOAD_ATTR                     379: loc
        34366   LOAD_CONST                    0: 0
        34368   LOAD_NAME                     197: leg_cols
        34370   BUILD_TUPLE                   2
        34372   STORE_SUBSCR                  
        34374   LOAD_GLOBAL                   76: read
        34376   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        34380   LOAD_CONST                    0: 0
        34382   BINARY_SUBSCR                 
        34384   LOAD_GLOBAL                   361: NULL + PE_TGT_Triggered
        34388   LOAD_CONST                    29: 1
        34390   BINARY_SUBSCR                 
        34392   LOAD_CONST                    0: 0
        34394   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        34398   BINARY_MULTIPLY               
        34400   BUILD_LIST                    4
        34402   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        34404   LOAD_ATTR                     379: loc
        34408   LOAD_CONST                    0: 0
        34410   LOAD_NAME                     197: leg_cols
        34412   BUILD_TUPLE                   2
        34414   STORE_SUBSCR                  
        34416   LOAD_NAME                     24: pd
        34418   LOAD_METHOD                   380: concat
        34422   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        34424   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        34426   BUILD_LIST                    2
        34428   CALL_METHOD                   1
        34430   STORE_GLOBAL                  200: Current_legs
        34432   LOAD_GLOBAL                   200: normal_StikeAdj_SLPer
        34434   LOAD_METHOD                   400: to_csv
        34438   LOAD_CONST                    26: './log/'
        34440   LOAD_GLOBAL                   46: pandas
        34442   BINARY_ADD                    
        34444   LOAD_CONST                    375: '_Current_legs.txt'
        34448   BINARY_ADD                    
        34450   CALL_METHOD                   1
        34452   POP_TOP                       
        34454   LOAD_GLOBAL                   144: tl
        34456   LOAD_CONST                    29: 1
        34458   COMPARE_OP                    2 (==)
        34460   POP_JUMP_IF_FALSE             17293 (to 34586)
        34464   LOAD_GLOBAL                   76: read
        34466   LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        34470   LOAD_CONST                    0: 0
        34472   BINARY_SUBSCR                 
        34474   LOAD_GLOBAL                   363: NULL + partial_profit_booking_triggered
        34478   LOAD_CONST                    29: 1
        34480   BINARY_SUBSCR                 
        34482   LOAD_CONST                    0: 0
        34484   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        34488   BINARY_MULTIPLY               
        34490   BUILD_LIST                    4
        34492   LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        34494   LOAD_ATTR                     379: loc
        34498   LOAD_CONST                    0: 0
        34500   LOAD_NAME                     197: leg_cols
        34502   BUILD_TUPLE                   2
        34504   STORE_SUBSCR                  
        34506   LOAD_GLOBAL                   76: read
        34508   LOAD_GLOBAL                   364: partial_profit_booked
        34512   LOAD_CONST                    0: 0
        34514   BINARY_SUBSCR                 
        34516   LOAD_GLOBAL                   364: partial_profit_booked
        34520   LOAD_CONST                    29: 1
        34522   BINARY_SUBSCR                 
        34524   LOAD_CONST                    0: 0
        34526   LOAD_GLOBAL                   367: NULL + CE_LTP_Update_Count
        34530   BINARY_MULTIPLY               
        34532   BUILD_LIST                    4
        34534   LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        34536   LOAD_ATTR                     379: loc
        34540   LOAD_CONST                    0: 0
        34542   LOAD_NAME                     197: leg_cols
        34544   BUILD_TUPLE                   2
        34546   STORE_SUBSCR                  
        34548   LOAD_NAME                     24: pd
        34550   LOAD_METHOD                   380: concat
        34554   LOAD_GLOBAL                   201: NULL + normal_StikeAdj_SLPer
        34556   LOAD_GLOBAL                   202: normal_StikeAdj_TgtPer
        34558   BUILD_LIST                    2
        34560   CALL_METHOD                   1
        34562   STORE_GLOBAL                  203: Current_legs_hedge
        34564   LOAD_GLOBAL                   203: NULL + normal_StikeAdj_TgtPer
        34566   LOAD_METHOD                   400: to_csv
        34570   LOAD_CONST                    26: './log/'
        34572   LOAD_GLOBAL                   46: pandas
        34574   BINARY_ADD                    
        34576   LOAD_CONST                    376: '_Current_legs_hedge.txt'
        34580   BINARY_ADD                    
        34582   CALL_METHOD                   1
        34584   POP_TOP                       
        34586   LOAD_NAME                     44: int
        34588   LOAD_NAME                     21: datetime
        34590   LOAD_ATTR                     21: datetime
        34592   LOAD_METHOD                   51: now
        34594   CALL_METHOD                   0
        34596   LOAD_METHOD                   52: strftime
        34598   LOAD_CONST                    50: '%H%M'
        34600   CALL_METHOD                   1
        34602   CALL_FUNCTION                 1
        34604   STORE_GLOBAL                  76: cur_HHMM
        34606   LOAD_NAME                     44: int
        34608   LOAD_NAME                     21: datetime
        34610   LOAD_ATTR                     21: datetime
        34612   LOAD_METHOD                   51: now
        34614   CALL_METHOD                   0
        34616   LOAD_METHOD                   52: strftime
        34618   LOAD_CONST                    291: '%H%M%S'
        34622   CALL_METHOD                   1
        34624   CALL_FUNCTION                 1
        34626   STORE_GLOBAL                  368: cur_HHMMSS
        34630   LOAD_NAME                     56: open
        34632   LOAD_CONST                    377: './PNL/'
        34636   LOAD_GLOBAL                   46: pandas
        34638   BINARY_ADD                    
        34640   LOAD_CONST                    378: '_PNL.txt'
        34644   BINARY_ADD                    
        34646   LOAD_CONST                    28: 'a'
        34648   LOAD_CONST                    379: ''
        34652   LOAD_CONST                    380: ('newline',)
        34656   CALL_FUNCTION_KW              3
        34658   SETUP_WITH                    41
        34660   STORE_NAME                    401: f_object
        34664   LOAD_NAME                     8: writer
        34666   LOAD_NAME                     401: f_object
        34670   CALL_FUNCTION                 1
        34672   STORE_NAME                    402: writer_object
        34676   LOAD_NAME                     21: datetime
        34678   LOAD_ATTR                     21: datetime
        34680   LOAD_METHOD                   51: now
        34682   CALL_METHOD                   0
        34684   LOAD_METHOD                   52: strftime
        34686   LOAD_CONST                    24: '%Y%m%d'
        34688   CALL_METHOD                   1
        34690   LOAD_GLOBAL                   78: get
        34692   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        34694   BUILD_LIST                    3
        34696   STORE_NAME                    403: List
        34700   LOAD_NAME                     402: writer_object
        34704   LOAD_METHOD                   404: writerow
        34708   LOAD_NAME                     403: List
        34712   CALL_METHOD                   1
        34714   POP_TOP                       
        34716   LOAD_NAME                     401: f_object
        34720   LOAD_METHOD                   405: close
        34724   CALL_METHOD                   0
        34726   POP_TOP                       
        34728   POP_BLOCK                     
        34730   LOAD_CONST                    1: None
        34732   DUP_TOP                       
        34734   DUP_TOP                       
        34736   CALL_FUNCTION                 3
        34738   POP_TOP                       
        34740   JUMP_FORWARD                  9 (to 34760)
        34742   WITH_EXCEPT_START             
        34744   POP_JUMP_IF_TRUE              17375 (to 34750)
        34748   RERAISE                       1
        34750   POP_TOP                       
        34752   POP_TOP                       
        34754   POP_TOP                       
        34756   POP_EXCEPT                    
        34758   POP_TOP                       
        34760   LOAD_CONST                    447: ' ExitTradenow Triggered : closing all Trades'
        34764   STORE_NAME                    65: strMsg
        34766   LOAD_NAME                     59: iLog
        34768   LOAD_NAME                     65: strMsg
        34770   LOAD_CONST                    42: 4
        34772   LOAD_CONST                    20: True
        34774   LOAD_CONST                    43: ('sendTeleMsg',)
        34776   CALL_FUNCTION_KW              3
        34778   POP_TOP                       
        34780   LOAD_CONST                    20: True
        34782   STORE_GLOBAL                  236: processIndexExitTradenow
        34784   LOAD_NAME                     61: set_config_value
        34786   LOAD_CONST                    55: 'algo'
        34788   LOAD_CONST                    287: 'ExitTradenow'
        34792   LOAD_CONST                    122: '0'
        34794   CALL_FUNCTION                 3
        34796   POP_TOP                       
        34798   LOAD_NAME                     62: savedata
        34800   CALL_FUNCTION                 0
        34802   POP_TOP                       
        34804   LOAD_CONST                    381: ' Current LTP = '
        34808   LOAD_NAME                     44: int
        34810   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        34812   LOAD_CONST                    292: -1
        34816   BINARY_SUBSCR                 
        34818   CALL_FUNCTION                 1
        34820   FORMAT_VALUE                  0
        34822   LOAD_CONST                    313: ', '
        34826   LOAD_GLOBAL                   381: NULL + df_king_cnt
        34830   FORMAT_VALUE                  0
        34832   LOAD_CONST                    382: ' ATM CE = ('
        34836   LOAD_GLOBAL                   252: ST_Close
        34838   FORMAT_VALUE                  0
        34840   LOAD_CONST                    303: ','
        34844   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        34848   FORMAT_VALUE                  0
        34850   LOAD_CONST                    303: ','
        34854   LOAD_GLOBAL                   250: ST_Mult
        34856   FORMAT_VALUE                  0
        34858   LOAD_CONST                    383: '), '
        34862   LOAD_GLOBAL                   382: df_cols
        34866   FORMAT_VALUE                  0
        34868   LOAD_CONST                    384: ' ATM PE = ('
        34872   LOAD_GLOBAL                   253: NULL + ST_Close
        34874   FORMAT_VALUE                  0
        34876   LOAD_CONST                    303: ','
        34880   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        34884   FORMAT_VALUE                  0
        34886   LOAD_CONST                    303: ','
        34890   LOAD_GLOBAL                   251: NULL + ST_Mult
        34892   FORMAT_VALUE                  0
        34894   LOAD_CONST                    385: '),MTM SL='
        34898   LOAD_NAME                     374: round
        34902   LOAD_GLOBAL                   182: float
        34904   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        34906   LOAD_GLOBAL                   79: NULL + get
        34908   BINARY_MULTIPLY               
        34910   BINARY_ADD                    
        34912   LOAD_CONST                    0: 0
        34914   CALL_FUNCTION                 2
        34916   FORMAT_VALUE                  0
        34918   LOAD_CONST                    386: ',MTM TGT='
        34922   LOAD_NAME                     374: round
        34926   LOAD_GLOBAL                   182: float
        34928   LOAD_GLOBAL                   240: RSI_Low
        34930   LOAD_GLOBAL                   79: NULL + get
        34932   BINARY_MULTIPLY               
        34934   BINARY_ADD                    
        34936   LOAD_CONST                    0: 0
        34938   CALL_FUNCTION                 2
        34940   FORMAT_VALUE                  0
        34942   LOAD_CONST                    387: ', Calc MTM = '
        34946   LOAD_NAME                     374: round
        34950   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        34952   LOAD_CONST                    0: 0
        34954   CALL_FUNCTION                 2
        34956   FORMAT_VALUE                  0
        34958   BUILD_STRING                  24
        34960   STORE_NAME                    65: strMsg
        34962   LOAD_NAME                     59: iLog
        34964   LOAD_NAME                     65: strMsg
        34966   LOAD_CONST                    20: True
        34968   LOAD_CONST                    43: ('sendTeleMsg',)
        34970   CALL_FUNCTION_KW              2
        34972   POP_TOP                       
        34974   LOAD_NAME                     61: set_config_value
        34976   LOAD_CONST                    48: 'status'
        34978   LOAD_CONST                    49: 'algo_running_status'
        34980   LOAD_CONST                    122: '0'
        34982   CALL_FUNCTION                 3
        34984   POP_TOP                       
        34986   LOAD_NAME                     62: savedata
        34988   CALL_FUNCTION                 0
        34990   POP_TOP                       
        34992   LOAD_NAME                     59: iLog
        34994   LOAD_CONST                    267: ' Shutter down... Calling sys.exit() @ '
        34998   LOAD_NAME                     343: str
        35002   LOAD_GLOBAL                   76: read
        35004   CALL_FUNCTION                 1
        35006   BINARY_ADD                    
        35008   LOAD_CONST                    42: 4
        35010   LOAD_CONST                    20: True
        35012   LOAD_CONST                    43: ('sendTeleMsg',)
        35014   CALL_FUNCTION_KW              3
        35016   POP_TOP                       
        35018   LOAD_NAME                     0: sys
        35020   LOAD_METHOD                   344: exit
        35024   CALL_METHOD                   0
        35026   POP_TOP                       
        35028   LOAD_NAME                     21: datetime
        35030   LOAD_ATTR                     21: datetime
        35032   LOAD_METHOD                   51: now
        35034   CALL_METHOD                   0
        35036   LOAD_ATTR                     372: minute
        35040   STORE_NAME                    207: cur_min
        35042   LOAD_NAME                     44: int
        35044   LOAD_NAME                     21: datetime
        35046   LOAD_ATTR                     21: datetime
        35048   LOAD_METHOD                   51: now
        35050   CALL_METHOD                   0
        35052   LOAD_METHOD                   52: strftime
        35054   LOAD_CONST                    50: '%H%M'
        35056   CALL_METHOD                   1
        35058   CALL_FUNCTION                 1
        35060   STORE_GLOBAL                  76: cur_HHMM
        35062   LOAD_NAME                     44: int
        35064   LOAD_NAME                     21: datetime
        35066   LOAD_ATTR                     21: datetime
        35068   LOAD_METHOD                   51: now
        35070   CALL_METHOD                   0
        35072   LOAD_METHOD                   52: strftime
        35074   LOAD_CONST                    291: '%H%M%S'
        35078   CALL_METHOD                   1
        35080   CALL_FUNCTION                 1
        35082   STORE_GLOBAL                  368: cur_HHMMSS
        35086   LOAD_NAME                     207: cur_min
        35088   LOAD_GLOBAL                   158: no_of_lots
        35090   BINARY_MODULO                 
        35092   LOAD_CONST                    0: 0
        35094   COMPARE_OP                    2 (==)
        35096   POP_JUMP_IF_FALSE             17642 (to 35284)
        35100   LOAD_NAME                     209: king_min
        35102   LOAD_NAME                     207: cur_min
        35104   COMPARE_OP                    3 (!=)
        35106   POP_JUMP_IF_FALSE             17642 (to 35284)
        35110   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        35114   LOAD_GLOBAL                   87: NULL + strBotTokenWObot
        35116   COMPARE_OP                    4 (>)
        35118   POP_JUMP_IF_FALSE             17642 (to 35284)
        35122   LOAD_GLOBAL                   76: read
        35124   LOAD_GLOBAL                   88: int
        35126   COMPARE_OP                    4 (>)
        35128   POP_JUMP_IF_FALSE             17642 (to 35284)
        35132   LOAD_GLOBAL                   368: PE_LTP_Update_Count
        35136   LOAD_GLOBAL                   89: NULL + int
        35138   COMPARE_OP                    1 (<=)
        35140   POP_JUMP_IF_FALSE             17642 (to 35284)
        35144   LOAD_NAME                     21: datetime
        35146   LOAD_ATTR                     347: date
        35150   LOAD_METHOD                   348: today
        35154   CALL_METHOD                   0
        35156   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        35160   COMPARE_OP                    3 (!=)
        35162   POP_JUMP_IF_FALSE             17588 (to 35176)
        35166   LOAD_GLOBAL                   93: NULL + log_file_name
        35168   LOAD_CONST                    29: 1
        35170   COMPARE_OP                    2 (==)
        35172   POP_JUMP_IF_TRUE              17604 (to 35208)
        35176   LOAD_NAME                     21: datetime
        35178   LOAD_ATTR                     347: date
        35182   LOAD_METHOD                   348: today
        35186   CALL_METHOD                   0
        35188   LOAD_GLOBAL                   351: NULL + K_Direction_Formed
        35192   COMPARE_OP                    2 (==)
        35194   POP_JUMP_IF_FALSE             17642 (to 35284)
        35198   LOAD_GLOBAL                   92: log_file_name
        35200   LOAD_CONST                    29: 1
        35202   COMPARE_OP                    2 (==)
        35204   POP_JUMP_IF_FALSE             17642 (to 35284)
        35208   LOAD_NAME                     207: cur_min
        35210   STORE_NAME                    209: king_min
        35212   LOAD_NAME                     2: time
        35214   LOAD_METHOD                   2: time
        35216   CALL_METHOD                   0
        35218   STORE_NAME                    373: t1
        35222   LOAD_NAME                     332: King_candle
        35226   CALL_FUNCTION                 0
        35228   POP_TOP                       
        35230   LOAD_NAME                     2: time
        35232   LOAD_METHOD                   2: time
        35234   CALL_METHOD                   0
        35236   LOAD_NAME                     373: t1
        35240   BINARY_SUBTRACT               
        35242   STORE_NAME                    414: t2
        35246   LOAD_NAME                     414: t2
        35250   LOAD_CONST                    448: 2
        35254   COMPARE_OP                    4 (>)
        35256   POP_JUMP_IF_FALSE             17642 (to 35284)
        35260   LOAD_CONST                    449: 'Processing time(secs)= {0:.2f}'
        35264   LOAD_METHOD                   50: format
        35266   LOAD_NAME                     414: t2
        35270   CALL_METHOD                   1
        35272   STORE_NAME                    65: strMsg
        35274   LOAD_NAME                     59: iLog
        35276   LOAD_NAME                     65: strMsg
        35278   LOAD_CONST                    52: 2
        35280   CALL_FUNCTION                 2
        35282   POP_TOP                       
        35284   LOAD_NAME                     44: int
        35286   LOAD_NAME                     21: datetime
        35288   LOAD_ATTR                     21: datetime
        35290   LOAD_METHOD                   51: now
        35292   CALL_METHOD                   0
        35294   LOAD_METHOD                   52: strftime
        35296   LOAD_CONST                    50: '%H%M'
        35298   CALL_METHOD                   1
        35300   CALL_FUNCTION                 1
        35302   STORE_GLOBAL                  76: cur_HHMM
        35304   LOAD_GLOBAL                   76: read
        35306   LOAD_CONST                    450: 1530
        35310   COMPARE_OP                    4 (>)
        35312   POP_JUMP_IF_FALSE             17776 (to 35552)
        35316   LOAD_GLOBAL                   76: read
        35318   LOAD_CONST                    451: 1532
        35322   COMPARE_OP                    0 (<)
        35324   POP_JUMP_IF_FALSE             17776 (to 35552)
        35328   LOAD_CONST                    381: ' Current LTP = '
        35332   LOAD_NAME                     44: int
        35334   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        35336   LOAD_CONST                    292: -1
        35340   BINARY_SUBSCR                 
        35342   CALL_FUNCTION                 1
        35344   FORMAT_VALUE                  0
        35346   LOAD_CONST                    313: ', '
        35350   LOAD_GLOBAL                   381: NULL + df_king_cnt
        35354   FORMAT_VALUE                  0
        35356   LOAD_CONST                    382: ' ATM CE = ('
        35360   LOAD_GLOBAL                   252: ST_Close
        35362   FORMAT_VALUE                  0
        35364   LOAD_CONST                    303: ','
        35368   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        35372   FORMAT_VALUE                  0
        35374   LOAD_CONST                    303: ','
        35378   LOAD_GLOBAL                   250: ST_Mult
        35380   FORMAT_VALUE                  0
        35382   LOAD_CONST                    383: '), '
        35386   LOAD_GLOBAL                   382: df_cols
        35390   FORMAT_VALUE                  0
        35392   LOAD_CONST                    384: ' ATM PE = ('
        35396   LOAD_GLOBAL                   253: NULL + ST_Close
        35398   FORMAT_VALUE                  0
        35400   LOAD_CONST                    303: ','
        35404   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        35408   FORMAT_VALUE                  0
        35410   LOAD_CONST                    303: ','
        35414   LOAD_GLOBAL                   251: NULL + ST_Mult
        35416   FORMAT_VALUE                  0
        35418   LOAD_CONST                    385: '),MTM SL='
        35422   LOAD_NAME                     374: round
        35426   LOAD_GLOBAL                   182: float
        35428   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        35430   LOAD_GLOBAL                   79: NULL + get
        35432   BINARY_MULTIPLY               
        35434   BINARY_ADD                    
        35436   LOAD_CONST                    0: 0
        35438   CALL_FUNCTION                 2
        35440   FORMAT_VALUE                  0
        35442   LOAD_CONST                    386: ',MTM TGT='
        35446   LOAD_NAME                     374: round
        35450   LOAD_GLOBAL                   182: float
        35452   LOAD_GLOBAL                   240: RSI_Low
        35454   LOAD_GLOBAL                   79: NULL + get
        35456   BINARY_MULTIPLY               
        35458   BINARY_ADD                    
        35460   LOAD_CONST                    0: 0
        35462   CALL_FUNCTION                 2
        35464   FORMAT_VALUE                  0
        35466   LOAD_CONST                    387: ', Calc MTM = '
        35470   LOAD_NAME                     374: round
        35474   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        35476   LOAD_CONST                    0: 0
        35478   CALL_FUNCTION                 2
        35480   FORMAT_VALUE                  0
        35482   BUILD_STRING                  24
        35484   STORE_NAME                    65: strMsg
        35486   LOAD_NAME                     59: iLog
        35488   LOAD_NAME                     65: strMsg
        35490   LOAD_CONST                    20: True
        35492   LOAD_CONST                    43: ('sendTeleMsg',)
        35494   CALL_FUNCTION_KW              2
        35496   POP_TOP                       
        35498   LOAD_NAME                     61: set_config_value
        35500   LOAD_CONST                    48: 'status'
        35502   LOAD_CONST                    49: 'algo_running_status'
        35504   LOAD_CONST                    122: '0'
        35506   CALL_FUNCTION                 3
        35508   POP_TOP                       
        35510   LOAD_NAME                     62: savedata
        35512   CALL_FUNCTION                 0
        35514   POP_TOP                       
        35516   LOAD_NAME                     59: iLog
        35518   LOAD_CONST                    267: ' Shutter down... Calling sys.exit() @ '
        35522   LOAD_NAME                     343: str
        35526   LOAD_GLOBAL                   76: read
        35528   CALL_FUNCTION                 1
        35530   BINARY_ADD                    
        35532   LOAD_CONST                    42: 4
        35534   LOAD_CONST                    20: True
        35536   LOAD_CONST                    43: ('sendTeleMsg',)
        35538   CALL_FUNCTION_KW              3
        35540   POP_TOP                       
        35542   LOAD_NAME                     0: sys
        35544   LOAD_METHOD                   344: exit
        35548   CALL_METHOD                   0
        35550   POP_TOP                       
        35552   LOAD_GLOBAL                   193: NULL + normal_Perlot_MTM_SL
        35554   LOAD_ATTR                     415: to_json
        35558   LOAD_CONST                    452: './log/df_king.json'
        35562   LOAD_CONST                    453: 'records'
        35566   LOAD_CONST                    454: 'infer'
        35570   LOAD_CONST                    455: 'true'
        35574   LOAD_CONST                    456: ('orient', 'compression', 'index')
        35578   CALL_FUNCTION_KW              4
        35580   POP_TOP                       
        35582   LOAD_GLOBAL                   76: read
        35584   LOAD_GLOBAL                   198: expiry_StikeAdj_TgtPer
        35586   LOAD_CONST                    341: 'NQ'
        35590   BINARY_SUBSCR                 
        35592   LOAD_METHOD                   390: sum
        35596   CALL_METHOD                   0
        35598   LOAD_GLOBAL                   199: NULL + expiry_StikeAdj_TgtPer
        35600   LOAD_CONST                    341: 'NQ'
        35604   BINARY_SUBSCR                 
        35606   LOAD_METHOD                   390: sum
        35610   CALL_METHOD                   0
        35612   LOAD_NAME                     44: int
        35614   LOAD_NAME                     91: float
        35616   LOAD_GLOBAL                   165: NULL + Trade_BankNifty
        35618   LOAD_CONST                    292: -1
        35622   BINARY_SUBSCR                 
        35624   CALL_FUNCTION                 1
        35626   CALL_FUNCTION                 1
        35628   LOAD_GLOBAL                   381: NULL + df_king_cnt
        35632   LOAD_GLOBAL                   252: ST_Close
        35634   LOAD_GLOBAL                   264: expiry_Single_Leg_Adj
        35638   LOAD_GLOBAL                   250: ST_Mult
        35640   LOAD_GLOBAL                   382: df_cols
        35644   LOAD_GLOBAL                   253: NULL + ST_Close
        35646   LOAD_GLOBAL                   265: NULL + expiry_Single_Leg_Adj
        35650   LOAD_GLOBAL                   251: NULL + ST_Mult
        35652   LOAD_NAME                     374: round
        35656   LOAD_GLOBAL                   182: float
        35658   LOAD_GLOBAL                   239: NULL + expiry_Perlot_MTM_Trailing
        35660   LOAD_GLOBAL                   79: NULL + get
        35662   BINARY_MULTIPLY               
        35664   BINARY_ADD                    
        35666   LOAD_CONST                    0: 0
        35668   CALL_FUNCTION                 2
        35670   LOAD_NAME                     374: round
        35674   LOAD_GLOBAL                   182: float
        35676   LOAD_GLOBAL                   240: RSI_Low
        35678   LOAD_GLOBAL                   79: NULL + get
        35680   BINARY_MULTIPLY               
        35682   BINARY_ADD                    
        35684   LOAD_CONST                    0: 0
        35686   CALL_FUNCTION                 2
        35688   LOAD_NAME                     374: round
        35692   LOAD_GLOBAL                   219: NULL + ATM_strike_pe_offset
        35694   LOAD_CONST                    0: 0
        35696   CALL_FUNCTION                 2
        35698   LOAD_GLOBAL                   296: hedge_buy_price_buffer
        35702   LOAD_GLOBAL                   268: partial_profit_booking_enable
        35706   LOAD_GLOBAL                   269: NULL + partial_profit_booking_enable
        35710   LOAD_GLOBAL                   285: NULL + max_entry_time
        35714   LOAD_GLOBAL                   286: max_entry_time_exit
        35718   LOAD_NAME                     374: round
        35722   LOAD_GLOBAL                   293: NULL + hedge_buy_strike
        35726   LOAD_CONST                    52: 2
        35728   CALL_FUNCTION                 2
        35730   LOAD_NAME                     374: round
        35734   LOAD_GLOBAL                   294: hedge_buy_price
        35738   LOAD_CONST                    52: 2
        35740   CALL_FUNCTION                 2
        35742   LOAD_GLOBAL                   222: entry_price
        35744   LOAD_GLOBAL                   221: NULL + strike_offset
        35746   LOAD_NAME                     374: round
        35750   LOAD_GLOBAL                   231: NULL + normal_Perlot_MTM_lock_profit
        35752   LOAD_CONST                    0: 0
        35754   CALL_FUNCTION                 2
        35756   BUILD_LIST                    25
        35758   LOAD_NAME                     196: df_runtime
        35760   LOAD_ATTR                     379: loc
        35764   LOAD_CONST                    0: 0
        35766   LOAD_NAME                     195: df_runtime_cols
        35768   BUILD_TUPLE                   2
        35770   STORE_SUBSCR                  
        35772   LOAD_NAME                     196: df_runtime
        35774   LOAD_ATTR                     415: to_json
        35778   LOAD_CONST                    457: './log/df_runtime.json'
        35782   LOAD_CONST                    453: 'records'
        35786   LOAD_CONST                    454: 'infer'
        35790   LOAD_CONST                    455: 'true'
        35794   LOAD_CONST                    456: ('orient', 'compression', 'index')
        35798   CALL_FUNCTION_KW              4
        35800   POP_TOP                       
        35802   LOAD_NAME                     2: time
        35804   LOAD_METHOD                   355: sleep
        35808   LOAD_CONST                    52: 2
        35810   CALL_METHOD                   1
        35812   POP_TOP                       
        35814   JUMP_ABSOLUTE                 2659 (to 5318)
