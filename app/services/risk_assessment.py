from app.models.loan_application import LoanApplication

class RiskAssessment:
    def calculate_risk_score(self, application: LoanApplication) -> int:
        score = 0
        if application.credit_score < 600:
            score += 100
        if application.loan_amount > application.income * 5:
            score += 200
        return score
    
    def approve_or_reject(self, application: LoanApplication) -> bool:
        risk_score = self.calculate_risk_score(application)
        return risk_score <= 600 and application.loan_amount <= application.income * 2
