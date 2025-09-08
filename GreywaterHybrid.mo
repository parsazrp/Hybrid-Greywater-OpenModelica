model GreywaterHybrid
  // Parameters
  parameter Real TankVolume = 150;   // liters per floor
  parameter Real FlowRate = 0.002;   // m3/s (greywater release)
  parameter Real SolarPower = 1000;  // W from PV
  parameter Real UV_Load = 200;      // W (UV lamp + sensors)

  // Variables
  Real HydroPower;
  Real NetPower;

equation
  // Simple hydro generator equation: P = ρ*g*Q*H*η
  HydroPower = 1000 * 9.81 * FlowRate * 10 * 0.6; // 10m head, 60% efficiency

  // Net power balance
  NetPower = SolarPower + HydroPower - UV_Load;
end GreywaterHybrid;
