package view;

import models.Models;
import toyInterface.ToyInterface;

public class View implements ToyInterface {

    @Override
    public Models addToys(int id, String name, int count, int frequency) {
        Models toy;
        toy = new Models(id, name, count, frequency);
        toy.setId(id);
        toy.setName(name);
        toy.setCount(count);
        toy.setFrequency(frequency);
        return toy;
    }
}
