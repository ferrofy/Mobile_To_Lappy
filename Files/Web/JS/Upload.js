const Text_Data = document.getElementById("Text_Data")
const Upload = document.getElementById("Upload")
const Write = document.getElementById("Write")
const Status = document.getElementById("Status")

async function Send_Command(Command) {
    const Data = Text_Data.value

    if (!Data.trim()) {
        Status.textContent = "Broooo! Really? Add Some Text First :)"
        return
    }

    const Button = Command === "upload" ? Upload : Write
    Button.disabled = true
    Status.textContent = "Sending Data..."

    try {
        const Response = await fetch("/" + Command, {
            method: "POST",
            headers: {
                "Content-Type": "text/plain; charset=UTF-8"
            },
            body: Data
        })

        const Result = await Response.text()
        Status.textContent = Response.ok ? Result : "Error: " + Result

    } catch (Error) {
        Status.textContent = "Server Connection Failed!"
    } finally {
        Button.disabled = false
    }
}

Upload.addEventListener("click", () => Send_Command("upload"))
Write.addEventListener("click", () => Send_Command("write"))