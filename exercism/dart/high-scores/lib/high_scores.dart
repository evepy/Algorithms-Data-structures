class HighScores {
  //mandar despues la lista con valores enteros
  late List<int> scores;
  //Señalando la lista en la clase
  HighScores(this.scores);

  //Buscar el ultimo elemento agregado a la lista
  int latest() {
    return scores.last;
  }
  //Buscar el mayor elemento de la lista
  int personalBest() {
    //Ordenando la lista en descendiente
    scores.sort(
      (a, b) => b.compareTo(a),
    );
    //retorna el primer elemento de la lista
    return scores[0];
  }
//Buscar los tres mayores elementos de la lista 
  List<int> personalTopThree() {
    //Ordenando la lista en descendiente
    scores.sort(
      (a, b) => b.compareTo(a),
    );
    //Extraer los 3 primeros en una lista
    List<int> three = scores.sublist(0, 3);
    return three;
  }
}
