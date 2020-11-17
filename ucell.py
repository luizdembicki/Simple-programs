from math import sqrt 
# Returns the closest unit cell type given atomic weight, radius and the comparation mass
# avogrado constant and input
Na = 6.022 * pow(10,23)
A = float(input("Provide the atomic weight: "))
R = float(input("Provide the atomic radius: ")) / (10 ** 7) # optimized for nanometers
# types of unit cells
SC = 1 / (8 * R ** 3)
FCC = 4 / (16 * pow(R, 3) * sqrt(2))
BCC = (2 *  3 * sqrt(3)) / (64 * pow(R, 3))
utypes = {'Simple Cube': SC, 'Face Centered Cube': FCC, 'Body Centered Cube': BCC}
# atomic mass template
RO = A / Na
# comparission input and results dictionary
COMP = float(input("Provide atomic mass for comparation: "))
results = {}
# calculations
for utype, value in utypes.items():
    results[f'{utype}'] = abs(COMP - value * RO)
    print(f"Type: {utype}, difference: {COMP - value * RO}")
# show lowest value
print(f"\nProbably a {min(results.keys(),key=( lambda k: results[k]))}")
#         ...                        .                        ....                                               ..       .                    ..         .      
#     .zf"` `"tu                    @88>                  .xH888888Hx.                                     . uW8"        @88>            < .z@8"`        @88>    
#    x88      '8N.    x.    .       %8P        ..       .H8888888888888:                  ..    .     :    `t888         %8P              !@88E          %8P     
#    888k     d88&  .@88k  z88u      .       .@88i      888*"""?""*88888X        .u     .888: x888  x888.   8888   .      .          .    '888E   u       .      
#    8888N.  @888F ~"8888 ^8888    .@88u    ""%888>    'f     d8x.   ^%88k    ud8888.  ~`8888~'888X`?888f`  9888.z88N   .@88u   .udR88N    888E u@8NL   .@88u    
#    `88888 9888%    8888  888R   ''888E`     '88%     '>    <88888X   '?8  :888'8888.   X888  888X '888>   9888  888E ''888E` <888'888k   888E`"88*"  ''888E`   
#      %888 "88F     8888  888R     888E    ..dILr~`    `:..:`888888>    8> d888 '88%"   X888  888X '888>   9888  888E   888E  9888 'Y"    888E .dN.     888E    
#       8"   "*h=~   8888  888R     888E   '".-%88b            `"*88     X  8888.+"      X888  888X '888>   9888  888E   888E  9888        888E~8888     888E    
#     z8Weu          8888 ,888B .   888E    @  '888k      .xHHhx.."      !  8888L        X888  888X '888>   9888  888E   888E  9888        888E '888&    888E    
#    ""88888i.   Z  "8888Y 8888"    888&   8F   8888     X88888888hx. ..!   '8888c. .+  "*88%""*88" '888!` .8888  888"   888&  ?8888u../   888E  9888.   888&    
#   "   "8888888*    `Y"   'YP      R888" '8    8888    !   "*888888888"     "88888%      `~    "    `"`    `%888*%"     R888"  "8888P'  '"888*" 4888"   R888"   
#         ^"**""                     ""   '8    888F           ^"***"`         "YP'                            "`         ""      "P'       ""    ""      ""     
#                                          %k  <88F                                                                                                              
#                                           "+:*%`                                                                                                               
#     .--~*teu.        .n~~%x.       .--~*teu.        .n~~%x.                                                                                                    
#    dF     988Nx    x88X   888.    dF     988Nx    x88X   888.                                                                                                  
#   d888b   `8888>  X888X   8888L  d888b   `8888>  X888X   8888L                                                                                                 
#   ?8888>  98888F X8888X   88888  ?8888>  98888F X8888X   88888                                                                                                 
#    "**"  x88888~ 88888X   88888X  "**"  x88888~ 88888X   88888X                                                                                                
#         d8888*`  88888X   88888X       d8888*`  88888X   88888X                                                                                                
#       z8**"`   : 88888X   88888f     z8**"`   : 88888X   88888f                                                                                                
#     :?.....  ..F 48888X   88888    :?.....  ..F 48888X   88888                                                                                                 
#    <""888888888~  ?888X   8888"   <""888888888~  ?888X   8888"                                                                                                 
#    8:  "888888*    "88X   88*`    8:  "888888*    "88X   88*`                                                                                                  
#    ""    "**"`       ^"==="`      ""    "**"`       ^"==="`                                                                                                    
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                             
                                                                                                                                                                                                                  
