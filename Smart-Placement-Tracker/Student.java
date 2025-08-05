package tracker;

public class Student {
    private int id;
    private String name;
    private String department;
    private float cgpa;
    private boolean placed;

    public Student(String name, String department, float cgpa) {
        this.name = name;
        this.department = department;
        this.cgpa = cgpa;
        this.placed = false;
    }

    // Getters and Setters
    public String getName() { return name; }
    public String getDepartment() { return department; }
    public float getCgpa() { return cgpa; }
    public boolean isPlaced() { return placed; }

    public void setPlaced(boolean placed) { this.placed = placed; }
}
