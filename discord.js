client.on("message", => {
    const channel = message.channel;
    channel.send(message.author.toString());
});
channel.send('hello!')
  .then(message => console.log(`Sent message: ${message.content}`))
  .catch(console.error);