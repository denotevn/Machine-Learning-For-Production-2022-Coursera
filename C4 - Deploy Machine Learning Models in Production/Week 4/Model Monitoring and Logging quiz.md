1. What issue arises when models are automatically trained on data collected during production?
    + Negative Feedback Loops
    > Data collected in production could be biased or corrupted in some way. If a model is automatically trained on such data, it will perform poorly as a result.
2. Is observability more attainable in modern systems?
    + No, observability gets more challenging when you consider modern systems.
    > Observability becomes a more complex problem when you consider modern systems, which means that you often need to rely on vendor monitoring systems to collect and sometimes aggregate data.
3. In the realm of ML engineering, the operational concerns include monitoring system performance. What measures do we use for doing so? (Select all that apply)
    + Latency
    > Monitoring latency to serve prediction is essential because the expected action should happen immediately for real-time use cases.
    + Uptime
    > Uptime is a measure of computer operating system reliability or stability. It is expressed as the percentage of time a computer can be left unattended without crashing or needing to be rebooted for administrative or maintenance purposes.
    + IO/memory/disk utilization
    > You need to keep a close eye on the system performance, including the usage of CPU, memory, disk, and network I/O. Analyzing these metrics is very significant for ensuring that the machine learning service is fully operational.
4. What are the advantages of Logging for ML Monitoring? (Select all that apply)
    + Logs focus on specific events.
    > While metrics show the trends of a service or an application, logs focus on specific events, including both log messages printed from your application as well as warnings, errors, or debug messages which are generated automatically.
    + Logs provide valuable insight.
    > Event logs provide valuable insight along with context, adding detail that averages and percentiles don’t surface. However, you must be careful to provide the right amount of context without obscuring the really valuable information in too much extraneous detail.
    + Logs are easy to generate.
    > Excellent! Logs are very easy to generate, since they are just strings, blobs of JSON, or typed key-value pairs.

