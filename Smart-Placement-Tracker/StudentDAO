package tracker;

import java.sql.*;

public class StudentDAO {
    public void insertStudent(Student student) {
        try (Connection conn = DBConnection.connect()) {
            String sql = "INSERT INTO students (name, department, cgpa, placed) VALUES (?, ?, ?, ?)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, student.getName());
            stmt.setString(2, student.getDepartment());
            stmt.setFloat(3, student.getCgpa());
            stmt.setBoolean(4, student.isPlaced());

            int rowsInserted = stmt.executeUpdate();
            if (rowsInserted > 0) {
                System.out.println("✅ Student added successfully.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
