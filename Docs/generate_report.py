from weasyprint import HTML

# Defining the detailed User Testing Template HTML
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4;
            margin: 15mm;
            background-color: #fcfaf7;
        }
        body {
            font-family: 'Times New Roman', 'Times', serif;
            color: #333;
            line-height: 1.4;
            font-size: 10pt;
        }
        .header {
            background-color: #1a1a1a;
            color: #c5a059;
            padding: 20px;
            text-align: center;
            border-bottom: 3px solid #c5a059;
            margin-bottom: 20px;
        }
        h1 { margin: 0; font-size: 18pt; text-transform: uppercase; letter-spacing: 2px; }
        h2 { color: #1a1a1a; border-bottom: 1px solid #c5a059; padding-bottom: 5px; margin-top: 20px; font-size: 14pt; }
        .instruction-box {
            background-color: #fff;
            border: 1px solid #dcdcdc;
            padding: 15px;
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            background-color: #fff;
        }
        th {
            background-color: #f2f2f2;
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
            font-size: 9pt;
        }
        td {
            border: 1px solid #ccc;
            padding: 8px;
            height: 25px;
        }
        .formula-box {
            background-color: #1a1a1a;
            color: #fff;
            padding: 15px;
            text-align: center;
            font-family: 'Times New Roman', 'Times', serif;
        }
        .persona-section {
            display: flex;
            justify-content: space-between;
        }
        .footer {
            font-size: 8pt;
            text-align: center;
            color: #777;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Adnexio: UX Efficiency Testing Protocol</h1>
        <p>Comparative Analysis: Manual vs. AI Itinerary Generation</p>
    </div>

    <div class="instruction-box">
        <h2 style="margin-top: 0;">About Adnexio</h2>
        <p style="font-size: 11pt; font-style: italic; color: #1a1a1a; margin-top: 0;"><strong>Luxury, Redefined by Intelligence.</strong></p>
        <p>Adnexio is your private gateway to the most prestigious lifestyle experiences in the Middle East. Developed for the discerning traveler, our platform eliminates the noise of traditional search. By uniquely blending advanced AI with dedicated human concierge support, Adnexio crafts hyper-personalized itineraries in seconds, not hours. Whether it's a private yacht at sunset or a Michelin-starred table in the heart of Dubai, Adnexio ensures your journey is as seamless as it is extraordinary.</p>
        <p style="margin-bottom: 0;">Your time is your most precious asset. We're here to help you spend it beautifully.</p>
    </div>

    <div class="instruction-box">
        <strong>Objective:</strong> To quantify the efficiency gains of the Adnexio AI Concierge. We are measuring the time and accuracy required to plan a 3-day high-end itinerary in Dubai.
    </div>

    <h2>1. Tester Profile (Complete per User)</h2>
    <table style="table-layout: fixed;">
        <tr>
            <th width="15%">Tester ID:</th><td width="35%" style="height: 45px;"></td>
            <th width="15%">Target Tier:</th><td width="35%">[&#10003;] Elite</td>
        </tr>
        <tr>
            <th>Name / Initials:</th><td style="height: 45px;"></td>
            <th>Tech Savvy (1-5):</th><td></td>
        </tr>
        <tr>
            <th>Job / Occupation:</th><td style="height: 45px;"></td>
            <th>Age:</th><td></td>
        </tr>
    </table>

    <h2>2. Test Scenario</h2>
    <p><em>"Plan a 3-day 'Romantic Anniversary' trip to Dubai. You need to find and book:</em></p>
    <ul>
        <li><em>One evening activity with a view.</em></li>
        <li><em>One luxury dinner.</em></li>
        <li><em>One afternoon relaxation activity.</em></li>
    </ul>
    <p><em><strong>Goal:</strong> The itinerary must feel high-end and cohesive (the activities should make sense together)."</em></p>

    <h2 style="page-break-before: always;">3. Record Sheet: Method A (Manual Selection)</h2>
    <p><small>User adds experiences one-by-one using filters and manual date/time input.</small></p>
    <table>
        <tr>
            <th>Start Time</th>
            <th>End Time</th>
            <th>Total Minutes</th>
            <th>Conflict Count (Overlaps)</th>
            <th>Human Errors (Wrong date/price)</th>
        </tr>
        <tr>
            <td></td><td></td><td></td><td></td><td></td>
        </tr>
    </table>

    <h2>4. Record Sheet: Method B (AI Itinerary Generation)</h2>
    <p><small>User enters the scenario prompt into the AI Assistant and waits for the streamed result.</small></p>
    <table>
        <tr>
            <th>Start Time</th>
            <th>End Time</th>
            <th>Total Seconds</th>
            <th>Conflict Count (Overlaps)</th>
            <th>Prompt Re-tries</th>
        </tr>
        <tr>
            <td></td><td></td><td></td><td></td><td></td>
        </tr>
    </table>

    <h2>5. Post-Test Qualitative Evaluation</h2>
    <table>
        <tr>
            <th>Metric (1-10 Score)</th>
            <th>Manual Method</th>
            <th>AI Method</th>
        </tr>
        <tr><td>Ease of Use</td><td></td><td></td></tr>
        <tr><td>Confidence in Schedule</td><td></td><td></td></tr>
        <tr><td>Perceived Speed</td><td></td><td></td></tr>
    </table>

    <h2>6. Final Evaluation Calculation</h2>
    <div class="formula-box">
        Time Reduction % = [ (Manual_Time - AI_Time) / Manual_Time ] x 100
    </div>
    <table style="margin-top: 15px;">
        <tr>
            <th width="30%">Calculated Result:</th>
            <td style="height: 45px;"></td>
        </tr>
    </table>
    <div style="margin-bottom: 40px;"></div>

    <div class="footer">
        Confidential Document | Adnexio Project Portfolio | Say Digital Co., Ltd. (MOHARA)
    </div>
</body>
</html>
"""

# Convert to PDF
output_path = "Adnexio_User_Testing_Protocol_Template.pdf"
HTML(string=html_content).write_pdf(output_path)