package controller;
import view.View;
import models.Models;

public class Controller {
    View view;
    Models model;

    public Controller() {
        this.view = new View();
        this.model = new Models();
    }

    public Models addToys(int id, String name, int count, int frequency) {
        return view.addToys(id, name, count, frequency);
    }

}
