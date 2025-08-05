package tracker;

public class Company {
    private int id;
    private String name;
    private float minCgpa;

    public Company(String name, float minCgpa) {
        this.name = name;
        this.minCgpa = minCgpa;
    }

    public String getName() { return name; }
    public float getMinCgpa() { return minCgpa; }
}
