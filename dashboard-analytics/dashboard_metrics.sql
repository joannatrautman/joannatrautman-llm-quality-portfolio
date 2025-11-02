-- Aggregate quality metrics by topic and grade level
SELECT
  topic,
  grade_level,
  AVG(accuracy_score)   AS avg_accuracy,
  AVG(clarity_score)    AS avg_clarity,
  AVG(tone_score)       AS avg_tone,
  AVG(alignment_score)  AS avg_alignment,
  COUNT(*)              AS sample_size
FROM llm_evaluations
GROUP BY topic, grade_level
ORDER BY avg_accuracy DESC, avg_alignment DESC;
