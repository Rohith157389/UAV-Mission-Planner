 UAV Mission Planner (Agentic AI)
 Project Overview
The UAV Mission Planner is an **AI-powered system** that analyzes drone missions and decides whether they are safe to execute.
It uses **Groq + LangChain** to simulate intelligent decision-making by evaluating:
* Battery level
* Weather conditions
* No-fly zones
 Objectives
* Automate UAV mission decision-making
* Improve safety using AI analysis
* Provide clear mission approval or rejection
*  Battery feasibility check
*  Weather safety analysis
*  No-fly zone detection
*  AI-based decision making
*  Mission history storage 
* Python
* LangChain
* Groq API
* dotenv

 Project Structure

uav-mission-planner/
│
├── app.py         
├── tools.py        
├── memory.py      
├── history.json   
├── requirements.txt
├── README.md

 How to Run the Project

 1. Clone the Repository

bash
git clone https://github.com/your-username/uav-mission-planner.git
cd uav-mission-planner

 2. Install Dependencies

bash
pip install -r requirements.txt
 3. Add API Key
Create a `.env` file and add:
GROQ_API_KEY=your_api_key_here
 4. Run the Application
bash
python app.py
Sample Output

**GREEN LIGHT** → Mission Approved
 **CANCEL** → Mission Rejected
 Example Decision Logic

* If battery is low →  Cancel
* If weather is unsafe →  Cancel
* If no-fly zone exists →  Cancel
* Otherwise →  Approve mission


---

## 🚀 Future Improvements

* Add web interface (Flask)
* Integrate real-time weather API
* Add map-based route visualization

