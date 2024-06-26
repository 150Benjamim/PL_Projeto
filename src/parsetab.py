
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "CHAR COMMENT CR DEPTH DO DOTQUOTE DROP DUP ELSE EMIT IF INT ITERATION KEY LOOP NAME OPR PLUSLOOP SPACE SPACES SWAP THEN VARIABLE WORDexp : exp : term exp\n           | function exp\n           | conditional exp\n           | loop exp\n           | variable exp\n    term : factfunction : ':' NAME exp ';'conditional : IF exp ELSE exp THENloop : DO exp LOOPloop : DO exp PLUSLOOPvariable : VARIABLE WORDvariable : WORD '!'variable : WORD '@'fact : OPRfact : INTfact : WORDfact : COMMENTfact : '.'fact : DOTQUOTEfact : EMITfact : CHARfact : DUPfact : CRfact : SPACEfact : SPACESfact : SWAPfact : KEYfact : DEPTHfact : DROPfact : ITERATION"
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,37,38,39,42,43,44,46,],[-1,0,-1,-1,-1,-1,-1,-7,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-2,-3,-4,-5,-6,-12,-13,-14,-10,-11,-8,-9,]),':':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[8,8,8,8,8,8,-7,8,8,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,8,-12,-13,-14,8,-10,-11,-8,-9,]),'IF':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[9,9,9,9,9,9,-7,9,9,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,9,-12,-13,-14,9,-10,-11,-8,-9,]),'DO':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[10,10,10,10,10,10,-7,10,10,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,10,-12,-13,-14,10,-10,-11,-8,-9,]),'VARIABLE':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[11,11,11,11,11,11,-7,11,11,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,11,-12,-13,-14,11,-10,-11,-8,-9,]),'WORD':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[12,12,12,12,12,12,-7,12,12,37,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,12,-12,-13,-14,12,-10,-11,-8,-9,]),'OPR':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[13,13,13,13,13,13,-7,13,13,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,13,-12,-13,-14,13,-10,-11,-8,-9,]),'INT':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[14,14,14,14,14,14,-7,14,14,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,14,-12,-13,-14,14,-10,-11,-8,-9,]),'COMMENT':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[15,15,15,15,15,15,-7,15,15,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,15,-12,-13,-14,15,-10,-11,-8,-9,]),'.':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[16,16,16,16,16,16,-7,16,16,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,16,-12,-13,-14,16,-10,-11,-8,-9,]),'DOTQUOTE':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[17,17,17,17,17,17,-7,17,17,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,17,-12,-13,-14,17,-10,-11,-8,-9,]),'EMIT':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[18,18,18,18,18,18,-7,18,18,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,18,-12,-13,-14,18,-10,-11,-8,-9,]),'CHAR':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[19,19,19,19,19,19,-7,19,19,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,19,-12,-13,-14,19,-10,-11,-8,-9,]),'DUP':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[20,20,20,20,20,20,-7,20,20,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,20,-12,-13,-14,20,-10,-11,-8,-9,]),'CR':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[21,21,21,21,21,21,-7,21,21,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,21,-12,-13,-14,21,-10,-11,-8,-9,]),'SPACE':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[22,22,22,22,22,22,-7,22,22,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,22,-12,-13,-14,22,-10,-11,-8,-9,]),'SPACES':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[23,23,23,23,23,23,-7,23,23,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,23,-12,-13,-14,23,-10,-11,-8,-9,]),'SWAP':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[24,24,24,24,24,24,-7,24,24,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,24,-12,-13,-14,24,-10,-11,-8,-9,]),'KEY':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[25,25,25,25,25,25,-7,25,25,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,25,-12,-13,-14,25,-10,-11,-8,-9,]),'DEPTH':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[26,26,26,26,26,26,-7,26,26,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,26,-12,-13,-14,26,-10,-11,-8,-9,]),'DROP':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[27,27,27,27,27,27,-7,27,27,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,27,-12,-13,-14,27,-10,-11,-8,-9,]),'ITERATION':([0,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,37,38,39,41,42,43,44,46,],[28,28,28,28,28,28,-7,28,28,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,28,-12,-13,-14,28,-10,-11,-8,-9,]),'ELSE':([2,3,4,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,37,38,39,42,43,44,46,],[-1,-1,-1,-1,-1,-7,-1,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-2,-3,-4,-5,-6,41,-12,-13,-14,-10,-11,-8,-9,]),'LOOP':([2,3,4,5,6,7,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,36,37,38,39,42,43,44,46,],[-1,-1,-1,-1,-1,-7,-1,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-2,-3,-4,-5,-6,42,-12,-13,-14,-10,-11,-8,-9,]),'PLUSLOOP':([2,3,4,5,6,7,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,36,37,38,39,42,43,44,46,],[-1,-1,-1,-1,-1,-7,-1,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-2,-3,-4,-5,-6,43,-12,-13,-14,-10,-11,-8,-9,]),';':([2,3,4,5,6,7,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,42,43,44,46,],[-1,-1,-1,-1,-1,-7,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-2,-3,-4,-5,-6,-1,-12,-13,-14,44,-10,-11,-8,-9,]),'THEN':([2,3,4,5,6,7,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,37,38,39,41,42,43,44,45,46,],[-1,-1,-1,-1,-1,-7,-17,-15,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-2,-3,-4,-5,-6,-12,-13,-14,-1,-10,-11,-8,46,-9,]),'NAME':([8,],[34,]),'!':([12,],[38,]),'@':([12,],[39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp':([0,2,3,4,5,6,9,10,34,41,],[1,29,30,31,32,33,35,36,40,45,]),'term':([0,2,3,4,5,6,9,10,34,41,],[2,2,2,2,2,2,2,2,2,2,]),'function':([0,2,3,4,5,6,9,10,34,41,],[3,3,3,3,3,3,3,3,3,3,]),'conditional':([0,2,3,4,5,6,9,10,34,41,],[4,4,4,4,4,4,4,4,4,4,]),'loop':([0,2,3,4,5,6,9,10,34,41,],[5,5,5,5,5,5,5,5,5,5,]),'variable':([0,2,3,4,5,6,9,10,34,41,],[6,6,6,6,6,6,6,6,6,6,]),'fact':([0,2,3,4,5,6,9,10,34,41,],[7,7,7,7,7,7,7,7,7,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> <empty>','exp',0,'p_exp_empty','expression_gt.py',7),
  ('exp -> term exp','exp',2,'p_exp','expression_gt.py',11),
  ('exp -> function exp','exp',2,'p_exp','expression_gt.py',12),
  ('exp -> conditional exp','exp',2,'p_exp','expression_gt.py',13),
  ('exp -> loop exp','exp',2,'p_exp','expression_gt.py',14),
  ('exp -> variable exp','exp',2,'p_exp','expression_gt.py',15),
  ('term -> fact','term',1,'p_term','expression_gt.py',21),
  ('function -> : NAME exp ;','function',4,'p_function','expression_gt.py',26),
  ('conditional -> IF exp ELSE exp THEN','conditional',5,'p_conditional','expression_gt.py',36),
  ('loop -> DO exp LOOP','loop',3,'p_loop','expression_gt.py',42),
  ('loop -> DO exp PLUSLOOP','loop',3,'p_plusloop','expression_gt.py',62),
  ('variable -> VARIABLE WORD','variable',2,'p_variable1','expression_gt.py',82),
  ('variable -> WORD !','variable',2,'p_variable2','expression_gt.py',94),
  ('variable -> WORD @','variable',2,'p_variable3','expression_gt.py',103),
  ('fact -> OPR','fact',1,'p_factOPR','expression_gt.py',114),
  ('fact -> INT','fact',1,'p_factInt','expression_gt.py',142),
  ('fact -> WORD','fact',1,'p_factWord','expression_gt.py',148),
  ('fact -> COMMENT','fact',1,'p_factComment','expression_gt.py',157),
  ('fact -> .','fact',1,'p_factDOT','expression_gt.py',161),
  ('fact -> DOTQUOTE','fact',1,'p_factDOTQUOTE','expression_gt.py',166),
  ('fact -> EMIT','fact',1,'p_factEMIT','expression_gt.py',170),
  ('fact -> CHAR','fact',1,'p_factCHAR','expression_gt.py',175),
  ('fact -> DUP','fact',1,'p_factDUP','expression_gt.py',180),
  ('fact -> CR','fact',1,'p_factCR','expression_gt.py',185),
  ('fact -> SPACE','fact',1,'p_factSPACE','expression_gt.py',189),
  ('fact -> SPACES','fact',1,'p_factSPACES','expression_gt.py',194),
  ('fact -> SWAP','fact',1,'p_factSWAP','expression_gt.py',207),
  ('fact -> KEY','fact',1,'p_factKey','expression_gt.py',212),
  ('fact -> DEPTH','fact',1,'p_factDEPTH','expression_gt.py',218),
  ('fact -> DROP','fact',1,'p_factDROP','expression_gt.py',224),
  ('fact -> ITERATION','fact',1,'p_factITER','expression_gt.py',230),
]
