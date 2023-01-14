class ArmstrongNumbers {
  // Put your code here
  bool isArmstrongNumber(int number) {

    //Resultado final
    int resultado=0;
    //Cantidad de digitos de un numero -> En cadena
    int longitud = number.toString().length;
    //Lista con los números que existen -> En cadena
    List<String> lb = number.toString().split('');
    //Lista con los números que existe para un numero principal -> En entero
    List<int> lista = lb.map(int.parse).toList();
    
    //Recorrido con todos los elementos de la lista
    for (int i in lista) {
      //Multiplicar el elemento de la lista por la longitud
      i = i * longitud;
      //Acumular y sumar los elementos de la lista
      resultado += i;
      
    }
    //Comprobar si el número ingresado es armstrong
    return number == resultado;
  }
}
