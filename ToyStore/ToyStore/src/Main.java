import controller.Controller;
import models.Models;

import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        Controller controller = new Controller();
        ArrayList<Models> newList = new ArrayList<>();
        Random random = new Random();
        newList.add(controller.addToys(
                (1), "L.O.L. Surprise! Fashion Dolls", 1, 100 / (random.nextInt(80)+ 1)));
        newList.add(controller.addToys(
                (2), "L.O.L. Surprise! Confetti Pop", 2, 100 / (random.nextInt(10) + 1)));
        newList.add(controller.addToys(
                (3), "L.O.L. Surprise! Dance Tots", 3, 100 / (random.nextInt(5) + 1)));

        System.out.print(newList);
        //shuffle(newList);
        System.out.println();
        System.out.print(newList);
        System.out.println();
        System.out.printf("Поздравляем, вы выиграли " + newList.get(2));
        System.out.printf("Поздравляем, вы выиграли " + newList.get(1));
        System.out.print("Поздравляем, вы выиграли " + newList.get(0));

        try (FileWriter fileWriter = new FileWriter("newList.txt")){
            for (Models toys: newList){
                fileWriter.append(toys.toString());
                //fileWriter.append("\n");
            }
        } catch (Exception e){
            System.out.println("Ошибка при загрузке в файл");
        }

    }

    public static<T> void shuffle(ArrayList<T> list)
    {
        Random random = new Random();
        for (int i = list.size() - 1; i >= 1; i--)
        {
            int j = random.nextInt(i + 1);
            T obj = list.get(i);
            list.set(i, list.get(j));
            list.set(j, obj);
        }
    }


}