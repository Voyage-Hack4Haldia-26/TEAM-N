try { require("dotenv").config(); } catch (e) {}
const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => res.sendFile(path.join(__dirname, "index.html")));

app.get("/health", (req, res) =>
  res.json({ status: "ok", project: "Team N: AI Study Planner + Quiz", stack: "node" })
);

app.post("/api/plan", (req, res) => {
  // TODO: Body: {syllabus, days} -> plan
  res.status(501).json({ error: "Not implemented", todo: "Body: {syllabus, days} -> plan" });
});

app.post("/api/quiz", (req, res) => {
  // TODO: Body: {topic} -> questions[]
  res.status(501).json({ error: "Not implemented", todo: "Body: {topic} -> questions[]" });
});

app.post("/api/review", (req, res) => {
  // TODO: Body: {cardId, quality} -> next review date
  res.status(501).json({ error: "Not implemented", todo: "Body: {cardId, quality} -> next review date" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Team N server running on http://localhost:${PORT}`));
