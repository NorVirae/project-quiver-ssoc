# ArduPilot simulation practice

**Your outcome:** run a repeatable flight-mode exercise and explain its limits.

SITL means software in the loop. It lets you practise with flight-controller software and a simulated aircraft. It can teach modes, telemetry and mission logic. It does not establish Quiver's real endurance, payload capacity or handling without a validated physical model.

## Prepare the session

Your instructor will provides a tested installation, launch instructions, vehicle model, Quiver aircraft flight configurations and parameter baseline. Record firmware version or commit, model, parameter-file revision and launch command.

Confirm that only simulator endpoints are connected. Disconnect real-vehicle connections and label the session **SIMULATION**. Do not upload settings to shared hardware during another team's work.

## Fly the common exercise

1. Start the approved scenario. Check simulated position, home, mode and warnings.
2. Follow the instructor's arm and take-off procedure.
3. Hold position, make a short commanded move and observe altitude, speed and mode changes.
4. Use the configured return procedure, then land.
5. Save the log and a screenshot. Explain one unexpected result or warning.
6. Repeat individually as operator while a partner observes.

Guided follows supplied commands. Loiter attempts to hold position and altitude when the required estimates are available. RTL follows configured return behaviour. Land descends according to the configured landing behaviour.

