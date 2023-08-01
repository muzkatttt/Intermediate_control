import controller.Controller;
import models.Models;

import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        Controller controller = new Controller();

        controller.addToys(1, "L.O.L. Surprise! Fashion Dolls", 2, 1);
        controller.addToys(2, "L.O.L. Surprise! Confetti Pop", 3, 2);
        controller.addToys(3, "L.O.L. Surprise! Dance Tots", 5, 3);
        int counts = 10;
        ArrayList<Models> newList = new ArrayList<>();
        while(newList.size() < counts) {
            newList.add(controller.addToys((1), "L.O.L. Surprise! Fashion Dolls", 2, 1));
            newList.add(controller.addToys((2), "L.O.L. Surprise! Confetti Pop", 3, 2));
            newList.add(controller.addToys((3), "L.O.L. Surprise! Dance Tots", 5, 3));
        }
        shuffle(newList);
        System.out.println();
        System.out.println(newList);
    }

    public static<T> void shuffle(ArrayList<T> list)
    {
        Random random = new Random();

        // начинаем с конца списка
        for (int i = list.size() - 1; i >= 1; i--)
        {
            // получить случайный индекс `j` такой, что `0 <= j <= i`
            int j = random.nextInt(i + 1);

            // поменять местами элемент в i-й позиции в списке с элементом в
            // случайно сгенерированный индекс `j`
            T obj = list.get(i);
            list.set(i, list.get(j));
            list.set(j, obj);
        }
    }


}