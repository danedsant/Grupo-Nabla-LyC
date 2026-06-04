const std = @import("std");

fn collatz(start_num: u64) u64 {
    var num = start_num;
    var pasos: u64 = 0;

    while (num > 1) {
        if (num % 2 == 0) {
            num /= 2;
        } else {
            num = 3 * num + 1;
        }
        pasos += 1;
    }
    return pasos;
}

fn pedirNumero(stdout: anytype) !u64 {
    const stdin = std.io.getStdIn().reader();
    var buf: [100]u8 = undefined;

    while (true) {
        try stdout.print("Ingresa un numero entero positivo mayor a 50: ", .{});

        if (try stdin.readUntilDelimiterOrEof(buf[0..], '\n')) |user_input| {
            const line = std.mem.trimRight(u8, user_input, "\r");

            const n = std.fmt.parseInt(u64, line, 10) catch {
                try stdout.print("Error: ingresar un numero valido.\n", .{});
                continue;
            };

            if (n <= 50) {
                try stdout.print("Error: El numero debe ser mayor a 50.\n", .{});
            } else {
                return n;
            }
        }
    }
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    const n = try pedirNumero(stdout);

    var timer = try std.time.Timer.start();

    var pasos_totales: u64 = 0;

    for (1..n) |i| {
        pasos_totales += collatz(i);
    }

    const tiempo_ns = timer.read();

    std.mem.doNotOptimizeAway(pasos_totales);

    // convertir tiempo en Ns a Ms
    const tiempo_ms = @as(f64, @floatFromInt(tiempo_ns)) / 1_000_000.0;

    try stdout.print("Pasos totales calculados: {d}\n", .{pasos_totales});

    try stdout.print("Tiempo preciso (decimales): {d:.4} ms\n", .{tiempo_ms});
}
