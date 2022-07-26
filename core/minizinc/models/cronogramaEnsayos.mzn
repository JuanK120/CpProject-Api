include "globals.mzn";
% Parámetros
enum ACTORES;
int: NumActores = length(ACTORES);
array[1..NumActores,int] of int: Escenas;
int: NumEscenas = length(index_set_2of2(Escenas))-1;
array[1..NumEscenas] of int: Duracion;

% Variables
array[1..NumEscenas] of var 1..NumEscenas: Sol;
var int: costo;
array[1..NumActores] of var int: Actor_Escenas;
array[1..NumActores] of var int: Actor_Costo;

% Funciones
function var int: CalcularDuracion(array[int] of var opt int:sub) =
  let {
    var int: f = min(sub);
    var int: e = max(sub);
  } in sum(i in f..e)(Duracion[Sol[i]]);

% Restricciones
% Establece la duracion de un actor en el set
constraint forall(i in 1..NumActores)(
  Actor_Escenas[i] = CalcularDuracion([ j | j in 1..NumEscenas where Escenas[i,Sol[j]]=1 ]));
% Estabece el costo de cada actor de acuerdo al tiempo que estarian en el set 
constraint forall(i in 1..NumActores)(
  Actor_Costo[i] = Actor_Escenas[i]*Escenas[i,NumEscenas+1]);
% Suma los costos y establece el costo final  
constraint costo = sum(i in 1..NumActores)(Actor_Costo[i]);
% Establece que no se repitan escenas en la planeacion
constraint alldifferent(Sol);

% Busq por defecto
%solve minimize costo;
% Busq al azar
%solve ::int_search(Sol,input_order,indomain_random) minimize costo;
% Busq domino mas pequeño
%solve ::int_search(Sol,first_fail,indomain_min) minimize costo;
% Busq Ponderacion de fallos
solve ::int_search(Sol,dom_w_deg,indomain_min) minimize costo;
%

output [show(Sol[i])++" "|i in index_set(Sol)]++[show(costo)];