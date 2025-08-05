package tracker;

import java.sql.Connection;
import java.sql.PreparedStatement;

public class CompanyDAO {
    public void insertCompany(Company company) {
        try (Connection conn = DBConnection.connect()) {
            String sql = "INSERT INTO companies (company_name, min_cgpa) VALUES (?, ?)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, company.getName());
            stmt.setFloat(2, company.getMinCgpa());

            int rowsInserted = stmt.executeUpdate();
            if (rowsInserted > 0) {
                System.out.println("✅ Company added successfully.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
