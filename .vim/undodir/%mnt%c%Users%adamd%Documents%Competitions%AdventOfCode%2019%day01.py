Vim�UnDo� �۳1�C�At#/�m�����`9���G�b\`d   "                 ;       ;   ;   ;    _�F    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _�A�     �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�A�     �                  �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�B$     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B+     �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B-     �                   d 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�B.     �                     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�BQ     �                     math.floor()5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             _�BU     �                     return math.floor()5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             _�Bg     �                     return math.floor() - 25�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             _�Br     �                      return math.floor(mass/) - 25�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             _�Bu     �                     return math.floor(mass/ - 25�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�Bv     �                      return math.floor(mass/3 - 25�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B�     �                 !    return math.floor(mass//3 - 25�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B�    �                     return (mass//3 - 25�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B�    �                 �               �                  """Day 01"""   import math       def req_fuel(mass: int) -> int:       return mass//3 - 25�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B�     �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B�     �                 assert req_fuel()5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             _�B�     �                 assert req_fuel()5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             _�B�     �   	              assert req_fuel()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B�    �   
              assert req_fuel()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B�    �                 �               �                  """Day 01"""   import math           def req_fuel(mass: int) -> int:       return mass // 3 - 2       assert req_fuel(12) == 2   assert req_fuel(14) == 2   assert req_fuel(1969) == 654    assert req_fuel(100756) == 335835�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�B�     �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�C     �                 fuel_sum = sum()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�CY     �                �             5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             _�Cd     �               with open()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�Cm     �               with open('input/day01.txt')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�C�     �                   fuel_sum = sum()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�C�     �               .    fuel_sum = sum( for line in f.readlines())5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�C�     �               8    fuel_sum = sum(req_fuel() for line in f.readlines())5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�C�     �                fuel_sum = sum()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�C�     �                     �               5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             _�C�    �                 print()5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                             _�C�     �               D    fuel_sum = sum(req_fuel(line.strip()) for line in f.readlines())5�_�   !   #           "      !    ����                                                                                                                                                                                                                                                                                                                                                             _�C�     �               I    fuel_sum = sum(req_fuel(int()line.strip()) for line in f.readlines())5�_�   "   $           #      -    ����                                                                                                                                                                                                                                                                                                                                                             _�C�   	 �               H    fuel_sum = sum(req_fuel(int(line.strip()) for line in f.readlines())5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             _�D@     �                  �               5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                             _�D�     �                 *def iterative_req_fuel(input: int) -> int:5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             _�D�     �                     �               5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                             _�D�     �                   �             5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                             _�D�     �                 5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                                                             _�D�     �                         �               5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                             _�E
     �                         total += req_fuel()5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                             _�E    
 �                       total += req_fuel(mass)5�_�   +   -           ,          ����                                                                                                                                                                                                                                                                                                                                                             _�E"    �                 �               �                  """Day 01"""   import math           def req_fuel(mass: int) -> int:       return mass // 3 - 2           assert req_fuel(12) == 2   assert req_fuel(14) == 2   assert req_fuel(1969) == 654    assert req_fuel(100756) == 33583       "with open('input/day01.txt') as f:   I    fuel_sum = sum(req_fuel(int(line.strip())) for line in f.readlines())   print(fuel_sum)       )def iterative_req_fuel(mass: int) -> int:       total = 0       while mass > 0:           mass += req_fuel(mass)           total += mass5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                                                             _�E/     �                         �               5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                                             _�EE     �               �               5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                             _�EK    �               I    fuel_sum = sum(req_fuel(int(line.strip())) for line in f.readlines())5�_�   /   1           0      $    ����                                                                                                                                                                                                                                                                                                                                                             _�EU    �                 �               �                  """Day 01"""   import math           def req_fuel(mass: int) -> int:       return mass // 3 - 2           assert req_fuel(12) == 2   assert req_fuel(14) == 2   assert req_fuel(1969) == 654    assert req_fuel(100756) == 33583       "with open('input/day01.txt') as f:   I    fuel_sum = sum(req_fuel(int(line.strip())) for line in f.readlines())   print(fuel_sum)           )def iterative_req_fuel(mass: int) -> int:       total = 0       while mass > 0:           mass += req_fuel(mass)           total += mass       return total           "with open('input/day01.txt') as f:   S    fuel_sum = sum(iterative_req_fuel(int(line.strip())) for line in f.readlines())   print(fuel_sum)5�_�   0   2           1           ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�Ei     �             �             5�_�   1   3           2           ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�Ek     �         !    5�_�   2   4           3          ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�E{     �         "       assert req_fuel(100756) == 335835�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�E�     �         "      assert req_fuel(1969) == 6545�_�   4   6           5          ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�E�    �         "      assert req_fuel(14) == 25�_�   5   7           6          ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�E�    �         "      assert req_fuel(14) == 6545�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�E�     �         "      assert req_fuel(14) == 25�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�E�     �         "      assert req_fuel(1969) == 9665�_�   8   :           9          ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�E�    �         "       assert req_fuel(100756) == 503465�_�   9   ;           :   !   .    ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�F    �       #   "      H        iterative_req_fuel(int(line.strip())) for line in f.readlines())5�_�   :               ;   "       ����                                                                                                                                                                                                                                                                                                                            
                     V   $    _�F    �          #       �               �               #   """Day 01"""   import math           def req_fuel(mass: int) -> int:       return mass // 3 - 2           assert req_fuel(12) == 2   assert req_fuel(14) == 2   assert req_fuel(1969) == 654    assert req_fuel(100756) == 33583       "with open('input/day01.txt') as f:   I    fuel_sum = sum(req_fuel(int(line.strip())) for line in f.readlines())   print(fuel_sum)           )def iterative_req_fuel(mass: int) -> int:       total = 0       while mass > 0:           mass += req_fuel(mass)           total += mass       return total           "assert iterative_req_fuel(14) == 2   &assert iterative_req_fuel(1969) == 966   *assert iterative_req_fuel(100756) == 50346       "with open('input/day01.txt') as f:       fuel_sum = sum(   .        iterative_req_fuel(int(line.strip()))    "        for line in f.readlines())   print(fuel_sum)5��