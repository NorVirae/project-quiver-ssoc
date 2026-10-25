# ArduPilot simulation practice

**Your outcome:** run a repeatable flight-mode exercise and explain its limits.

SITL means software in the loop. It lets you practise with flight-controller software and a simulated aircraft. It can teach modes, telemetry and mission logic. It does not establish Quiver's real endurance, payload capacity or handling without a validated physical model.

## Prepare the session

The instructor provides a tested installation, launch instructions, vehicle model and parameter baseline. Record firmware version or commit, model, parameter-file revision and launch command.

Confirm that only simulator endpoints are connected. Disconnect real-vehicle connections and label the session **SIMULATION**. Do not upload settings to shared hardware during another team's work.

## Fly the common exercise

1. Start the approved scenario. Check simulated position, home, mode and warnings.
2. Follow the instructor's arm and take-off procedure.
3. Hold position, make a short commanded move and observe altitude, speed and mode changes.
4. Use the configured return procedure, then land.
5. Save the log and a screenshot. Explain one unexpected result or warning.
6. Repeat individually as operator while a partner observes.

Guided follows supplied commands. Loiter attempts to hold position and altitude when the required estimates are available. RTL follows configured return behaviour. Land descends according to the configured landing behaviour.

## Keep the result honest

The Quiver repository includes an obstacle-avoidance SITL evaluation with approximate aircraft configuration and simulated sensors. Its launch command alone is not a complete, validated Quiver physics model. Advanced exercises need the matching firmware, parameters and sensor configuration verified by the instructor.

Change only one approved parameter at a time. Record the baseline, prediction, change and result, then restore the baseline. Never bypass a safety check to obtain an apparent success.

## Practise and show

Submit your launch record, one flight log, one explained anomaly and two model limitations. Another student should be able to repeat the setup.

Sources S7 and P5. Passing the simulation exercise does not authorise real flight.

