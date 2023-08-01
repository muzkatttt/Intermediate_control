package models;

import java.util.Comparator;

public class ToyComparator implements Comparator<Models> {

    @Override
    public int compare(Models o1, Models o2) {
        int result = o1.compareTo(o2);
        return result;
    }
}