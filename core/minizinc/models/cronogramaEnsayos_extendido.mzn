include "globals.mzn";
% Parámetros
enum ACTORES;
int: NumActores = length(ACTORES);
array[1..NumActores,int] of int: Escenas;
int: NumEscenas = length(index_set_2of2(Escenas))-1;
array[1..NumEscenas] of int: Duracion;
array[1..NumActores,1..2] of int: Disponibilidad;
array[int,1..2] of int: Evitar;
int: NumEvitar = length(index_set_1of2(Evitar));

% Variables
array[1..NumEscenas] of var 1..NumEscenas: Sol;
var int: costo;
array[1..NumActores,1..3] of var int: Actor_Escenas;
array[1..NumActores] of var int: Actor_Costo;
array[1..NumEvitar] of var int: compartidos;
var int: Tiempo_Compartido;
%var int: dur;

% Funciones
function array[1..3] of var int: CalcularDuracion(array[int] of var opt int:sub) =
  let {
    var int: f = min(sub);
    var int: e = max(sub);
  } in [f,e,sum(i in f..e)(Duracion[Sol[i]])];

function var int: CalcularCompartidos(int:actor1, int: actor2) = 
  sum(i in Actor_Escenas[actor1,1]..Actor_Escenas[actor1,2],j in Actor_Escenas[actor2,1]..Actor_Escenas[actor2,2])(
    if i = j then Duracion[Sol[i]] else 0 endif);
   

% Restricciones
% Establece el indice de la primera escena, la ultima escena y la duracion de un actor en el set
constraint forall(i in 1..NumActores)(
  let {
    array[1..3] of var int: a = CalcularDuracion([ j | j in 1..NumEscenas where Escenas[i,Sol[j]]=1 ]);
  } in forall(k in 1..3)(Actor_Escenas[i,k]=a[k]));
% Estabece el costo de cada actor de acuerdo al tiempo que estarian en el set 
constraint forall(i in 1..NumActores)(
  Actor_Costo[i] = Actor_Escenas[i,3]*Escenas[i,NumEscenas+1]);
% Suma los costos y establece el costo final  
constraint costo = sum(i in 1..NumActores)(Actor_Costo[i]);
% Establece que cada actor no supere el tiempo disponible
constraint forall(i in 1..NumActores)(
  if Disponibilidad[i,2]!=0
  then Actor_Escenas[i,3] <= Disponibilidad[i,2]
  else true endif);
% Establece el tiempo copartido por los actores en la fila i en el set de grabacion 
constraint forall(i in 1..NumEvitar)(
  compartidos[i] = CalcularCompartidos(Evitar[i,1],Evitar[i,2]));
% EStablece el tiempo total que se compartio entre actores que se debianevitar
constraint Tiempo_Compartido = sum(i in 1..NumEvitar)(compartidos[i]);
% Establece que no se repitan escenas en la planeacion
constraint alldifferent(Sol);

% Funcion OBjetivo ajustada para evitar cuando sea posible

% Busq por defecto
%solve minimize (costo+Tiempo_Compartido);
% Busq al azar
%solve ::int_search(Sol,input_order,indomain_random) minimize (costo+Tiempo_Compartido);
% Busq domino mas pequeño
%solve ::int_search(Sol,first_fail,indomain_min) minimize (costo+Tiempo_Compartido);
% Busq Ponderacion de fallos
solve ::int_search(Sol,dom_w_deg,indomain_min) minimize (costo+Tiempo_Compartido);
%

output [show(Sol[i])++" "|i in index_set(Sol)]++[show(costo)++" "]++[show(Tiempo_Compartido)];