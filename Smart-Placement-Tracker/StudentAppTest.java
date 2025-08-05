package tracker;

public class StudentAppTest {
    public static void main(String[] args) {
        Student s1 = new Student("Asmita Jadhav", "E&TC", 8.35f);
        StudentDAO dao = new StudentDAO();
        dao.insertStudent(s1);
    }
}
